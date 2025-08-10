import boto3
import json
import os

region = os.getenv('AWS_REGION', 'us-east-2')  # fallback region if none set in env
dynamodb = boto3.resource('dynamodb', region_name=region)
table = dynamodb.Table('visitor-counter')

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={'id': 'homepage'},
            UpdateExpression='SET visits = if_not_exists(visits, :start) + :inc',
            ExpressionAttributeValues={
                ':start': 0,
                ':inc': 1
            },
            ReturnValues='UPDATED_NEW'
        )
        # Convert Decimal to int
        visits = int(response['Attributes']['visits'])

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'visits': visits})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
