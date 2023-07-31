# Stori Report Mailer

Script to read an CSV with a list of transactions and send an email with the
report to the given email.

## Setup

- create virtual environment and install dependencies:
```
python -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

## Run

```
python index.py <destination_email>
```

- destination_email: the email which receives the report
