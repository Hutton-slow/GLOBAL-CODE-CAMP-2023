# Your API key is: 1e59334392114f02b478215a2d6f4ae5

import requests

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=1e59334392114f02b478215a2d6f4ae5')


response = requests.get(url).json()
# print(response)
articles = response['articles']

for i in articles:
    print(f"{i['title']}\n{i['description']}\n{i['content']}\n\nBy - {i['author']}\n\n\n")
# print(articles)