from .api import Api
from config import ZING_NEWS

class ZingNews(Api):
    def __init__(self, url, recursive):
        super(ZingNews, self).__init__(url, recursive)
        self.baseUrl = ZING_NEWS

    def isVideo(self):
        return self.url.find(self.baseUrl + '/video') == 0

    def getAllLinks(self):
        return self.soup.select('.article-item .article-title a')

    def getDateTime(self):
        try:
            if self.isVideo():
                return self.soup.find('span', {'class': 'publish'}).string
            return self.soup.find('li', {'class': 'the-article-publish'}).string
        except Exception as e:
            print('[WARNING] Get datetime:', e)
            return ''
        
    def getAuthor(self):
        try:
            if self.isVideo():
                return self.soup.find('span', {'class': 'video-author'}).string
            return self.soup.find('p', {'class': 'author'}).string
        except Exception as e:
            print('[WARNING] Get author:', e)
            return ''