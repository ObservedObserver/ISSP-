import csv, json
def loadCompanies():
  sqlList = []
  with open('../dataset/manualProcess/beijing_inc_wei.csv', 'r', encoding='utf-8-sig') as f:
    data = csv.DictReader(f)
    # 分类,序号,证券代码,证券简称,公司中文名称,注册地址,办公地址,邮编,公司电话,公司网站
    for record in data:
      sql = """INSERT INTO Companies (
        companyID,
        category,
        companyCode,
        companyName,
        companyFullName,
        companyLocReg,
        companyLocReal,
        zipCode,
        companyPhone,
        companyWebsite) VALUES (
          %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'
        );
      """ % (
        int(record['序号']),
        record['分类'],
        record['证券代码'],
        record['证券简称'],
        record['公司中文名称'],
        record['注册地址'],
        record['办公地址'],
        record['邮编'],
        record['公司电话'],
        record['公司网站']
      )
      sqlList.append(sql)
  with open('./data/companies.sql', 'w') as f:
    f.write('\n'.join(sqlList))

def loadStock():
  sqlList = []
  with open('../dataset/stock.csv', 'r') as f:
    data = csv.DictReader(f)
    # 日期,开盘,最高,最低,收盘,成交量,成交金额,升跌$,升跌%,company_name
    for record in data:
      # print(record)
      date = record['日期'].split('/')
      newDate = [date[2], date[0], date[1]]
      sql = """INSERT INTO stockMarket (
        companyName,
        time,
        startPrice,
        maxPrice,
        minPrice,
        endPrice,
        amount,
        cash,
        changeInCash,
        changeInPercent) VALUES (
          '%s', '%s', %f, %f, %f, %f, %f, %f, %f, %f
        );
      """ % (
        record['company_name'],
        '/'.join(newDate),
        float(record['开盘'].replace('/', '')),
        float(record['最高'].replace('/', '')),
        float(record['最低'].replace('/', '')),
        float(record['收盘'].replace('/', '')),
        float(record['成交量'].replace('/', '')),
        float(record['成交金额'].replace('/', '')),
        float(record['升跌$'].replace('/', '0')),
        float(record['升跌%'].replace('/', '0').replace('%', ''))
      )
      sqlList.append(sql)
  with open('./data/stockMarket.sql', 'w') as f:
    f.write('\n'.join(sqlList))


def loadEvents():
  sqlList = []
  with open('../dataset/manualProcess/clean_data.json', 'r') as f:
    data = json.load(f)
    for record in data:
      sql = """INSERT INTO safetyEvents (
        title,
        time,
        companyName,
        articleURL,
        abstract) VALUES (
          '%s', '%s', '%s', '%s', '%s'
        );
      """ % (
        record['title'],
        record['time'],
        record['company_name'],
        record['article_url'],
        record['abstract']
      )
      sqlList.append(sql)
  with open('./data/safetyEvents.sql', 'w') as f:
    f.write('\n'.join(sqlList))


loadCompanies()
loadStock()
loadEvents()


