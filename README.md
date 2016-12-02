# twittTrend

Front End: Ajax, Jquery

Back End: Django

Database: ElasticSearch

AWS: SQS, SNS, EBS

Link: http://tweetygooglemap-dev.us-west-2.elasticbeanstalk.com

This web app is an update to the twittmap app with tweets now indexed in real time and the counter shown for tweets for a particular keyword in real time.

What twittmap did?
This web app is dedicated to displaying the location of keyword based tweets on Google map . 
Tweets were collected using the twitter streaming API and stored on the ElasticSearch. 
Based on what option(keyword) user chooses from the drop down menu, the app retreives the tweets related to that keywords 
from the ElasticSearch and displays the location from where it was tweeted on Google Maps.

How is twittTrend different than twittmap?
The basic functionality remains the same but advancements for elasticity with use of SQS, SNS.

To use, clone the project and enter the required keys for Twitter and Google API and host name of your ElasticSearch.
Install dependencies.
Create a SQS queue on AWS and add the queue name in stream.py file to add the tweets to SQS.
Create a SNS Topic and subscribe it to the yourElasticBeanStalkDomain/SNSEP.
Create an ELasticSearch domain and add the domain in the spaces listed in code to index tweets.

Dependencies: Requests, Tweepy and Elasticsearch. To install dependencies install pip and run "pip install 'name of dependency'" on terminal.


