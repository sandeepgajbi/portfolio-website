import smtplib
import ssl
from email.message import EmailMessage

USERNAME = "sandeepgajbi@gmail.com"
PASSWORD = ""  # update key later when you need to run
HOST = "smtp.gmail.com"
PORT = 465


def send_email(user_email, message):
    email = EmailMessage()
    email['From'] = user_email
    email['To'] = USERNAME
    email['Subject'] = 'New message from Streamlit app'
    email.set_content(f"There is a message from: {user_email}\n\nMessage:\n{message}")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.send_message(email)
