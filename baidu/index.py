import csv, time, json
from parse import parseHtml
from request import getHtml, getBaiduURL
from utils import dataFilter

# url = getBaiduURL('中石油网络攻击')
# res = getHtml(url)
# ans = parseHtml(res) 

# print(ans)

def main():
  print('test')
  with open('../dataset/beijing_inc.csv') as f:
    result = []
    dataSource = csv.DictReader(f)
    totalRows = 304#len(f.readlines())
    i = 0
    for row in dataSource:
      i += 1
      try:
        print(row['证券简称'], str(i * 100 / totalRows) + '%')
        url = getBaiduURL(row['证券简称'] + '网络攻击')
        res = getHtml(url)
        fullData = parseHtml(res)
        filterData = dataFilter(row['证券简称'], ['网络攻击', '病毒', 'DDos', '勒索'], fullData) 
        result[0:0] = filterData
      except:
        continue
      time.sleep(1)
      
    with open('../dataset/bj_safe_baidu.json', 'w+') as w:
      w.write(json.dumps(result))

if __name__ == '__main__':
  main()