import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

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
    
    for item in enumerate(title):
        annouth = item[1].find('div', class_='cafe-item--wrap').get_text(strip=True)
        title_list.append(str(item[0]))
        title_list.append(annouth)

    sales_list.append(title_list)

    return sales_list
