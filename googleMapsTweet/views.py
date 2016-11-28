from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
# from .forms import MyForm
import requests
import json

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
        host = ''

        

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
        data = [res['_source']['coordinates']['coordinates'] for res in r['hits']['hits']]

        hits = len(data)
        print (hits)
        length = {'hits': hits}
        coordinates = {}
        for i in range(hits):
            coordinates[i] = {'lat': data[i][0], 'lng': data[i][1]}

        data = {'coordinates': coordinates, 'length': length}

        return JsonResponse(data)