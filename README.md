# aws_sns_demo
Description: how to subscrib sns-message via `http(s) endpoint`.
 
## Usage
Before start , install dependence.
```
pip3 install -r requirements.txt
```
First, Set up your own http server.
```
python3 http_server.py --port 8080
```
The command should be run on the machine which owned public ip.
For test or dev environment, you may choose `NAT server` to expose your local server, such as ngrok.(https://ngrok.com/)

Second,
enter to your aws console, setting your topic, enter the topic you setted just now, and find `create subscription` button in aws console (refs: https://us-west-1.console.aws.amazon.com/sns/v3/home?region=us-west-1#/topics). Choose option type `http(s) endpoint`, then fill your own `public server host` and try to subscrib.

Third,
Find the `publish message` button in the same page, try to send your message.
## Caveat: 
About sns-message-validator, due to aws still not supply offical sns-message-validator. There are some validator from aws user written. The validator in this repo also choosen from them.

## Refs

### Data format
SNS will send 3 type event, which`s detail message as below,

SubscriptionConfirmation Example:
```
{
    "Type" : "SubscriptionConfirmation",
    "MessageId" : "165545c9-2a5c-472c-8df2-7ff2be2b3b1b",
    "Token" : "2336412f37...",
    "TopicArn" : "arn:aws:sns:us-west-2:123456789012:MyTopic",
    "Message" : "You have chosen to subscribe to the topic arn:aws:sns:us-west-2:123456789012:MyTopic.\nTo confirm the subscription, visit the SubscribeURL included in this message.",
    "SubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=ConfirmSubscription&TopicArn=arn:aws:sns:us-west-2:123456789012:MyTopic&Token=2336412f37...",
    "Timestamp" : "2012-04-26T20:45:04.751Z",
    "SignatureVersion" : "1",
    "Signature" : "EXAMPLEpH+DcEwjAPg8O9mY8dReBSwksfg2S7WKQcikcNKWLQjwu6A4VbeS0QHVCkhRS7fUQvi2egU3N858fiTDN6bkkOxYDVrY0Ad8L10Hs3zH81mtnPk5uvvolIC1CXGu43obcgFxeL3khZl8IKvO61GWB6jI9b5+gLPoBc1Q=",
    "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem"
}
```

UnsubscribeConfirmation Example:
```
{
    "Type" : "UnsubscribeConfirmation",
    "MessageId" : "47138184-6831-46b8-8f7c-afc488602d7d",
    "Token" : "2336412f37...",
    "TopicArn" : "arn:aws:sns:us-west-2:123456789012:MyTopic",
    "Message" : "You have chosen to deactivate subscription arn:aws:sns:us-west-2:123456789012:MyTopic:2bcfbf39-05c3-41de-beaa-fcfcc21c8f55.\nTo cancel this operation and restore the subscription, visit the SubscribeURL included in this message.",
    "SubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=ConfirmSubscription&TopicArn=arn:aws:sns:us-west-2:123456789012:MyTopic&Token=2336412f37fb6...",
    "Timestamp" : "2012-04-26T20:06:41.581Z",
    "SignatureVersion" : "1",
    "Signature" : "EXAMPLEHXgJm...",
    "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem"
}
```

Notification Example:
```
{
    "Type" : "Notification",
    "MessageId" : "22b80b92-fdea-4c2c-8f9d-bdfb0c7bf324",
    "TopicArn" : "arn:aws:sns:us-west-2:123456789012:MyTopic",
    "Subject" : "My First Message",
    "Message" : "Hello world!",
    "Timestamp" : "2012-05-02T00:54:06.655Z",
    "SignatureVersion" : "1",
    "Signature" : "EXAMPLEw6JRN...",
    "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem",
    "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:123456789012:MyTopic:c9135db0-26c4-47ec-8998-413945fb5a96"
    }
}
```

### links
https://docs.aws.amazon.com/sns/latest/dg/sns-message-and-json-formats.html
https://gist.github.com/stebunovd/c4122c5a9ae70185c20c7b2f1ec03cfc
https://github.com/wlwg/aws-sns-message-validator/tree/master
https://aws.amazon.com/cn/blogs/security/sign-amazon-sns-messages-with-sha256-hashing-for-http-subscriptions/
https://docs.aws.amazon.com/zh_cn/sns/latest/dg/sns-verify-signature-of-message.html


