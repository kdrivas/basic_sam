import json
import boto3

# import requests


def lambda_handler(event, context):
	"""
		Example
	"""
	s3 = boto3.resource('s3')
	copy_source = {
				'Bucket': 'test-experiments-bucket',
				'Key': 'original/aplication.txt'
	}
	bucket = s3.Bucket('test-experiments-bucket')
	bucket.copy(copy_source, 'copy_folder/aplication.txt')

	return {
		"statusCode": 200,
		"body": json.dumps({
			"message": "hello world"
		})
	}
