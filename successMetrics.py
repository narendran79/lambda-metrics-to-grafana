import json
import boto3
import time

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    cloudwatch.put_metric_data(
        Namespace='LambdaMonitoring',
        MetricData=[{
            'MetricName': 'SuccessCount',
            'Dimensions': [{'Name': 'FunctionType', 'Value': 'Success'}],
            'Timestamp': time.time(),
            'Value': 1,
            'Unit': 'Count'
        }]
    )
    return {
        'statusCode': 200, 
        'body': 'Success metric emitted'
    }