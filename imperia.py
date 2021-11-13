import requests
from bs4 import BeautifulSoup

def make_requests():
    html="https://mypizza.kg/Shares"
    r = requests.get(html)
    return r.content


def get_data2():
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('main', class_='c-main')
    title = divs.find_all('div', class_='c-article__item')
    sales_list = []
    title_list = []
    description_list = []
    photo = open('logoimpiria.jpeg', 'rb')
    for item in enumerate(title, 1):
        annouth = item[1].find('div', class_='c-article__title').text
        description = item[1].find('div', class_='c-article__text').text
        full_title = f"{str(item[0])}. "+annouth
        title_list.append(full_title)
        full_description = f"{str(item[0])}. " + description
        description_list.append(full_description)
    sales_list.append(title_list)
    sales_list.append(description_list)
    sales_list.append(photo)
    return sales_list
