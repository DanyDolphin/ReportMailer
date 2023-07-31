# Stori Report Mailer

Script to read an CSV with a list of transactions and send an email with the
report to the given email.

## Setup

```
docker build -t report-mailer .
```

## Run

```
docker run report-mailer <destination_email>
```

- destination_email: the email which receives the report

## Deploy to AWS Lambda

To deploy this script to an AWS Lambda, run the following script:
```
bash ./scripts/build-lambda.sh
```

This will create a `deployment.zip` file that you can load inside AWS Lambda.
