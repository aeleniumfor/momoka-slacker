import requests
import json,random


def books():
    url='https://api.syosetu.com/novelapi/api/?out=json&lim=100'
    context = requests.get(url)
    context = json.loads(context.text)
    del context[0]
    rand = random.randint(0,len(context)-1)
    book = context[rand]
    c = book["title"]+"\n---------------------------\n"+book["story"]+"\n---------------------------\n"+'http://ncode.syosetu.com/'+book["ncode"]
    return c
