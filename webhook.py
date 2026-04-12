import requests
import json
import time
#webhook_url = 'https://unventurous-droningly-rosaria.ngrok-free.dev/'
webhook_url = 'https://eerpi.ddns.net'


data = { 'name':'whatever',
         'Channel':'test message' }
data2 = { 'name':'John',
            'video':'CIA things'}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type':'application/json'})

#j = requests.get(webhook_url, data=json.dumps(data2), headers={'Content-Type':'application/json'})