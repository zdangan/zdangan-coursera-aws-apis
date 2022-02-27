import boto3

s3 = boto3.resource('s3', 'us-west-2')
bucket = s3.Bucket('practice-test-fm')
# the objects are available as a collection on the bucket object
for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)
    
# access the client from the resource 
s3_client = boto3.resource('s3').meta.client