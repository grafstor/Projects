# Translator

'''
    author: graf stor
    date: 29.11.19
'''

__version__ = "1.0" 

import vk_api
import time
import random
import requests

token = "yourfackingtoken"
vk = vk_api.VkApi(token=token)

a = ''

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"  #это адрес для обращения к API 
KEY = "trnsl.1.1.hui" #Это ваш API ключ 

def translate_me(mytext):
    params = {"key": KEY, "text": mytext, "lang": aa}
    response = requests.get(URL ,params=params)
    return response.json()

def AAA(rtr):
    vk.method("messages.send", {"peer_id": id, "message": rtr, "random_id": random.randint(1, 2147483647)})

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body == '~':
                AAA("ВЫКЛЮЧАЮСЬ")
                break
            else:
                aa = 'en-ru'
                a = str(''.join(translate_me(body)["text"]))
                if a == body:
                    aa = 'ru-en'
                    json = translate_me(body)
                    AAA(str(''.join(json["text"])))
                else:
                    AAA(a)
    except Exception as E:
        time.sleep(1)
