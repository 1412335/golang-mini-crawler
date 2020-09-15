# golang-mini-crawler

```bash
cd golang-mini-crawler

pip3 install -r requirements.txt

python3 index.py [-h] -l LINK [-o OUT] [-r RECURSIVE]
# required arguments:
#   -l LINK, --link LINK  Url link to news
# optional arguments:
#   -h, --help            show this help message and exit
#   -o OUT, --out OUT     Output path
#   -r RECURSIVE, --recursive RECURSIVE Level recursive (default: 2)

# Example:
# zingnews
python3 index.py -l https://zingnews.vn/ap-thap-nhiet-doi-tien-vao-bien-dong-post1131607.html -o ./crawl/zingnews
# baomoi
python3 index.py -l https://baomoi.com/noi-lai-mot-so-chuyen-bay-thuong-mai-quoc-te-tu-15-9/c/36385489.epi -o ./crawl/baomoi.
csv
# other
python3 index.py -l https://vnexpress.net/hai-phuong-an-nghi-tet-tan-suu-4162207.html
```