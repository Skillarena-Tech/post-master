import boto3

class SQSUtil:
    def __init__(self, queue_name: str):
        self.sqs_client = boto3.client('sqs')
        try:
            self.queue_url = self.sqs_client.create_queue(QueueName=queue_name)['QueueUrl']
        except self.sqs_client.exceptions.QueueNameExists:
            self.queue_url = self.sqs_client.list_queues(QueueNamePrefix=queue_name)['QueueUrls'][0]

    def send_message(self, message):
        self.sqs_client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message
        )

    def send_message_with_attributes(self, message, attributes):
        self.sqs_client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message,
            MessageAttributes=attributes
        )

    def send_message_with_delay(self, message, delay_seconds):
        self.sqs_client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message,
            DelaySeconds=delay_seconds
        )

    def send_message_with_attributes_and_delay(self, message, attributes, delay_seconds):
        self.sqs_client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message,
            MessageAttributes=attributes,
            DelaySeconds=delay_seconds
        )

    def send_message_with_group_id(self, message, group_id):
        self.sqs_client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message,
            MessageGroupId=group_id
        )

    def send_message_with_attributes_and_group_id(self, message, attributes, group_id):
        self.sqs_client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message,
            MessageAttributes=attributes,
            MessageGroupId=group_id
        )

    def send_message_with_delay_and_group_id(self, message, delay_seconds, group_id):
        self.sqs_client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message,
            DelaySeconds=delay_seconds,
            MessageGroupId=group_id
        )

    def send_message_with_attributes_and_delay_and_group_id(self, message, attributes, delay_seconds, group_id):
        self.sqs_client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message,
            MessageAttributes=attributes,
            DelaySeconds=delay_seconds,
            MessageGroupId=group_id
        )

    def send_message_with_deduplication_id(self, message, deduplication_id):
        self.sqs_client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message,
            MessageDeduplicationId=deduplication_id
        )