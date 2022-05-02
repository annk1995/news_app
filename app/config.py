from instance.config import NEWS_API_KEY


class Config:
  NEWS_API_KEY="7e46dfc39abd4a32a42ce973de9159e0"
  MOVIE_API_BASE_URL ='https://newsapi.org/v2/everything?q=Apple&from=2022-05-02&sortBy=popularity&apiKey='+NEWS_API_KEY
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True