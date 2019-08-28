import boto3
import json


def send_message(handle, queue_URL, message):
    response = handle.send_message(
        QueueUrl=queue_URL,
        DelaySeconds=1,
        MessageAttributes={
        },
        MessageBody=(
            message
        )
    )
    return response


if __name__ == '__main__':

    sqs = boto3.client('sqs')

    queue_url = 'https://eu-west-1.queue.amazonaws.com/363553477801/aws-primer'

    with open('contacts.json') as f:
        contacts = json.load(f)
        for line in contacts:
            resp = send_message(sqs, queue_url, json.dumps(line))
            print(resp)



