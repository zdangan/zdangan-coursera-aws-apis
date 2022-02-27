import boto3

client = boto3.client('s3')

response = client.list_objects(Bucket='practice-test-fm')

for content in response['Contents']:
    obj_dict = client.get_object(Bucket='practice-test-fm', Key=content['Key'])
    print(content['Key'], obj_dict['LastModified'])
