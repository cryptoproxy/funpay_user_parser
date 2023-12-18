import time
import requests
from bs4 import BeautifulSoup
import json

'''
это мой очень старый код
'''

url = input('Enter seller profile: ')


def parse(link_profile):
    response = requests.get(link_profile)
    soup = BeautifulSoup(response.content, 'lxml')
    username = soup.find('span', class_='mr4').text.strip()

    offers = soup.find('div', class_='mb20').find_all('div', class_='offer')
    datas = []
    with open(fr'{username}.json', 'w', encoding='utf-8') as f:
        for offer in offers:
            game_lots: list = offer.find_all('a', class_='tc-item')
            try:
                for lot in game_lots:
                    link = lot['href']
                    desc = lot.find('div', 'tc-desc-text').text
                    price = lot.find('div', class_='tc-price').find('div').text.strip()
                    data = {
                        'desc': desc,
                        'price': price,
                        'link': link,
                    }
                    datas.append(data)
            except AttributeError:
                print(f'AttributeError: {link}')
        json.dump(datas, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    parse(url)
