import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

def make_requests():
    html="https://sushiwok.kg/bishkek/akcii/"
    r = requests.get(html)
    return r.content


def get_data():
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', class_='page-container page-stocks')
    title = divs.find_all('div', class_='stock-wrapper')
    sales_list = []
    for item in title:
        annouth = item.find('span', class_='stock-title').text
        description = item.find('div', class_='descr-container').text
        sales_list.append({
            "title":annouth,
            "description": description,
        })
        print(annouth) 
        print(description)
    print(sales_list)
get_data()
    # return sales_list
