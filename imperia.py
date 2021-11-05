import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

def make_requests():
    html="https://mypizza.kg/Shares"
    r = requests.get(html)
    return r.content


def get_data():
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('main', class_='c-main')
    title = divs.find_all('div', class_='c-article__item')
    sales_list = []
    for item in title:
        annouth = item.find('div', class_='c-article__title').text
        description = item.find('div', class_='c-article__text').text
        sales_list.append({
            "title":annouth,
            "description": description,
        })
        # print(annouth) 
        # print(description)
    print(sales_list)
get_data()
    # return sales_list


