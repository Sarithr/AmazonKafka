import boto3
import logging

logging.basicConfig(level = logging.DEBUG)

class AmazonSQSConnector:
	def __init__(self, region_name, aws_access_key_id, aws_secret_access_key):
		self.region_name = region_name
		self.aws_access_key_id = aws_access_key_id
		self.aws_secret_access_key = aws_secret_access_key
		self.sqs = boto3.client('sqs', region_name = self.region_name, aws_access_key_id = self.aws_access_key_id, aws_secret_access_key = self.aws_secret_access_key)
	
client = boto3.client('kafka')
