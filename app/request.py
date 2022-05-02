
from app import app
from app.models import headlines

import urllib.request,json


from .models import headlines

# News=news.News
api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]

Headlines = headlines.Headlines  # variable name News of file news of class News



def get_headlines():
    """
    method to get headlines
    """
    get_headlines_url = base_url.format(api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)
        print(get_headlines_response)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_headlines(headlines_results_list)

    return headlines_results


def process_headlines(get_headlines_response):
    """
    method that processes response from the api call
    """
    headlines_results = []
    for headline_item in get_headlines_response:
        source = headline_item.get('source')
        author = headline_item.get('author')
        url = headline_item.get('url')
        urlToImage = headline_item.get('urlToImage')
        title = headline_item.get('title')
        description = headline_item.get('description')
        publishedAt = headline_item.get('publishedAt')

        if urlToImage and author and title:
            headline_object = Headlines(source, author, title, description, url, urlToImage, publishedAt)
            headlines_results.append(headline_object)

    return headlines_results
