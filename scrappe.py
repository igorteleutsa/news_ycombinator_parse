import requests
from bs4 import BeautifulSoup

def create_custom_hn(links,votes):
    news_list =[]
    for index,item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href',None)
        points = votes[index].getText()
        print(points)
        news_list.append({'title':title,'link': href})

    return news_list


url = 'https://news.ycombinator.com/news'
request = requests.get(url)
soup = BeautifulSoup(request.text,'html.parser')

links = soup.select('.storylink')
votes = soup.select('.score')
create_custom_hn(links,votes)