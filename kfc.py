import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

def make_requests():
    html="https://kfc.kg/promo"
    r = requests.get(html)
    return r.content


def get_data_2():
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', class_='main-content-inr group')
    title = divs.find_all('div', class_='content-list-main')
    sales_list = []
    title_list = []
    description_list = []
    photo_list_1 = open('logokfc.jpeg', 'rb')
    photo_list_2 = open('kfc.jpeg', 'rb')
    for item in enumerate(title, 1):
        annouth = item[1].find('h2', class_='title').text
        description = item[1].find('p',).text
        title_list.append(str(item[0]))
        title_list.append(annouth)
        description_list.append(str(item[0]))
        description_list.append(description)
    sales_list.append(title_list)
    sales_list.append(description_list)
    sales_list.append(photo_list_1)
    sales_list.append(photo_list_2)
    return sales_list
