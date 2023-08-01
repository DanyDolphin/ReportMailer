# Dotenv
from dotenv import load_dotenv

# Utilities
from utilities.report import Report

# Clients
from clients.gmail import GmailClient

# Flask
from flask import Flask, request

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    recipient = request.json['email']
    use = request.json['use']

    report = Report()
    if use == 'csv':
        report.load_from_csv('transactions.csv')
    else:
        report.load_from_user(recipient)

    GmailClient().send_email(
        'Your transactions report at Stori',
        report.get_report(format='html'),
        [recipient])

    return 'Mail enviado'
