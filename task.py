import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'Python']

response = requests.get('https://habr.com/ru/all')
if not response.ok:
    raise RuntimeError('сайт не доступен')

list_reference = []

text = response.text

soup = BeautifulSoup(text, features = 'html.parser')
articles = soup.find_all('article', class_="tm-articles-list__item")

for article in articles:

    for word in KEYWORDS:

        article_text = article.find('div', class_="article-formatted-body").text.lower()

        if article_text.find(word.lower()) > -1:
            a_head = article.find('a', class_="tm-article-snippet__title-link").text
            a_time = article.find('time').text
            a_link = article.find('a', class_="tm-article-snippet__title-link").get('href')
            list_reference.append((a_time, a_head, a_link))

unique_list = set(list_reference)
print(list(unique_list))
