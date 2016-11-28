import time
from alchemyapi import AlchemyAPI
import boto3
import json

sqs = boto3.resource('sqs')
sns = boto3.client('sns')
queue = sqs.get_queue_by_name(QueueName='tweetsIn')
alchemiapi = AlchemyAPI()
arn = 'arn:aws:sns:us-east-1:370645577623:twitterApp'
def worker(queue):
    while True:
        messages = queue.receive_messages(MessageAttributeNames=['Tweet', 'Latitude', 'Longitude'])
        if len(messages)>0:
            for message in messages:
            
                if message.message_attributes is not None:
                    tweet = message.message_attributes.get('Tweet').get('StringValue')
                    lat = message.message_attributes.get('Latitude').get('StringValue')
                    lng = message.message_attributes.get('Longitude').get('StringValue')
                    
                    try:
                        response = alchemiapi.sentiment('text',tweet)
                        senti = response.get('docSentiment').get('type')
                    except Exception as e:
                        senti = "neutral"
                
                    sns_message = {"tweet":tweet, "lat":lat, "lng": lng, "sentiment":senti}
                    print("SNS messsage: "+str(sns_message))
                    sns.publish(TargetArn=arn, Message=json.dumps({'default':json.dumps(sns_message)}))
                
                message.delete()
        else:
            time.sleep(1)
if __name__ == '__main__':
    worker(queue)
while True:
    pass
