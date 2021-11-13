import requests
from bs4 import BeautifulSoup

def make_requests():
    html = "https://dodopizza.kg/bishkek/bonusactions?gclid=CjwKCAjwoP6LBhBlEiwAvCcthAUVJjnicBju7HmNCXZhEHrfeBBXahyQDGR1XR09HnMj1BSxd5zHchoCYTQQAvD_BwE"
    r = requests.get(html)
    return r.content


def get_data1():
    html = make_requests()
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('main', class_='sc-1cc6vxk-2 eh81ri-0 bGeGUs bshVwl')
    title = divs.find_all('article')
    sales_list = []
    title_list = []
    description_list = []
    photo = open('logododopng.jpeg', 'rb')

    for item in enumerate(title, 1):
        annouth = item[1].find('h1', class_='title').text
        description = item[1].find('p').text
        full_title = f"{str(item[0])}. " + annouth
        title_list.append(full_title)
        full_description = f"{str(item[0])}. " + description
        description_list.append(full_description)
    sales_list.append(title_list)
    sales_list.append(description_list)
    sales_list.append(photo)
    return sales_list
