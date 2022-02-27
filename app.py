
import boto3

s3 = boto3.resource('s3','us-west-2').meta.client
ssm = boto3.client('ssm', 'us-west-2')
bucket_name = ssm.get_parameter( Name='dragon_data_bucket_name',WithDecryption=False)['Parameter']['Value']
file_name = ssm.get_parameter( Name='dragon_data_file_name',WithDecryption=False)['Parameter']['Value']
# aws ssm put-parameter --type String --name "dragon_data_file_name" --value "dragon_stats_one.json" --overwrite
# aws ssm put-parameter --type String --name "dragon_data_bucket_name" --value "practice-test-fm" --overwrite

def listDragons():
    
    expression = "select * from s3object s"

    result = s3.select_object_content(
            Bucket=bucket_name, # 'practice-test-fm'
            Key=file_name, # 'dragon_stats_one.json',
            ExpressionType='SQL',
            Expression=expression,
            InputSerialization={'JSON': {'Type': 'Document'}},
            OutputSerialization={'JSON': {}}
    )
    
    for event in result['Payload']:
        if 'Records' in event:
            print(event['Records']['Payload'].decode('utf-8'))
   
listDragons()