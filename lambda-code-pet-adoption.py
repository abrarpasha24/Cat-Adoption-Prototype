import boto3

def lambda_handler(event, context):
    sns = boto3.client('sns')
    accountid = context.invoked_function_arn.split(":")[4]
    region = context.invoked_function_arn.split(":")[3]
    for record in event['Records']:
        message = record['dynamodb']['NewImage']
        catName = message['catName']['S']

        response = sns.publish(
            TopicArn=f'arn:aws:sns:{region}:{accountid}:Adoption-Alerts',
            Message=f"{catName} has been adopted!",
            Subject='Cat adopted!',
        )