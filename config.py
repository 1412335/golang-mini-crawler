import os

# base path
BASE_PATH = os.path.dirname(os.path.realpath(__file__))

# level recursion
RECURSIVE=2

# output csv path 
OUTPATH='./crawl/data.csv'

# base url
BAO_MOI='https://baomoi.com'
ZING_NEWS='https://zingnews.vn'

# demo
URLS = [
    'https://baomoi.com/vu-an-dong-tam-toa-tuyen-2-an-tu-hinh-1-an-tu-chung-than/c/36371911.epi',
    'https://zingnews.vn/chinh-phu-quyet-mo-lai-6-duong-bay-quoc-te-post1131565.html',
]