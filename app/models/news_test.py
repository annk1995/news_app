import unittest
from models import news
News=news.news

class newsTest(unittest.TestCase):
    def setUp(self):
        self.new_news=News(1234,'headlines','https://newsapi.org/v2/top-headlines?country=de&category=business&apiKey=7e46dfc39abd4a32a42ce973de9159e0') 
        def test_instance(self):
         self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()