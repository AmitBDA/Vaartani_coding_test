import requests
import nltk
import random

api_endpoint='http://127.0.0.1:8080/sendval/'

emma_text = nltk.corpus.gutenberg.sents('austen-emma.txt')
text=[]
data={}
for i in range(len(emma_text)):
    sen=' '.join(emma_text[i])
    text.append(sen)


for i in range(30):
    text_val=random.randint(0,len(text))
    val=random.randint(5,500)
    data['val']=val
    data['text']=str(text[text_val])    
    r = requests.post(url=api_endpoint,params=data)

if r.status_code == 200:
  print(r.content)
