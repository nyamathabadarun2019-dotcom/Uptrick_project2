# Uptrick_project2 — Automated Email Sender

## Problem Statement
Automate routine email communication to save time and improve efficiency.

## Features
- Automated email sending
- Customized content per recipient
- Scheduled email delivery
- Error handling and logging

## Technologies Used
- Python
- smtplib
- email.message
- schedule

## How to Run
1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Update `config.py` with your email credentials (email address and app password).

3. Run the scheduler:

```bash
python scheduler.py
```

## Use Cases
- Client reminders
- Team notifications
- Follow-up emails
- Scheduled announcements

## Files
- `config.py`: configuration for sender account and recipients
- `email_sender.py`: email composition and sending logic
- `scheduler.py`: schedules and triggers sending
- `requirements.txt`: project dependencies

## Notes
- Keep your credentials secure; prefer environment variables for production.

Enjoy using Uptrick_project2 to automate your emails!
