import boto3

def create_cloudwatch_alarm(metric_name, threshold, sns_topic_arn):
    cloudwatch = boto3.client('cloudwatch')
    response = cloudwatch.put_metric_alarm(
        AlarmName='FraudDetectionAlarm',
        MetricName=metric_name,
        Namespace='AWS/Lambda',
        Statistic='Sum',
        Period=300,
        Threshold=threshold,
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        AlarmActions=[sns_topic_arn]
    )
    return response

if __name__ == "__main__":
    sns_topic_arn = "arn:aws:sns:region:account-id:topic-name"
    response = create_cloudwatch_alarm("Invocations", 100, sns_topic_arn)
    print("CloudWatch Alarm Created:", response)
