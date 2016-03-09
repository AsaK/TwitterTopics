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
    return render(request, 'TwitterTopicsApp/index.html', response)
