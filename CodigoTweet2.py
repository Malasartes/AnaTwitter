#-*- coding: utf-8 -*- 
import tweepy
from tweepy import OAuthHandler
import json
import io 
import sys

sys.stdout.encoding
'UTF-8'

 
consumer_key = '2IeLEqz9Cvtn2M98FClJoqFF2'
consumer_secret = 'bfK122blSgOE79395h0WgRF90oyW80GFT3g8JS5PL3YQopTRJM'
access_token = '497493775-JVGxBhJPF2KhyiIluivHvWMHl30x9upyjeemKqHT'
access_secret = 'vxl2OpxAPL55ruzIp3da2W9bVJZlkbQkcq5HuEAePfbkf'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

#Correcto/Inactivo solo imprime
#def process_or_store(tweet):
    #print(json.dumps(tweet))

#Correcto/Activo crea y guarda archivo
def process_or_store(tweet07):
    with io.open(u'tweet07.json', 'w', encoding='utf-8') as f:
         f.write(json.dumps(tweet07, ensure_ascii=False, indent=4))
    

#Correcto/Inactivo
#for tweet in tweepy.Cursor(api.home_timeline).items(1):
     #process_or_store(tweet._json)
    
#Correcto/Activo
for tweet in tweepy.Cursor(api.user_timeline).items(1):
    process_or_store(tweet._json)
    




