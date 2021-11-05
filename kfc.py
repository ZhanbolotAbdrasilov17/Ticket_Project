import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

def make_requests():
    html="https://kfc.kg/promo"
    r = requests.get(html)
    return r.content


def get_data():
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', class_='main-content-inr group')
    title = divs.find_all('div', class_='content-list-main')
    
    sales_list = []
    for item in title:
        annouth = item.find('h2', class_='title').text
        description = item.find('p',).text
        sales_list.append({
            "title":annouth,
            "description": description,
        })
        print(annouth) 
        print(description)
    print(sales_list)
get_data()
    # return sales_list
