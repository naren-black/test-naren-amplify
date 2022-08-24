import json, boto3

sns = boto3.client('sns')

def handler(event, context):
    print('So the event we have here is:')
    print(event)
    topic_arn = 'arn:aws:sns:ap-southeast-2:697037784263:optus-form-and-status'
    message = "Naren has both sent and recieved this message..hahaha!"
    resp = sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject="NarenTestsSNS-lambda"
    )
    print('The response we got from SNS publish is:')
    print(resp)
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps('Hello from your new Amplify Python lambda written by Naren!')
    }