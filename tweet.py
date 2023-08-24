
import tweepy
import requests
import json


consumer_key = ""
consumer_secret_key = ""

access_token =""
access_token_secret = ""

auth = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret_key, access_token=access_token, access_token_secret=access_token_secret)

print(auth)



request = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=5.6037168&appid={OpenWeatherAPIkeyhere}&lon=-0.1869644')

response = request.json()


icon = response['weather'][0]['main']





emoji = {
        'thunderstorm' : "⛈️",    # Code: 200's, 900, 901, 902, 905
        'drizzle' : "🌧️" ,       # Code: 300's
        'rain' : "🌧️"    ,        # Code: 500's
        'snow' : "⛄"  ,       # Code: 600's snowman, 903, 906
        "clear sky" :"🌤️",       # Code: 800 clear sky
        "clouds" : "☁️",      # Code: 801 sun behind clouds         # Code: 802-803-804 clouds general
        "shower rain" : "🌧️",             # Code: 904
    }


tweet = icon + emoji.get(icon.lower())

# auth.create_tweet(text=tweet)

print(auth.get_user(id='elonmusk'))

print(tweet)
