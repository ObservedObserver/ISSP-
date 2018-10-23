from bs4 import BeautifulSoup

def parseHtml(html):
  soup = BeautifulSoup(html, 'lxml')
  dataTable = soup.find_all('table', class_='data')[1].contents
  transData = list(map(lambda record: [text.replace(',', '') for text in record.stripped_strings], dataTable))[:-1]
  return transData