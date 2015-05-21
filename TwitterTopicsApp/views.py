from django.shortcuts import render
from requests_oauthlib import OAuth1Session
import json
# Create your views here.
def index(request):
	#PUT YOU APP TWITER KEYS HERE
    api_key = ""
    api_secret = ""
    access_token = ""
    access_token_secret = ""
    session = OAuth1Session(api_key, api_secret, access_token, access_token_secret)
    response = session.get("https://api.twitter.com/1.1/trends/place.json?id=1")
    worlds = json.loads(response.content)[0]["trends"]
    context = {'tt1': worlds[0]["name"],
               'tt2': worlds[1]["name"],
               'tt3': worlds[2]["name"],
               'tt4': worlds[3]["name"],
               'tt5': worlds[4]["name"],
               'tt6': worlds[5]["name"],
               'tt7': worlds[6]["name"],
               'tt8': worlds[7]["name"],
               'tt9': worlds[8]["name"],
               'tt10': worlds[9]["name"],
               }

    print "Status da consulta " + str(response.status_code)
    return render(request, 'TwitterTopicsApp/index.html', context)
