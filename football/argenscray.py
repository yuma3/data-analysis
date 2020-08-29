import requests
from bs4 import BeautifulSoup


# print(name.get_text())


def get_argen_news():
    url = 'https://mundoalbiceleste.com/'

    html = requests.get(url)

    soup = BeautifulSoup(html.text, 'html.parser')

    items = soup.find_all('h3', attrs={'class', 'entry-title'})
    news_list = []
    for item in items:
        headlines = item.find('a').text
        print(headlines)
        news_list.append(headlines)

    # print(news_list)
    return news_list

def get_argen_player():

    url = 'https://mundoalbiceleste.com/argentina-national-team-players/'

    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    names = soup.find_all('td', attrs={'class', 'name'})
    name_list = []
    for name in names:
        name = name.text
        name = name.strip('\n')
        name_list.append(name)

    print(name_list)
    return name_list





if __name__ == '__main__':
    get_argen_news()
    get_argen_player()
