from urllib import request, parse
import json
def getHtml (url):
  req = request.Request(url)
  print(url)
  req.add_header('user-agent', 'Chrome/69.0')
  res = request.urlopen(req)
  return res.read().decode('utf-8')

def getTouTiaoURL (keyword):
  parseKeyword = parse.quote(keyword)
  return 'https://www.toutiao.com/search/?keyword=' + parseKeyword

def getToutiaoAPI (content):
  keyword = parse.quote(content)
  api = 'https://www.toutiao.com/search_content/?offset=0&format=json&keyword=' + keyword + '&autoload=true&count=20&cur_tab=1&from=search_tab'
  req = request.Request(api)
  res = request.urlopen(req)
  # print(res.reason())
  return res.read().decode('utf-8')