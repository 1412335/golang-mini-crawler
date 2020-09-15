from .api import Api
from config import ZING_NEWS

class ZingNews(Api):
    def __init__(self, url, recursive):
        super(ZingNews, self).__init__(url, recursive)
        self.baseUrl = ZING_NEWS

    def getAllLinks(self):
        return self.soup.select('.article-item .article-title a')

    def getDateTime(self):
        try:
            return self.soup.find('li', {'class': 'the-article-publish'}).string
        except Exception as e:
            print('[WARNING] Get datetime:', e)
            return ''
        
    def getAuthor(self):
        try:
            author = self.soup.find('p', {'class': 'author'}).string
            return author
        except Exception as e:
            print('[WARNING] Get author:', e)
            return ''