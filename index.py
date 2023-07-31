# Utils
import sys

# Dotenv
from dotenv import load_dotenv

# Utilities
from utilities.report import Report

# Clients
from clients.gmail import GmailClient

load_dotenv()

report = Report()
report.load_from_csv('transactions.csv')

GmailClient().send_email(
    'Your transactions report at Stori',
    report.get_report(format='html'),
    [sys.argv[1]])
print('Mail enviado')
