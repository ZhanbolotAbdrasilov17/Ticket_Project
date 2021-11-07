import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

def make_requests():
    html="https://nambafood.kg/bonus"
    r = requests.get(html)
    return r.content


def get_data():
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', class_='catalog-content')
    title = divs.find_all('a', class_='cafe-item')
   
    # print(divs, title)
    sales_list = []



    for item in title:
        annouth = item.find('div', class_='cafe-item--wrap').get_text(strip=True)
        # description = item.find('div', class_='information').get_text(strip=True)
        sales_list.append({
            "title":annouth,
            # "description": description,
        })
        # print(annouth) 
        # # print(description)
    print(sales_list)
print(get_data())
    # return sales_list
