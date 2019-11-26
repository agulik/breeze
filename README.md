# Breeze

Manage AWS EC2 instance snapshots

## About

This project uses boto3 to manage AWS EC2 instance snapshots.

## Configuration

Breeze uses the configuration file created by the AWS cli. e.g.
`aws configure --profile breeze`

## Running

`pipenv run python breeze.py <command> <--project=PROJECT>`

*command* is list, start or stop <br>
*project* is optional