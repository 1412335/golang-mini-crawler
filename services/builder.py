import re

from .api import Api
from .baomoi import BaoMoi
from .zingnews import ZingNews

from .utils import isValidUrl
from config import *

def Parser(url, recursive=2):
    parsedUrl, valid = isValidUrl(url, return_parser=True)
    if valid:
        netloc = parsedUrl.netloc.lower()
        if BAO_MOI.find(netloc) > -1:
            api = BaoMoi(url, recursive)
        elif ZING_NEWS.find(netloc) > -1:
            api = ZingNews(url, recursive)
        else:
            api = Api(url, recursive)
        return api

    raise ValueError('Invalid url')