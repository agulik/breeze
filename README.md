# Breeze

Manage AWS EC2 instance snapshots

## About

This project uses boto3 to manage AWS EC2 instance snapshots.

## Configuration

Breeze uses the configuration file created by the AWS cli. e.g.
`aws configure --profile breeze`

## Running

`pipenv run python breeze.py <command> <subcommand> <--project=PROJECT>`

*command* is instances, volumes or snapshots <br>
*subcommand* - depends on command <br>
*project* is optional