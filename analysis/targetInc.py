import json

with open('../dataset/bj_safe_baiduall.json') as f:
  data = json.loads(f.read())
  s = set()
  for record in data:
    # print(record)
    s.add(record['company_name'])
  with open('../dataset/target_inc.json', 'w+') as w:
    w.write(json.dumps(list(s)))