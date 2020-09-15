from .api import Api
from config import BAO_MOI

class BaoMoi(Api):
    def __init__(self, url, recursive):
        super(BaoMoi, self).__init__(url, recursive)
        self.baseUrl = BAO_MOI

    def getAllLinks(self):
        return self.soup.find_all('a', {'class': 'cache', 'href': True})
    
    def getDateTime(self):
        try:
            el = self.soup.find('time', {'class': 'time'})
            datetime = el['datetime']
            return datetime
        except Exception as e:
            print('[WARNING] Get datetime:', e)
            return ''
        
    def getAuthor(self):
        try:
            author = self.soup.find('p', {'class': 'body-author'}).string
            return author
        except Exception as e:
            print('[WARNING] Get author:', e)
            return ''