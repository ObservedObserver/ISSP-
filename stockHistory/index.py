import csv, json
from parse import parseHtml
from request import getHtml, getStockURL

# url = getStockURL('600028')
# res = getHtml(url) 
# ans = parseHtml(res) 
import copy
def main():
  with open('../dataset/target_inc.json') as f0:
    targetInc = json.loads(f0.read())
    with open('../dataset/beijing_inc.csv') as f:
      result = []
      dataSource = csv.DictReader(f)
      # headers = []
      fieldnames = []
      i = 0
      for row in dataSource:
        if row['证券简称'] in targetInc:
          try:
            print(str(i) + ':' + row['证券简称'])
            url = getStockURL(row['证券代码'].split('.')[0])
            res = getHtml(url)
            csvData = parseHtml(res)
            # fieldnames = csvData[0]
            for record in csvData[1:]:
              record.append(row['证券简称'])
            if i == 0:
              # csvData[0].append('incName')
              fieldnames = copy.deepcopy(csvData[0])
              fieldnames.append('company_name')
            result[0:0] = csvData[1:]
          except:
            print('err')
            continue
          i += 1
        else:
          print(row['证券简称'] + ' not found')
      with open('../dataset/stock.csv', 'w+') as csvfile:
        csvfile.write(','.join(fieldnames) + '\n')
        for row in result:
          csvfile.write(','.join(row) + '\n')

if __name__ == '__main__':
  main()