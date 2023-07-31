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
