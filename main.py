import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep
from random import uniform

def get_html(url):
    proxies = open('proxies.txt').read().split('\n')
    useragents = open('useragents.txt').read().split('\n')
    for i in range(3):
        proxy = {'https': 'https://' + choice(proxies)}
        useragent = {'User-Agent': choice(useragents)}
        print(proxy, useragent)
        try:
            r = requests.get(url, headers=useragent, proxies=proxy)
            print(200, 'work')
            sleep(uniform(1,3))
            return r.text
        except:
            print('dont work')
            continue

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a', class_='_3_q0k')
    for link in links:
        url = 'https://domclick.ru' + link.get('href')
        pr = link.find('div', class_='_2LpFR').text.strip()
        price = ''.join(pr.split(' ')[:-1])
        adress = link.find('p', class_='_20lRQ').text.strip()
        rooms = link.find_all('li', class_='_2aoTm')[0].text
        sq = link.find_all('li', class_='_2aoTm')[1].text
        square = sq.split(' ')[0]
        fl = link.find_all('li', class_='_2aoTm')[2].text
        floor = fl.split(' ')[0]
        max_floor = fl.split(' ')[-1]
        print(url, 'Количество комнат:', rooms,'Цена:', price, 'Адрес:', adress, 'Площадь:', square, 'Этаж:', floor, 'из', max_floor)

def main():
    url = 'https://domclick.ru/search?address=f2b23f98-35d8-4d18-a433-7a01e7820cf5&offset=0&limit=30&category=living&deal_type=sale&has_photo=1&offer_type=flat&rooms=1&sort_dir=desc'
    get_data(get_html(url))

if __name__ == '__main__':
    main()