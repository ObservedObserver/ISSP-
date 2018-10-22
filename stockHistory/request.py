from urllib import request, parse
import json
def getHtml (url):
  print('request' + url)
  req = request.Request(url)
  # print(url)
  req.add_header('user-agent', 'Chrome/69.0')
  res = request.urlopen(req)
  print('request finished', res.status)
  return res.read().decode('utf-8')

def getStockURL (stockNum):
  return  'http://www.aigaogao.com/tools/history.html?s=' + stockNum
