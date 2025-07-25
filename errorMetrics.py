import json
import boto3
import time

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    cloudwatch.put_metric_data(
        Namespace='LambdaMonitoring',
        MetricData=[{
            'MetricName': 'ErrorCount',
            'Dimensions': [{'Name': 'FunctionType', 'Value': 'Error'}],
            'Timestamp': time.time(),
            'Value': 1,
            'Unit': 'Count'
        }]
    )
    return {
        'statusCode': 500, 
        'body': 'Error metric emitted'
    }