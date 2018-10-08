import json, re, time
def toutiaoParser(incName, keywords, rawData):
  data = json.loads(rawData)['data']
  cleanData = []
  for record in data:
    keep = False
    for keyword in keywords:
      try:
        if re.search(keyword, record['title']):
          keep = True
        if re.search(keyword, record['abstract']):
          keep = True
      except:
        pass
      try:
        if re.search(incName, record['title']) == None and re.search(incName, record['abstract']) == None:
          keep = False
      except:
        pass
    if keep:
      cleanData.append({
        'title': record['title'],
        'article_url': record['article_url'],
        'abstract': record['abstract'],
        'publish_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(record['publish_time'])))
      })
  print(cleanData)
  return cleanData
