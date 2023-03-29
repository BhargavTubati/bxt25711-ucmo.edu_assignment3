import boto3
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')
queue_name = config['QUEUE']['Name']

#Creation of SQS client
sqs = boto3.client('sqs')

#Creation of a new queue
response = sqs.create_queue(
    QueueName = queue_name
)

#Queue URL
queue_url = response['QueueUrl']
print(f'Queue created: {queue_url}')

def send_message_to_queue(message):
    # Loading configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')
    queue_name = config['QUEUE']['Name']

# Create an SQS client
    sqs = boto3.client('sqs')

    # Get the queue URL
    response = sqs.get_queue_url(
        QueueName=queue_name
    )
    queue_url = response['QueueUrl']

    # Send the message to the queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message)
    )

    # Print the message ID
    print(f'Message sent: {response["MessageId"]}')

if __name__ == '__main__':
    # Send a message to the queue
    message = {'message': 'Hello, SQS!'}
    send_message_to_queue(message)



