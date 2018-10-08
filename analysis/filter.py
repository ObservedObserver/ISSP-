import json, re
with open('../dataset/bj_safe_baidu.json') as f:
  data = json.loads(f.read())
  filterData = []
  count = 0
  for record in data:
    try:
      t = int(record['publish_time'].split('年')[0])
      if t >= 2017 and t <= 2018:
        record['time'] = '-'.join(re.findall('[0-9]+', record['publish_time'])[:3])
        filterData.append(record)
        count += 1
    except:
      count += 1
      record['time'] = '2018-10-8'
      filterData.append(record)
  print(count, filterData)
  with open('../dataset/bj_safe_baidu2017.json', 'w+') as w:
    w.write(json.dumps(filterData))