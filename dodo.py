from typing import SupportsAbs
import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('main', class_='sc-1cc6vxk-2 eh81ri-0 bGeGUs bshVwl')
    title = divs.find_all('article')
    sales_list = []
    for item in title:
        annouth = item.find('h1', class_='title').text
        description = item.find('p').text
        sales_list.append({
            "title":annouth,
            "description": description,
        })
        # print(annouth) 
        # print(description)

    return sales_list

        

def main():
    html="https://dodopizza.kg/bishkek/bonusactions?gclid=CjwKCAjwoP6LBhBlEiwAvCcthAUVJjnicBju7HmNCXZhEHrfeBBXahyQDGR1XR09HnMj1BSxd5zHchoCYTQQAvD_BwE"
    r = requests.get(html)
    get_data(r.content)

if __name__ == '__main__':
    main()
