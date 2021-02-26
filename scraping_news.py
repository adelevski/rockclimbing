from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.planetmountain.com/en/news?genere=1&page='

def pull_articles(numpages=1, term='9b'):
    articles = []
    thumbs = []
    links = []
    for page in range(1, numpages):
        source = requests.get(URL + str(page)).text
        soup = bs(source, 'lxml')
        posts = soup.find_all("div", class_='post clearfix')
        for post in posts:            
            if term in str(post.h2.text):
                articles.append(str(post.h2.text) + f' (p. {page})')
                thumbs.append('https://www.planetmountain.com' + post.find('img').get('src'))
                links.append('https://www.planetmountain.com' + post.find('a').get('href'))
    return articles, thumbs, links
    




