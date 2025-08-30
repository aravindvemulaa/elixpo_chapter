import os
import hmac
import hashlib
import jwt
import time
import requests
import asyncio
from flask import Flask, request, abort, jsonify
from dotenv import load_dotenv
from githubScan import PollinationsTokenScanner  

load_dotenv()

# GitHub App credentials
APP_ID = os.getenv("GITHUB_APP_ID")
WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET")
CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")       # from App settings
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")  # from App settings
PRIVATE_KEY = open("private-key.pem", "r").read()  

app = Flask(__name__)

def verify_signature(payload, signature):
    """Verify GitHub webhook signature"""
    mac = hmac.new(WEBHOOK_SECRET.encode(), msg=payload, digestmod=hashlib.sha256)
    return hmac.compare_digest("sha256=" + mac.hexdigest(), signature)

def get_jwt():
    """Create JWT for GitHub App authentication"""
    now = int(time.time())
    payload = {
        "iat": now,
        "exp": now + (10 * 60),  # valid 10 mins
        "iss": APP_ID
    }
    return jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")

def get_installation_token(installation_id):
    """Exchange JWT for installation access token"""
    headers = {
        "Authorization": f"Bearer {get_jwt()}",
        "Accept": "application/vnd.github+json"
    }
    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
    r = requests.post(url, headers=headers)
    r.raise_for_status()
    return r.json()["token"]

@app.route("/auth")
def auth():
    """OAuth callback for GitHub App"""
    code = request.args.get("code")
    if not code:
        return "❌ No code provided", 400

    # Exchange code for access token
    url = "https://github.com/login/oauth/access_token"
    headers = {"Accept": "application/json"}
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code
    }

    r = requests.post(url, data=data, headers=headers)
    r.raise_for_status()
    resp_json = r.json()

    if "access_token" not in resp_json:
        return f"❌ Failed to get token: {resp_json}", 400

    access_token = resp_json["access_token"]

    # (Optional) get user info
    user_info = requests.get(
        "https://api.github.com/user",
        headers={"Authorization": f"token {access_token}"}
    ).json()

    return f"✅ App installed for user: {user_info.get('login')}"

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Hub-Signature-256")
    if not verify_signature(request.data, signature):
        abort(400, "Invalid signature")

    event = request.headers.get("X-GitHub-Event", "ping")
    payload = request.json

    if event == "ping":
        return jsonify({"msg": "pong"}), 200

    if event == "push":
        repo = payload["repository"]["full_name"]
        username = payload["repository"]["owner"]["login"]
        installation_id = payload["installation"]["id"]

        print(f"📦 Push detected on {repo} by {username}")

        # get installation token
        token = get_installation_token(installation_id)
        os.environ["githubToken"] = token  # inject into scanner

        # run scanner
        scanner = PollinationsTokenScanner()
        asyncio.run(scanner.scan_user_protection(username))

    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
