from typing import SupportsAbs
import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('main', class_='c-main')
    title = divs.find_all('div', class_='c-article__item')
    print(divs)
    print(title)
    sales_list = []
    for item in title:
        annouth = item.find('div', class_='c-article__title').text
        description = item.find('div', class_='c-article__text').text
        sales_list.append({
            "title":annouth,
            "description": description,
        })
        print(annouth) 
        print(description)

    return sales_list

        

def main():
    html="https://mypizza.kg/Shares"
    r = requests.get(html)
    get_data(r.content)

if __name__ == '__main__':
    main()


