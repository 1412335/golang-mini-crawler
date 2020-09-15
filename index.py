import argparse

from services.builder import Parser
from services.utils import saveCSVFile
from config import OUTPATH, RECURSIVE, URLS

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--link', help='Url link to news', required=True, type=str)
    parser.add_argument('-o', '--out', help='Output path', required=False, type=str, default=OUTPATH)
    parser.add_argument('-r', '--recursive', help='Level recursive', required=False, type=int, default=RECURSIVE)
    args = parser.parse_args()
    return args

def main():
    args = getArgs()

    try:
        print('[INFO] Starting crawl data with url:', args.link)
        print('='*100)
    
        parser = Parser(args.link, args.recursive)
        data = parser.parseData()
    except ValueError as e:
        print('[ERROR]', e)
        return False
    except Exception as e:
        print('[ERROR] Exception:', e)
        return False

    print('='*100)

    outPath = saveCSVFile(data, path=args.out)
    print('[INFO] Write data into csv file at', outPath)

    return True

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)