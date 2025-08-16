import re
import requests
import time
import hashlib
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
import os
load_dotenv()

# ================================
# CONFIG
# ================================
GITHUB_TOKEN = os.getenv("githubToken")
TOKEN_REGEX = re.compile(r'^Poll_[A-Z2-7]{8}[A-Z2-7]{11}[A-Z2-7]{8}$')
SEARCH_QUERY = "Poll_ in:file"
FILE_EXTENSIONS = ["md", "env", "json", "py", "js"]
RESULTS_PER_PAGE = 30
MAX_PAGES = 10
MAX_THREADS = 5
OUTPUT_LOG = "pollinations_token_leaks_validated.log"

# Mapping of username -> GitHub ID
USER_MAPPING = {
    "Circuit-Overtime": 74301576,
    # Add more users here
}

# ================================
# HELPER FUNCTIONS
# ================================
def hash_to_alphanum(s, length):
    h = hashlib.sha256(s.encode()).digest()
    b32 = base64.b32encode(h).decode('utf-8')
    alphanum = ''.join(c for c in b32 if c.isalnum())
    return alphanum[:length]

def generate_pollinations_token(username, github_id):
    part1 = hash_to_alphanum(username, 8)
    part2 = hash_to_alphanum(str(github_id), 11)
    combined = username + str(github_id)
    part3 = hash_to_alphanum(combined, 8)
    return "Poll_" + part1 + part2 + part3

def is_valid_token(token):
    """Check token against all known username-ID pairs."""
    for user, gid in USER_MAPPING.items():
        if token == generate_pollinations_token(user, gid):
            return True, user, gid
    return False, None, None

def github_search_code(query, file_ext=None, page=1):
    url = "https://api.github.com/search/code"
    q = query
    if file_ext:
        q += f" extension:{file_ext}"
    params = {"q": q, "per_page": RESULTS_PER_PAGE, "page": page, "sort": "indexed"}
    headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 403:
        reset = int(response.headers.get("X-RateLimit-Reset", time.time()+60))
        sleep_time = max(reset - time.time(), 5)
        print(f"Rate limited, sleeping {sleep_time:.0f}s")
        time.sleep(sleep_time)
        return github_search_code(query, file_ext, page)
    response.raise_for_status()
    return response.json().get("items", [])

def fetch_raw_file(html_url):
    raw_url = html_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    try:
        response = requests.get(raw_url, timeout=10)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error fetching {raw_url}: {e}")
    return ""

def scan_content_for_tokens(content, repo_url, file_path):
    matches = []
    for i, line in enumerate(content.splitlines(), 1):
        m = TOKEN_REGEX.search(line)
        if m:
            token = m.group()
            valid, user, gid = is_valid_token(token)
            if valid:
                matches.append((i, token, user, gid))
    if matches:
        with open(OUTPUT_LOG, "a") as f:
            for lineno, token, user, gid in matches:
                f.write(f"{repo_url} | {file_path} | line {lineno} | {token} | {user} | {gid}\n")
        print(f"[+] Found {len(matches)} valid token(s) in {repo_url}/{file_path}")

def process_file(item):
    repo_url = item["repository"]["html_url"]
    file_path = item["path"]
    html_url = item["html_url"]
    content = fetch_raw_file(html_url)
    if content:
        scan_content_for_tokens(content, repo_url, file_path)

# ================================
# MAIN SCAN LOOP
# ================================
def main():
    for ext in FILE_EXTENSIONS:
        print(f"\nScanning .{ext} files...")
        for page in range(1, MAX_PAGES+1):
            results = github_search_code(SEARCH_QUERY, ext, page)
            if not results:
                break
            with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                futures = [executor.submit(process_file, item) for item in results]
                for future in as_completed(futures):
                    future.result()  # wait for all to finish
            time.sleep(2)  # gentle delay between pages

if __name__ == "__main__":
    main()
