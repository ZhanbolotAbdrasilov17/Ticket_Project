import requests
from bs4 import BeautifulSoup



def make_requests():
    html="https://mypizza.kg/Shares"
    r = requests.get(html)
    return r.content


def get_data1():
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('main', class_='c-main')
    title = divs.find_all('div', class_='c-article__item')
    sales_list = []
    title_list = []
    description_list = []
    photo_list_1 = open('logoimpiria.jpeg', 'rb')
    photo_list_2 = open('best.jpеg', 'rb')
    for item in enumerate(title, 1):
        annouth = item[1].find('div', class_='c-article__title').text
        description = item[1].find('div', class_='c-article__text').text
        title_list.append(str(item[0]))
        title_list.append(annouth)
        description_list.append(str(item[0]))
        description_list.append(description)
    sales_list.append(title_list)
    sales_list.append(description_list)
    sales_list.append(photo_list_1)
    sales_list.append(photo_list_2)
    return sales_list