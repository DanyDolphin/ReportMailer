# Utils
import sys
import json

# Utilities
from utilities.report import Report

# Clients
from clients.gmail import GmailClient


def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])
        recipient = body['email']
    elif event['httpMethod'] == 'GET':
        recipient = event['queryStringParameters']['email']

    report = Report()
    report.load_from_csv('transactions.csv')
    GmailClient().send_email(
        'Your transactions report at Stori',
        report.get_report(format='html'),
        [recipient])
    return {
        'statusCode': 200,
        'body': json.dumps('Mail enviado')}
