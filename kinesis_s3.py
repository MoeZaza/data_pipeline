import boto3
import base64

s3 = boto3.resource('s3')
ev_lst = []

def lambda_handler(event):
    for record in event['Records']:
        payload = base64.b64decode(record["kinesis"]["data"])
        ev_lst.append(payload)

    s3.Object('kotharv-target', 'test.txt').put(Body=str(ev_lst))