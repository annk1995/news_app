from app import app
from app.models import news

import urllib.request,json
from .models import news

News=news.News
api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]

def get_news():
    """
    method to get headlines
    """
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        print(get_news_response)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news(news_results_list)

            
def process_news(get_news_response):
     news_results = []
     for news_item in get_news_response:
       name = news_item.get('name')
       author = news_item.get('author')
       url = news_item.get('url')
       urlToImage = news_item.get('urlToImage')
       title = news_item.get('title')
       description = news_item.get('description')
       publishedAt = news_item.get('publishedAt')
       if urlToImage and author and title:
        news_object = News(author, title, description, url, urlToImage, publishedAt)
       news_results.append(news_object)
            
     return news_results

