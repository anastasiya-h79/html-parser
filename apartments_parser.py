import requests
from bs4 import BeautifulSoup
from time import sleep


url = 'https://prian.ru/spain/canary-islands/tenerife/apartments/'
#url = f'{DOMAIN}/apartments/'
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
    apart_list = soup.find('div', class_='list').find_all('dl')       #find_all_next('dd')             #find_all_next('list_object list_inline list_object_xs')
    for item in apart_list:
        apartment_title = soup.find('dd', class_='list_object__foot__title').text
        apartment_price = soup.find('dd', class_='list_object__foot__price').text
        apartment = soup.find('dd', class_='list_object__foot__subtext list__inline-only').text
        #apartment_url = soup.find_all('div', class_='list_object list_inline list_object_xs').a.get('href')
        apartments_data = {
            'апартаменты': apartment_title,
            'цена': apartment_price,
            'краткое описание': apartment

        }
    print(f'{apartment_title}: {apartment_price}\n{apartment}')
    #print(apartments_data)
        # print(len(apartments_data))


