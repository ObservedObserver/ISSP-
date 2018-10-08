import re, json, time
import csv
from bs4 import BeautifulSoup

from request import getHtml, getTouTiaoURL, getToutiaoAPI
from parse import toutiaoParser

def main():
  with open('../dataset/beijing_inc.csv') as f:
    result = []
    dataSource = csv.DictReader(f)
    for row in dataSource:
      try:
        print(row['证券简称'])
        data = getToutiaoAPI(row['证券简称'] + '网络攻击')
        result[0:0] = toutiaoParser(row['证券简称'], ['攻击', '病毒'], data) 
        time.sleep(2)
      except:
        continue
      
    with open('../dataset/bj_safe.json') as w:
      w.write(json.dumps(result))

if __name__ == '__main__':
  main()