import requests
from bs4 import BeautifulSoup

def make_requests():
    html="https://nambafood.kg/bonus"
    r = requests.get(html)
    return r.content


def get_data_4():
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', class_='catalog-content')
    title = divs.find_all('a', class_='cafe-item')
    sales_list = []
    title_list = []
    description_list = []
    photo_list_1 = open('logonambafood.jpeg', 'rb')
    photo_list_2 = open('food.jpеg', 'rb')
    for item in enumerate(title):
        annouth = item[1].find('div', class_='cafe--name').get_text(strip=True)
        description = item[1].find('div', class_='information--sales').text
        full_title = f"{str(item[0])}. " + annouth
        title_list.append(full_title)
        full_description = f"{str(item[0])}. " + description
        description_list.append(full_description)
    sales_list.append(title_list)
    sales_list.append(description_list)
    sales_list.append(photo_list_1)
    sales_list.append(photo_list_2)
    return sales_list
    # print(sales_list)

# get_data_4()