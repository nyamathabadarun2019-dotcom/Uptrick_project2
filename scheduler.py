# scheduler.py

import schedule
import time
from email_sender import send_email

recipients = [
    {
        "email": "recipient1@gmail.com",
        "name": "Arun",
        "purpose": "Client Follow-up"
    },
    {
        "email": "recipient2@gmail.com",
        "name": "Ravi",
        "purpose": "Meeting Reminder"
    },
    {
        "email": "recipient3@gmail.com",
        "name": "Sneha",
        "purpose": "Status Update"
    }
]

def send_scheduled_emails():
    for user in recipients:
        subject = f"Automated Email – {user['purpose']}"
        body = f"""
Hello {user['name']},

This is an automated email regarding: {user['purpose']}.

We are reaching out to ensure smooth communication and timely updates.

Thank you for your time.

Regards,
Automation Team
"""
        send_email(user["email"], subject, body)

# Schedule email (Example: daily at 10:00 AM)
schedule.every().day.at("10:00").do(send_scheduled_emails)

print("📅 Automated Email Scheduler Running...")

while True:
    schedule.run_pending()
    time.sleep(1)
