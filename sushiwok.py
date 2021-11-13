import requests
from bs4 import BeautifulSoup

def make_requests():
    html="https://sushiwok.kg/bishkek/akcii/"
    r = requests.get(html)
    return r.content

def get_data5():
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', class_='page-container page-stocks')
    title = divs.find_all('div', class_='stock-wrapper')
    sales_list = []
    title_list = []
    description_list = []
    photo = open('logosushiwok.jpeg', 'rb')
    for item in enumerate(title, 1):
        annouth = item[1].find('span', class_='stock-title').text
        description = item[1].find('div', class_='descr-container').text
        full_title = f"{str(item[0])}. " + annouth
        title_list.append(full_title)
        full_description = f"{str(item[0])}. " + description
        description_list.append(full_description)
    sales_list.append(title_list)
    sales_list.append(description_list)
    sales_list.append(photo)
    return sales_list
