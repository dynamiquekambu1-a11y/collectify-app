import smtplib
from email.mime.text import MIMEText
from config import EMAIL, PASSWORD

def send_email(to_email, subject, body):

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

        return "sent"

    except Exception as e:
        return str(e)
