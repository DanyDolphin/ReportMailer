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
print(report.get_report(format='text'))

GmailClient().send_email(
    'Tu reporte de transacciones Stori',
    report.get_report(format='text'),
    [sys.argv[1]])
print('Mail enviado')
