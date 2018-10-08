from urllib import request, parse
import json
def getHtml (url):
  req = request.Request(url)
  # print(url)
  req.add_header('user-agent', 'Chrome/69.0')
  res = request.urlopen(req)
  return res.read().decode('utf-8')

def getBaiduURL (keyword):
  parseKeyword = parse.quote(keyword)
  # return 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=' + parseKeyword
  return 'https://www.baidu.com/s?ie=utf-8&cl=2&rtt=1&bsst=1&tn=news&word=' + parseKeyword + '&rsv_sug3=23&rsv_sug4=735&rsv_sug1=6&rsv_sug2=0&inputT=4997'
