import json, re, csv
with open('../../dataset/relation/ratings_time_lag_less100_wei_list_fix.json', 'r') as f:
  event_data = json.loads(f.read())
  with open('../../dataset/manualProcess/beijing_inc_wei.csv', 'r', encoding='utf-8-sig') as c:
    csv_data = list(map(lambda record: dict(record), list(csv.DictReader(c))))
    for record in event_data:
      record['category'] = list(filter(lambda x: x['证券简称'] == record['company_name'], csv_data))[0]['分类']
    with open('../../dataset/manualProcess/clean_rating_category.json', 'w') as w:
      w.write(json.dumps(event_data))
    
  # data = json.loads(f.read())
  # filterData = []
  # count = 0
  # for record in data:
    
  # print(count, filterData)
  # with open('../dataset/bj_safe_baiduall.json', 'w+') as w:
  #   w.write(json.dumps(filterData))