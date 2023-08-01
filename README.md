# Stori Report Mailer

Script to read an CSV with a list of transactions and send an email with the report to the given email.

## Requirements

- Docker and docker compose

## Setup

1. Copy the content of `.env.example` file into an `.env` file. Store the values of GMAIL_SENDER and GMAIL_PASSWORD variables with and email and an app password.

2. Run the following commands:

```
docker-compose build
docker-compose exec mailer bash

# Inside storireportmailer-mailer container
python manage.py create_db
python manage.py load_test_data
```

You can edit test data at `./models/mock.py`

## Run

```
docker-compose up
```

## Usage

The mailer container export an endpoint at port 5000 with the given specifications:

/ (POST)

Body:

    - email: email to send the report. If "use" value is not "csv", it retrieves transactions from database, related to the given email.
    - use: if value is "csv", it load transactions from transactions.csv


## Deploy to AWS Lambda

To deploy this script to an AWS Lambda, run the following script:
```
bash ./scripts/build-lambda.sh
```

This will create a `deployment.zip` file that you can load inside AWS Lambda.

The lambda expects same "email" and "use" values either form body or query params.
