import boto3
import json
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event,context) :
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    
    json_object = s3_client.get_object(Bucket=bucket_name,Key=json_file_name)
    jsonFileReader = json_object['Body'].read()
    jsonDist = json.loads(jsonFileReader)
    
    
    table = dynamodb.Table('company_details')
    table.put_item(Item=jsonDist)
    return "Successfully added item to the table"