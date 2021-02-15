import requests
import pprint
from bs4 import BeautifulSoup


def create_custom_hn(links, subtext):
    news_list = []
    for index, item in enumerate(links):
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().strip(' points'))
            if points > 99:
                title = links[index].getText()
                href = links[index].get('href', None)
                news_list.append({'title': title, 'link': href, 'score': points})

    return sorted(news_list, key=lambda i: i['score'], reverse=True)


def get_link(pages=1):
    return f'https://news.ycombinator.com/news?p={pages}'


def slicing_url(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    return links, subtext


if __name__ == '__main__':
    url = get_link(2)
    links, subtext = slicing_url(url)
    pprint.pprint(create_custom_hn(links, subtext))
