from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
import urllib2
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

keywords=['Elections, Trump, Hillary, Democrat, Republican',
          'health, hospital, gym, fitness, yoga, diet, running, jogging, workout',
          'monument, camping, rental, nyc, london, travelling, backpack, hotel, motel',
          'Religion, Hinduism, Islam, Muslim, Christianity, Jewish, Judaism, Buddhism, Atheism, Pope, Church, Temple',
          'Lunch, Breakfast, Dinner, Brunch, Pizza, restaurant, food, drink, eating',
          'Leisure, Beach, camping, fishing, parks, picnic, outing, entertainment, gaming, playing, movies, songs,\
           reading, novels',
          'Sports, Hockey, Football, soccer, messi, ronaldo, fifa, league, chelsea, cricket, kohli, wrestling,\
           arsenal, manu, barcelona',
          'Science, Technology, engineering, medicine, doctor, drugs, cyber, web, space, tesla, spacex, robotics,\
           machine, learning, AI, Apple, Microsoft, IBM, Google',
          'Peace, Humanity',
          'Fashion, Hollywood, ftv, playboy, fashion, lingerie, bikini, shopping, brands, jewellery']




def Index(Request):
    return render(Request, 'googleMapsTweet/base.html')





def Post(Request):
    if Request.method == "POST":
        msg = Request.POST.get('Search', None)

        # Shashank's Domain
        host = 'Enter Elasticsearch domain here'


        def search(url, term):
            uri = url + term
            response = requests.get(uri)
            results = json.loads(response.text)
            return results

        if msg == 'Elections':
            k = 0
        elif msg == 'Health':
            k = 1
        elif msg == 'Travel':
            k = 2
        elif msg == 'Religion':
            k = 3
        elif msg == 'Food':
            k = 4
        elif msg == 'Leisure':
            k = 5
        elif msg == 'Sports':
            k = 6
        elif msg == 'Science & Technology':
            k = 7
        elif msg == 'Peace':
            k = 8
        elif msg == 'Fashion':
            k = 9

        r = search(host, keywords[k])
        data = [res['_source']['coordinates'] for res in r['hits']['hits']]
        sentiment= [res['_source']['sentiment'] for res in r['hits']['hits']]
        tweet = [res['_source']['tweet'] for res in r['hits']['hits']]
        hits = len(data)
        print (hits)
        length = {'hits': hits}
        coordinates = {}
        for i in range(hits):
            coordinates[i] = {'lat': data[i]['lng'], 'lng': data[i]['lat']}
        data = {'coordinates': coordinates, 'length': length, 'sentiment': sentiment, 'tweet': tweet}

        return JsonResponse(data)
    else:
        msg = Request.GET.get('Search', None)

        # Shashank's Domain
        host = 'Enter elasticsearch domain here'


        def search(url, term):
            uri = url + term
            response = requests.get(uri)
            results = json.loads(response.text)
            return results

        if msg == 'Elections':

            k = 0
        elif msg == 'Health':
            k = 1
        elif msg == 'Travel':
            k = 2
        elif msg == 'Religion':
            k = 3
        elif msg == 'Food':
            k = 4
        elif msg == 'Leisure':
            k = 5
        elif msg == 'Sports':
            k = 6
        elif msg == 'Science & Technology':
            k = 7
        elif msg == 'Peace':
            k = 8
        elif msg == 'Fashion':
            k = 9

        r = search(host, keywords[k])
        data = [res['_source']['coordinates'] for res in r['hits']['hits']]

        hits = len(data)

        data = {'hits': hits}
        return JsonResponse(data)


@csrf_exempt
def snsEP(request):
    context={"message":"Outside"}
    if request.method=="GET":
        return render(request,'googleMapsTweet/base.html')
    else:
        header=json.loads(request.body)
        if header['Type']=="SubscriptionConfirmation":
            subscribleURL=header['SubscribeURL']
            urllib2.urlopen(subscribleURL).read()
        elif header['Type']=="Notification":
            message=json.loads(json.loads(header["Message"]).get('default'))
            tweet=message.get('tweet')
            lat=message.get('lat')
            lng=message.get('lng')
            sentiment=message.get('sentiment')
            # coordinates=[lat,lng]

            e_data={
                "tweet":tweet,
                "coordinates":{"lat":lat,"lng":lng},
                "sentiment":sentiment
            }
            requests.post('Enter elasticsearch domain here',json=e_data)
            context={"message": "I am in notification"}
    return render(request,'googleMapsTweet/base.html',context)