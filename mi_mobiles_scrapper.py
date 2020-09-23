import requests

from bs4 import BeautifulSoup
from urllib.request import urlopen as uRqst
from urllib.parse import urljoin
import cssutils
import json


def make_soup(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    # product_data.append(soup)
    return soup

# def fetch_url():
#     soup = make_soup(web_url)
#     # product_data.append(soup)
#     mobile_names=[]
#     links = soup.find_all("div",class_="product-item__figure")
#     for each in links:
#       mobile_names.append("https:" + each.select('a')[0]['href'])
#       # product_data.append(mobile_names)
#     return mobile_names


url = 'https://www.flipkart.com/redmi-8-sapphire-blue-64-gb/p/itmd1c68a1a86f5e?pid=MOBFKPYDENDXZZ7U&lid=LSTMOBFKPYDENDXZZ7U9TT5NP&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Mi&fm=organic&iid=3ababe67-423b-4924-be14-9de89c50040e.MOBFKPYDENDXZZ7U.SEARCH&ppt=browse&ppn=browse&ssid=ub3jtn1d5s0000001600830247417'


def get_full_data():
    #   mobile_urls = fetch_url()
    # product_data.append (mobile_urls)
    product_data = {}
    product_soup = make_soup(url)

    data = product_soup.find("div", class_="_3Z5yZS")
    try:
        title2 = data.find("span", class_="_35KyD6").get_text()
        try:
            title = title2.replace("\u00a0\u00a0", "")

        except:
            title = title2
        product_data['title'] = title
    except:
        print('title')
    try:
        color_link = list(each.get("href")
                          for each in data.find_all("a", class_="_2VtE5i"))
        product_data['colorLink'] = color_link
    except:
        print('color link')
    try:
        a = list(each for each in data.find_all("div", class_="_37KLG6"))
    except:
        print('a error')
    try:
        color = list(each.get_text()
                     for each in a[0].find_all("div", class_="_3xOS0O"))
        product_data['color'] = color
    except:
        print('color')
    try:
        variations = list(each.get_text()
                          for each in a[1].find_all("div", class_="_3xOS0O"))
        product_data['variations'] = variations
    except:
        print('variations')
    try:
        mrp2 = data.find("div", class_="_1POkHg").get_text()
        try:
            mrp = mrp2.replace("\u20b9", "")
        except:
            mrp = mrp2
        product_data['Mrp'] = mrp
    except:
        print('mrp')
    try:
        price2 = data.find("div", class_="_3qQ9m1").get_text()
        try:
            price = price2.replace("\u20b9", "")
        except:
            price = price2
        product_data['price'] = price
    except:
        print('price')
    try:
        mImage = list(cssutils.parseStyle(each['style'])['background-image'].replace(
            'url(', '').replace(')', '') for each in data.find_all("div", class_="_2_AcLJ"))
        product_data['imageUrl'] = mImage
    except:
        print('m image')
    camImage = []
    try:
        highlights = list(each.get_text()
                          for each in data.find_all("li", class_="_2-riNZ"))
        product_data['highlights'] = highlights
    except:
        print('highlights')
    try:
        description = data.find("div", class_="_3la3Fn").get_text()
        product_data["discription"] = description
    except:
        print('description')
    try:
        specification_keys = list(each.get_text()
                                  for each in data.find_all("td", class_="_3-wDH3"))
    except:
        print('specification-keys')
    try:
        specification_values = list(each.get_text()
                                    for each in data.find_all("li", class_="_3YhLQA"))
    except:
        print('specification-values')
    specifications = {}
    try:
        for i in range(len(specification_keys)):
            specification_keys2 = ''.join(specification_keys[i].split())
            specifications[specification_keys2] = specification_values[i]

        product_data['specifications'] = specifications
    except:
        print('specification')
    return product_data


product_data = get_full_data()
num =5
max_num=5
# print(product_data)
# print(json.dumps(product_data))
mobile_data = open('./mobiles.json', 'a')
if num == 0:
    mobile_data.write('[' + json.dumps(product_data)+'')
elif num ==max_num:
    mobile_data.write((',\n'+json.dumps(product_data)+']'))
else:
    mobile_data.write((',\n'+json.dumps(product_data)))
  
