from bs4 import BeautifulSoup
import requests
from datetime import datetime
from fake_useragent import UserAgent
import re

ua = UserAgent()
headers = {'accept': '*/*', 'user-agent': ua.firefox}
news_url = 'https://sakhalin.info/'
get_news_url='https://sakhalin.info/'
rubriks_url=[]
rubriks_name=[]
city_names = []
city_urls = []




topics_title = []
topics_url = []
topic_desk = []

def get_html(url):
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		result = requests.get(url)
	return result.text


    
def get_topics(html):
    soup = BeautifulSoup(html, 'lxml')
    for a in soup.find_all('div', class_="dropdown-menu dropdown-menu_disable-on-mobile header__menu-button"):
        # i = a.find('a').get('href')
        n = a.find_all('span', class_='header__menu-link')
        #print(n)
        for j in n:
           if j.text.strip() == 'Рубрики':
              i = a.find_all('ul',class_='dropdown-menu__list')
              for b in i:
                  k = b.find_all('li',class_='dropdown-menu__item dropdown-menu__item_thin')
                  for d in k:
                    rubriks_url.append(d.find('a').get('href'))
                    rubriks_name.append(d.text)
           elif j.text.strip() == 'Города':
              i = a.find_all('ul',class_='dropdown-menu__list')
              for b in i:
                  k = b.find_all('li',class_='dropdown-menu__item dropdown-menu__item_thin')
                  for d in k:
                    city_urls.append(d.find('a').get('href'))
                    city_names.append(d.text)




get_topics(get_html(news_url))

def get_urls_from_topic(i):
	try:
		index = rubriks_name.index(i)
		return rubriks_url[index]
	except:
		index = city_names.index(i)
		return city_urls[index]


trash_symbols = '[\xa0\n\t\t\t]' 

def get_news_from_topics(url):
  global topics_title, topics_url
  soup = BeautifulSoup(get_html(url), 'lxml')
  topics_title.clear()
  topics_url.clear()
  for a in soup.find_all('a',class_='story-title-link'):
      
      title = a.text
     
        #print(topics_title)
      final_title = re.sub(trash_symbols, ' ',title)
      topics_title.append(final_title.strip())
      topics_url.append(a.get('href'))


def get_topic_descript_sakh(url):
  soup = BeautifulSoup(get_html(url), 'lxml')
  for a in soup.find_all('p',class_='text-style-text'):
      desc = a.text
      final_desc = re.sub(trash_symbols, ' ', desc)
      topic_desk.append(final_desc.strip())



# get_news_from_topics(get_urls_from_topic('Политика'))
# get_topic_descript_sakh(topics_url[1])

# print(topic_desk)
#Debug
# i = input('Какие новости? ')

#get_news_from_topics(get_urls_from_topic('ЖКХ'))
#print(f"Headder - {topics_title[0]} \nURL- {topics_url[0]}")
#get_news_from_topics(get_urls_from_topic('Бизнес'))
#print(f"Headder - {topics_title[0]} \nURL- {topics_url[0]}")
#print(topics_title)

# for o in topics_title:
#   print(topics_title[topics_title.index(o)])
