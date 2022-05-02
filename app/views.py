from flask import render_template
from app import app
# from .request import get_news
from .request import get_headlines
# Views

@app.route('/')
def index():
 news_headlines =get_headlines()
 return render_template('index.html',news=news_headlines)
    
    
