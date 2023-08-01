# Utils
import json

# Utilities
from utilities.report import Report

# Clients
from clients.gmail import GmailClient


def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])
        recipient = body['email']
        use = body['use']
    elif event['httpMethod'] == 'GET':
        recipient = event['queryStringParameters']['email']
        use = event['queryStringParameters']['use']

    report = Report()
    if use == 'csv':
        report.load_from_csv('transactions.csv')
    else:
        report.load_from_user(recipient)

    GmailClient().send_email(
        'Your transactions report at Stori',
        report.get_report(format='html'),
        [recipient])

    return {
        'statusCode': 200,
        'body': json.dumps('Mail enviado')}
