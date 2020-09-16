import re
import urllib.parse
from dateutil.parser import parse
from .utils import getSoup, isValidUrl

class Api(object):
    def __init__(self, url, recursive):
        self.url = url
        self.baseUrl = ''
        self.recursive = recursive

    def getTitle(self):
        return self.soup.title.string

    def getMetadata(self):
        metas = dict()
        for meta in self.soup.find_all('meta'):
            try:
                content = meta['content']
                name = meta['name']
                metas[name] = content
            except Exception as e:
                continue
        return metas

    def getDateTime(self):
        return ''

    def getAuthor(self):
        return ''

    # get all possible links in self.url
    def getAllLinks(self):
        return []

    # get others interesting urls in self.url
    def getDataLinks(self):
        all = self.getAllLinks()
        if all is None:
            return set()
        links = set()
        for a in all:
            try:
                href = a['href']
                if re.match('^(http(s)?:)?\/\/.*', href) is not None:
                    parsedUrl, valid = isValidUrl(href, return_parser=True)
                    if not valid or self.baseUrl.find(parsedUrl.netloc.lower()) == -1:
                        continue
                else:
                    href = urllib.parse.urljoin(self.baseUrl, href)
                links.add(href)
            except Exception as e:
                print('[WARNING] Get links:', e)
                continue
        return links

    def parseData(self):
        if self.recursive <= 0:
            return []

        print('[INFO] Parse data url:', self.url)
        self.soup = getSoup(self.url)
        if self.soup is None:
            return []

        title = self.getTitle()
        metas = self.getMetadata()
        time = self.getDateTime()
        author = self.getAuthor()

        if time:
            time = parse(time).strftime('%Y-%m-%d %H:%M:%S')

        data = []
        data.append({
            "URL": self.url,
            "Title": title,
            "Author": author,
            "Date": time,
            "Metas": metas,
        })

        links = self.getDataLinks()

        self.recursive -= 1
        for link in links:
            self.url = link
            subdata = self.parseData()
            data.extend(subdata)

        self.recursive += 1
        return data