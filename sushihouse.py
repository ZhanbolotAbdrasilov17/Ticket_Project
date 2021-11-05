import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

def make_requests():
    html="http://sushihouse.kg/"
    r = requests.get(html)
    return r.content


def get_data():
    data = {}
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', {"id":"комбо"})
    items = divs.find('div', class_ = 's-elements-grid').find_all('div', 's-elements-grid__cell')
    for item in items:
        all_info = item.find_all('div', class_ = 'widget-text')
        data["title"] = all_info[0].text
        data["body"] = all_info[1].text
        data["price"] = all_info[2].text
        print(data)

#     # return sales_list
