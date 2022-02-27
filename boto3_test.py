import boto3
# import pandas as pd


'''list all of the contents of a s3 bucket using boto3 client'''
client = boto3.client('s3')

response = client.list_objects(Bucket='practice-test-fm')

for k, v in response['Contents'][0].items():
    print(k)

for _ in response['Contents']:
    print(_.get('Key'), _.get('LastModified'))




'''list all of the contents of a s3 bucket using boto3 resource'''
s3 = boto3.resource('s3')
bucket = s3.Bucket('practice-test-fm')

for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)
