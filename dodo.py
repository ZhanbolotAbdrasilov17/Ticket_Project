import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

def make_requests():
    html="https://dodopizza.kg/bishkek/bonusactions?gclid=CjwKCAjwoP6LBhBlEiwAvCcthAUVJjnicBju7HmNCXZhEHrfeBBXahyQDGR1XR09HnMj1BSxd5zHchoCYTQQAvD_BwE"
    r = requests.get(html)
    return r.content


def get_data():
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('main', class_='sc-1cc6vxk-2 eh81ri-0 bGeGUs bshVwl')
    title = divs.find_all('article')
    sales_list = []
    for item in enumerate(title):
        annouth = item[1].find('h1', class_='title').text
        description = item[1].find('p').text
        sales_list.append({
            "title":annouth,
            "description": description,
            "number":item[0]
        })
    return sales_list
#     print(sales_list[:]['title'])
# get_data()


