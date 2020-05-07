'''
task: get temprature of any given city for the current time from google.com

url: f'https://www.google.com/search?q=temp+city+of+{city}'

libraries required
1. requests
2. BeautifulSoup

'''

import requests
from bs4 import BeautifulSoup as bs


city = input('enter the city: ')
url = f'https://www.google.com/search?q=temp+city+of+{city}'

## storing the webpage content in the variable page
page=requests.get(url)

# page2 = requests.get('https://www.crunchbase.com/')

## To test wether request was succesful or not!

# if page2.status_code == 200:
#     print('We landed safely! Roger')
# else:
#     print(f'Contact with rover failed due to error code {page2.status_code}')


soup_object = bs(page.text,'html.parser')

# with open('temprature.html','w+',encoding='utf-8') as fp:
#     fp.write(soup_object.prettify())

temprature = soup_object.find('div',{'class':'BNeawe iBp4i AP7Wnd'})

# print(temprature.get_text())

print(f'temprature in {city} currently is:{temprature.get_text()}')

with open('temprature.txt','w+',encoding='utf-8') as fp:
    fp.write(f'temprature in the current city is:{temprature.get_text()}')



