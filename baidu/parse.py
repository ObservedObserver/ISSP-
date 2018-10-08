from bs4 import BeautifulSoup
def parseHtml(html):
  result = []
  # print(html)
  soup = BeautifulSoup(html)
  links = list(map(lambda record: record.contents[1].get('href'), soup.find_all('h3', class_='c-title')))
  titles = list(map(lambda record: ''.join(''.join([text for text in record.stripped_strings]).split()), soup.find_all('h3', class_='c-title')))
  times = list(map(lambda record: ''.join(record.contents[0].split()[1:]), soup.find_all('p', class_='c-author')))
  abstracts = list(map(lambda record: ''.join(''.join([text for text in record.stripped_strings]).split()), soup.find_all('div', class_='result')))
  # print(len(times), len(abstracts), titles, len(links))
  for i in range(len(titles)):
    result.append({
        'title': titles[i],
        'article_url': links[i],
        'abstract': abstracts[i],
        'publish_time': times[i]
      })
  return result
