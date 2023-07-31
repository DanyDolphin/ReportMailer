# Utils
import os
import smtplib

# Email
from email.mime.text import MIMEText


class GmailClient:
    def __init__(self):
        self.sender = os.getenv('GMAIL_SENDER')
        self.password = os.getenv('GMAIL_PASSWORD')

    def send_email(self, subject, body, recipients):
        msg = MIMEText(body, 'html')
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self.sender, self.password)
            smtp_server.sendmail(self.sender, recipients, msg.as_string())
