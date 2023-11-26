import boto3
from scripts.config import AWSConfig



class NotificationUtil:
    def __init__(self, topic_name: str):
        if AWSConfig.creds:
            self.sns_client = boto3.client(
                'sns',
                aws_access_key_id=AWSConfig.aws_access_key,
                aws_secret_access_key=AWSConfig.aws_secret_key,
                region_name=AWSConfig.aws_region
            )
        self.sns_client = boto3.client('sns')
        try:
            self.topic_arn = self.sns_client.create_topic(Name=topic_name)['TopicArn']
        except self.sns_client.exceptions.TopicNameExists:
            self.topic_arn = self.sns_client.list_topics()['Topics'][0]['TopicArn']

    
    def send_notification(self, message):
        self.sns_client.publish(
            TopicArn=self.topic_arn,
            Message=message
        )
    
    def send_notification_with_subject(self, message, subject):
        self.sns_client.publish(
            TopicArn=self.topic_arn,
            Message=message,
            Subject=subject
        )
    
    def send_notification_with_attributes(self,  message, attributes):
        self.sns_client.publish(
            TopicArn=self.topic_arn,
            Message=message,
            MessageAttributes=attributes
        )
    
    def send_notification_with_subject_and_attributes(self, message, subject, attributes):
        self.sns_client.publish(
            TopicArn=self.topic_arn,
            Message=message,
            Subject=subject,
            MessageAttributes=attributes
        )
