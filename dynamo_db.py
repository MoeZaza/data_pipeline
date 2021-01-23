import boto3
import base64


dynamodb = boto3.resource('dynamodb')

def lambda_handler(event):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])

    main_lst = payload.decode().split('\r\n')
    # Assign first index value as keys
    keys = main_lst[0].split(',')

    # Loop through the records in the uploaded CSV file
    for i in range(1, len(main_lst) - 1):
        record = main_lst[i].split(',')
        arr = {}
        # Loop through keys to create item
        for j in record:
            value = record[j] if record[j] is not None else '5'
            arr[keys[j]] = int(value) if keys[j] == 'Complain_ID' else value

        (dynamodb.Table('cc_complaint')).put_item(Item=arr)
