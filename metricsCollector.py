import boto3
import datetime

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    end_time = datetime.datetime.utcnow()
    start_time = end_time - datetime.timedelta(minutes=5)

    def get_metric(metric_name, function_type):
        response = cloudwatch.get_metric_statistics(
            Namespace='LambdaMonitoring',
            MetricName=metric_name,
            Dimensions=[{'Name': 'FunctionType', 'Value': function_type}],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            Statistics=['Sum']
        )
        datapoints = response['Datapoints']
        return datapoints[0]['Sum'] if datapoints else 0

    success_count = get_metric('SuccessCount', 'Success')
    error_count = get_metric('ErrorCount', 'Error')

    print(f"Success: {success_count}, Error: {error_count}")

    return {
        'statusCode': 200,
        'body': f"Success: {success_count}, Error: {error_count}"
    }