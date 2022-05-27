import requests
from bs4 import BeautifulSoup
import csv
file = open('books.csv', 'w', encoding='utf-8_sig')
file.write('სათაური'+','+'\n')
from time import sleep
for ind in range(1,6):
    url = 'https://biblusi.ge/products?category=291&page=1' + str(ind)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    div = soup.find('div', class_='b-overlay-wrap position-relative mt-1_875rem')
    # print(div)
    books = div.find_all('div', class_='mb-1_875rem col-sm-4 col-md-3 col-xl-2 col-6')
    for book in books:
        name = book.find('acronym').get('title')
        print(name)
        file.write(name + ',''\n')
    sleep(15)