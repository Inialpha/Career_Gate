#!/usr/bin/python3
import requests


from datetime import datetime, timedelta
current_date = datetime.now()
yesterday = (current_date - timedelta(days=1)).strftime('%Y-%m-%d')
last_week = (current_date - timedelta(days=7)).strftime('%Y-%m-%d')
print("Yesterday's date:", yesterday)


url = "https://newsapi.org/v2/everything"

data = {'q': 'job AND career AND employment',
        'from': yesterday,
        }

headers = {'x-api-key': 'a73a26f264ce491d9d5769d880731b2e',
        'Content-Type': 'application/json'
        }

response = requests.get(url, params=data, headers=headers)
data = response.json()
articles = (data.get('articles'))

#url = articles[0].get('url')
#html = requests.get(url)

#print(response.json())
#rint(response.json())
#for article in articles:
#    url = (article.get('url'))
#    html = requests.get(url)
#   print(html.__dict__)
