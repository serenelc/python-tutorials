import boto3
import json


def read_message(handle, queue_URL):
    response = handle.receive_message(
        QueueUrl=queue_URL,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']
    return message, receipt_handle


if __name__ == '__main__':

    sqs = boto3.client('sqs')

    queue_url = 'https://eu-west-1.queue.amazonaws.com/363553477801/aws-primer'

    while True:
        msg, resp = read_message(sqs, queue_url)
        print(msg['Body'])




