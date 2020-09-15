import re
import os
import urllib.request
from bs4 import BeautifulSoup
import gzip
import pandas as pd

from config import OUTPATH, BASE_PATH

try:
    from urlparse import urlparse
except :
    from urllib.parse import urlparse

def isValidUrl(url, min_token=('scheme', 'netloc', 'path'), return_parser=False):
    try:
        result = urlparse(url)
        if return_parser:
            return result, all([getattr(result, token) for token in min_token])
        return all([getattr(result, token) for token in min_token])
    except ValueError as e:
        if return_parser: 
            return None, False
        return False

def getSoup(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
        }
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)

        contentEncoding = resp.info().get('Content-Encoding')
        if contentEncoding == 'gzip':
            html = gzip.decompress(resp.read())
        elif contentEncoding == 'deflate':
            html = resp.read()
        else:
            html = resp.read()

        return BeautifulSoup(html, 'html.parser')
    except Exception as e:
        print('[WARNING] Get soup:', e)
        return None
    
def saveCSVFile(data, path='.'):

    if re.match('.*\.csv$', path) is None:
        if path[-1:] == '/':
            path += OUTPATH
        else:
            path += '.csv'

    dir, filename = os.path.split(os.path.join(BASE_PATH, path))

    if not os.path.isdir(dir):
        try:
            os.makedirs(dir, mode=0o777)
        except Exception as e:
            print(e)
            dir = '.'

    outPath = os.path.join(dir, filename)
    pd.DataFrame(data).to_csv(outPath)
    return outPath