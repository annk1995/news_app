from flask import render_template
from app import app
from .request import get_news
# Views

@app.route('/')
def index():
 news_headlines =get_news()
 return render_template('index.html',news=news_headlines)
    
    
@app.route('/news/<int:news_id>')
def news(news_id):

  
    return render_template('news.html',id = news_id)
