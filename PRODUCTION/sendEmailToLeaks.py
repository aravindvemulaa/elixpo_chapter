import smtplib
import asyncio
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from prepareEmailPayload import build_html_body
from dotenv import load_dotenv
import os
load_dotenv()

# Your email credentials
sender_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")

if not sender_email or not password:
    raise ValueError("EMAIL_USER and EMAIL_PASS must be set in the .env file")

receivedQueue = []
sentQueue = []
failedQueue = []

async def send_email(receiver_email, repo_url, file_path, line_number, token, commit_hash, diff_info):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Polli Leaks - Token Exposure Alert"
    
    body = build_html_body(
        token_leaks=[{"repo_url": repo_url, "file_path": file_path, "line_number": line_number, "token": token}],
        commit_hash=commit_hash,
        diff_info=diff_info
    )
    msg.attach(MIMEText(body, "html", "utf-8"))
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return {"status": "success", "email": receiver_email}
    except Exception as e:
        return {"status": "error", "email": receiver_email, "message": str(e)}

async def process_queue():
    while receivedQueue:
        receiver_email = receivedQueue.pop(0)
        result = await send_email(receiver_email)
        if result["status"] == "success":
            sentQueue.append(receiver_email)
            print(f"Email sent to {receiver_email}")
        else:
            failedQueue.append({"email": receiver_email, "error": result["message"]})
            print(f"Failed to send email to {receiver_email}: {result['message']}")

    print(f"Sent: {sentQueue}")
    print(f"Failed: {failedQueue}")

if __name__ == "__main__":
    asyncio.run(process_queue())