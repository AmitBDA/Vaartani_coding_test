import requests
#import json

api_endpoint='http://127.0.0.1:8080/sendval/'
data={
'val': 20,
'text': 'some free text in English'
}

r = requests.post(url=api_endpoint,params=data)

if r.status_code == 200:
  print(r.content)


