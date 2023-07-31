# Utils
import sys
import json

# Utilities
from utilities.report import Report

# Clients
from clients.gmail import GmailClient


def lambda_handler(event, context):
    report = Report()
    report.load_from_csv('transactions.csv')
    GmailClient().send_email(
        'Your transactions report at Stori',
        report.get_report(format='html'),
        [sys.argv[1]])
    return {
        'statusCode': 200,
        'body': json.dumps('Mail enviado')}
