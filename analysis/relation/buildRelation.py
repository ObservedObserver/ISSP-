import json, csv, math
import datetime
def loadData():
  # bj_safe_baiduall.json 信息安全时间统计
  # stock.csv 股票数据
  # 关联字段：company_name（公司简称）
  company_event = {}
  company_stock = {}
  with open('../../dataset/manualProcess/clean_data_wei.json', 'r') as f:
    data = json.loads(f.read())
    for record in data:
      if company_event.get(record['company_name']) == None:
        company_event[record['company_name']] = []
      [year, month, day] = record['time'].split('-')
      # record['time'] = datetime.datetime(year, month, day)
      record['time'] = [int(year), int(month), int(day)]
      company_event[record['company_name']].append(record)
  with open('../../dataset/stock.csv', 'r') as f:
    data = csv.DictReader(f)
    for record in data:
      if company_stock.get(record['company_name']) == None:
        company_stock[record['company_name']] = []
      new_record = dict(record)
      [month, day, year] = new_record['日期'].split('/')
      new_record['time'] = [int(year), int(month), int(day)]
      company_stock[record['company_name']].append(new_record)
  return {
    'company_event': company_event,
    'company_stock': company_stock
  }
def cosXY(x, y):
  xy = 0
  x2 = 0
  y2 = 0
  for i in range(len(x)):
    xy += x[i] * y[i]
  for i in range(len(x)):
    x2 += x[i] ** 2
    y2 += y[i] ** 2
  try:
    ans = xy / (math.sqrt(x2) * math.sqrt(y2))
  except:
    ans = 'null'
  return ans

def getRelevancy(company_data):
  companies = company_data['company_event'].keys()
  company_stock = company_data['company_stock']
  company_event = company_data['company_event']
  rate_list = []
  for company in companies:
    # print(company_stock[company])
    year_range = [min(list(map(lambda x: x['time'][0], company_stock[company]))), max(list(map(lambda x: x['time'][0], company_stock[company])))]
    month_range = [min(list(map(lambda x: x['time'][1], company_stock[company]))), max(list(map(lambda x: x['time'][1], company_stock[company])))]
    day_range = [min(list(map(lambda x: x['time'][2], company_stock[company]))), max(list(map(lambda x: x['time'][2], company_stock[company])))]
    vec_stock = []
    vec_event = []
    # print(company)
    # print(year_range, month_range, day_range)
    for y in range(year_range[0], year_range[1] + 1):
      for m in range(month_range[0], month_range[1] + 1):
        for d in range(day_range[0], day_range[1] + 1):
          result = list(filter(lambda x: x['time'] == [y, m, d], company_stock[company]))
          if len(result) > 0:
            try:
              vec_stock.append(float(result[0]['升跌$']))
            except:
              vec_stock.append(0)
          else: 
            vec_stock.append(0)
          result = list(filter(lambda x: x['time'] == [y, m, d], company_event[company]))
          if len(result) > 0:
            vec_event.append(len(result))
          else: 
            vec_event.append(0)
    rate = cosXY(vec_event, vec_stock)
    print(company, rate)
    rate_list.append({
      'company_name': company,
      'rate': rate
    })
  return rate_list

if __name__ == '__main__':
  company_data = loadData()
  with open('../../dataset/relation/stock&event.json', 'w') as f:
    f.write(json.dumps(company_data))
  # rate_list = getRelevancy(company_data)
  # with open('../../dataset/ratings.json', 'w') as f:
  #   f.write(json.dumps(rate_list))
