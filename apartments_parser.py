import requests
from bs4 import BeautifulSoup
from time import sleep
import json

DOMAIN = 'https://prian.ru/spain/canary-islands/tenerife'
url = f'{DOMAIN}/apartments/'
html_doc = requests.get(url).text

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup)


for i in range(1, 288, 24):
    sleep(1)
    next_page_url = f'{url}?next={i + 23}'
    print(f'current page url: {next_page_url}\n')
    html_doc = requests.get(next_page_url).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    apartments_data = {}
    apart_list = soup.find('div', class_='list').find_all('dl')
    for item in apart_list:
        apartment_title = item.find('dd', class_='list_object__foot__title').text
        apartment_price = item.find('dd', class_='list_object__foot__price').text
        apartment = item.find('dd', class_='list_object__foot__subtext list__inline-only').text
        #apartment_url = item.find('div', class_='list_object list_inline list_object_xs').a.get('href')

        apartments_data = {
            'апартаменты': apartment_title,
            'цена': apartment_price,
            'краткое описание': apartment,
            #'ссылка на объект': apartment_url

        }
        print(f'{apartment_title}: {apartment_price}\n{apartment}')


#with open('apartment_data.json', 'w', encoding='utf-8') as f:
    #f.write(json.dumps(apartments_data))


