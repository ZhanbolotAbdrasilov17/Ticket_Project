import requests
from bs4 import BeautifulSoup


# def get_html(url):
#     response = requests.get(url)
#     return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('article', class_= "eh81ri-1 jBiDFj").find('h1', class_ = "title").text
    description = soup.find('p').text
    print(title)
    print(description)

def main():
    html="https://dodopizza.kg/bishkek/bonusactions?gclid=CjwKCAjwoP6LBhBlEiwAvCcthAUVJjnicBju7HmNCXZhEHrfeBBXahyQDGR1XR09HnMj1BSxd5zHchoCYTQQAvD_BwE"
    r = requests.get(html)
    get_data(r.content)

if __name__ == '__main__':
    main()


