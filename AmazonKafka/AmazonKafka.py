import boto3
import logging

logging.basicConfig(level = logging.DEBUG)

logging.info("Connecting Amazon Kafka")
class AmazonKafkaConnector:
	def __init__(self, region_name, aws_access_key_id, aws_secret_access_key):
		self.region_name = region_name
		self.aws_access_key_id = aws_access_key_id
		self.aws_secret_access_key = aws_secret_access_key
		self.client = boto3.client('kafka', region_name = self.region_name, aws_access_key_id = self.aws_access_key_id, aws_secret_access_key = self.aws_secret_access_key)

	def creatingCluster(self, createClusterData):
		response = self.client.create_cluster(
			BrokerNodeGroupInfo = {
			"ClientSubnets" : createClusterData.get("ClientSubnets"),
			"InstanceType" : createClusterData.get("InstanceType")},
    		ClusterName = createClusterData.get("ClusterName"),
    		KafkaVersion = createClusterData.get("KafkaVersion"),
    		NumberOfBrokerNodes = createClusterData.get("NumberOfBrokerNodes"))
		logging.info("Cluster Created")

	def deletingCluster(self):	
		clusterArn = response.get("ClusterArn")
		response = self.client.delete_cluster(
   			ClusterArn = clusterArn,
    		CurrentVersion = deleteClusterData.get("CurrentVersion"))
		logging.info("Cluster Deleted")

createClusterData = {"ClientSubnets" : ["subnet-f55b0ab9", "subnet-a22cccc9", "subnet-dfcf54a4"],
					"InstanceType" : "kafka.m5.large",
					"ClusterName" : "TwoCluster",
					"KafkaVersion" : "2.8.0",
					"NumberOfBrokerNodes" : 90} 
deleteClusterData = {"ClusterArn" : "clusterArn",
					"CurrentVersion" : "2.8.0"}

awsKafkaObject = AmazonKafkaConnector("ap-south-1", "AKIATMGVFWAEJBQPIDEY", "6zQQdkf5a466mREJtQoc8QhGXStF2aEotq7IAVmx")	
awsKafkaObject.creatingCluster(createClusterData)
awsKafkaObject.deletingCluster(deleteClusterData)