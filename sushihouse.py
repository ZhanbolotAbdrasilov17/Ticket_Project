import requests
from bs4 import BeautifulSoup

from nambafood import get_data_4


# def get_html(url):
#     response = requests.get(url)
#     return response.text

def make_requests():
    html="http://sushihouse.kg/"
    r = requests.get(html)
    return r.content


def get_data5():
    sales_list = []
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', {"id":"комбо"})
    items = divs.find('div', class_ = 's-elements-grid').find_all('div', 's-elements-grid__cell')
    title_list = []
    description_list = []
    photo_list_1 = open('logosushihause.jpeg', 'rb')
    photo_list_2 = open('sushihause.jpeg', 'rb')
    for item in enumerate(items, 1):
        all_info = item[1].find_all('div', class_ = 'widget-text')
        title_list.append(f"{str(item[0])}. {str(all_info[0].text)}")
        description_list.append(f"{str(item[0])}. {str(all_info[1].text)} ({str(all_info[2].text)})")
    sales_list.append(title_list)
    sales_list.append(description_list)
    sales_list.append(photo_list_1)
    sales_list.append(photo_list_2)
    return sales_list