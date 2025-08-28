import re
import asyncio
import requests
import time
import os
import hashlib
import base64
from dotenv import load_dotenv
from getFileExtension import findExtensions
load_dotenv()

class PollinationsTokenScanner:
    def __init__(self):
        self.github_token = os.getenv("githubToken")
        self.token_regex = re.compile(r'Poll_[A-Z0-9]{8}[A-Z0-9]{11}[A-Z0-9]{8}')
        self.user_mapping = {
            "Circuit-Overtime": 74301576
        }
        
    def hash_to_alphanum(self, s, length):
        """Convert string to alphanumeric hash"""
        h = hashlib.sha256(s.encode()).digest()
        b32 = base64.b32encode(h).decode('utf-8')
        alphanum = ''.join(c for c in b32 if c.isalnum())
        return alphanum[:length]

    def generate_pollinations_token(self, username, github_id):
        """Generate expected token for a user"""
        part1 = self.hash_to_alphanum(username, 8)
        part2 = self.hash_to_alphanum(str(github_id), 11)
        combined = username + str(github_id)
        part3 = self.hash_to_alphanum(combined, 8)
        return "Poll_" + part1 + part2 + part3

    def scan_text_for_tokens(self, text, file_path=""):
        """Scan text content for Pollinations tokens using regex"""
        findings = []
        lines = text.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # Find all potential tokens using regex
            matches = self.token_regex.findall(line)
            
            for token in matches:
                # Validate against known users
                for username, github_id in self.user_mapping.items():
                    expected_token = self.generate_pollinations_token(username, github_id)
                    if token == expected_token:
                        findings.append({
                            'file_path': file_path,
                            'line_number': line_num,
                            'token': token,
                            'username': username,
                            'github_id': github_id,
                            'line_content': line.strip()
                        })
                        break
        
        return findings

    async def search_github_repos(self, username):
        extensionList = await findExtensions()
        search_queries = [
            f"Poll_ in:file user:{username} extension:{ext}" for ext in extensionList
        ]

        all_findings = []

        for query in search_queries:
            print(f"🔍 Scanning: {query}")
            findings = self._execute_search(query)
        
        all_findings = []
        
        for query in search_queries:
            print(f"🔍 Scanning: {query}")
            findings = self._execute_search(query)
            all_findings.extend(findings)
            time.sleep(2)  # Rate limit protection
            
        return all_findings

    def _execute_search(self, query):
        params = {
            "q": query,
            "per_page": 100
        }
        headers = {
            "Authorization": f"Bearer {self.github_token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        
        try:
            response = requests.get("https://api.github.com/search/code", 
                                  params=params, headers=headers)
            
            if response.status_code == 403:
                reset = int(response.headers.get("X-RateLimit-Reset", time.time()+60)%60)
                sleep_time = max(reset - time.time(), 5)
                print(f"   Rate limited, sleeping {sleep_time:.0f}s")
                time.sleep(sleep_time)
                return self._execute_search(query)
            
            if response.status_code != 200:
                print(f"   Error: {response.status_code}")
                return []
                
            items = response.json().get("items", [])
            findings = []
            
            for item in items:
                # Get file content
                content = self._get_file_content(item["url"])
                if content:
                    file_findings = self.scan_text_for_tokens(content, item["path"])
                    for finding in file_findings:
                        finding.update({
                            'repo_url': item["repository"]["html_url"],
                            'file_url': item["html_url"],
                            'owner': item["repository"]["owner"]["login"]
                        })
                        findings.append(finding)
                        
            return findings
            
        except Exception as e:
            print(f"   Search error: {e}")
            return []

    def _get_file_content(self, content_url):
        headers = {
            "Authorization": f"Bearer {self.github_token}",
            "Accept": "application/vnd.github.raw"
        }
        
        try:
            response = requests.get(content_url, headers=headers)
            if response.status_code == 200:
                return response.text
        except:
            pass
        return None

    async def scan_user_protection(self, username):
        print(f"🛡️  POLLINATIONS TOKEN PROTECTION SCAN")
        print(f"👤 Scanning for user: {username}")
        print("=" * 60)
        
        if username not in self.user_mapping:
            print(f"❌ User {username} not registered for protection")
            return []
            
        findings = await self.search_github_repos(username)
        
        if not findings:
            print("✅ No exposed Pollinations tokens found!")
        else:
            print(f"🚨 ALERT: Found {len(findings)} exposed tokens!")
            print("\n📋 EXPOSURE REPORT:")
            print("=" * 60)
            
            for finding in findings:
                print(f"🗂️  Repository: {finding['repo_url']}")
                print(f"📄 File: {finding['file_path']} (line {finding['line_number']})")
                print(f"🔑 Token: {finding['token']}")
                print(f"👤 User: {finding['username']} ({finding['github_id']})")
                print(f"🔗 Direct link: {finding['file_url']}")
                print(f"📝 Content: {finding['line_content']}")
                print("-" * 40)
                
            # Save report
            self._save_report(findings, username)
            
        return findings

    def _save_report(self, findings, username):
        """Save exposure report to file"""
        report_file = f"pollinations_exposure_report_{username}.log"
        with open(report_file, "w") as f:
            f.write(f"POLLINATIONS TOKEN EXPOSURE REPORT\n")
            f.write(f"User: {username}\n")
            f.write(f"Scan Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Exposed Tokens Found: {len(findings)}\n")
            f.write("=" * 60 + "\n\n")
            
            for finding in findings:
                f.write(f"Repository: {finding['repo_url']}\n")
                f.write(f"File: {finding['file_path']} (line {finding['line_number']})\n")
                f.write(f"Token: {finding['token']}\n")
                f.write(f"User: {finding['username']} ({finding['github_id']})\n")
                f.write(f"Direct Link: {finding['file_url']}\n")
                f.write(f"Content: {finding['line_content']}\n")
                f.write("-" * 60 + "\n")
                
        print(f"📄 Report saved to: {report_file}")

# GitHub App usage
if __name__ == "__main__":
    async def main():
        scanner = PollinationsTokenScanner()
        findings = await scanner.scan_user_protection("Circuit-Overtime")
        print(f"Total Findings: {len(findings)}")
    asyncio.run(main())
        
    