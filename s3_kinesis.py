import boto3

s3 = boto3.client('s3')
kinesis = boto3.client('kinesis')

def lambda_handler(event):
    if event:
        bucket_name = event["Records"][0]['s3']['bucket']['name']
        file_name = event["Records"][0]['s3']['object']['key']
        file_obj = s3.get_object(Bucket=bucket_name, Key=file_name)
        file_content = file_obj["Body"].read().decode('utf-8')
        kinesis.put_record(Data=bytes(file_content, 'utf-8'), StreamName='my_fake_stream', PartitionKey='vjfirst')
