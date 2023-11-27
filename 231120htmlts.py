import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

word = input()
wb = openpyxl.load_workbook('./gmarket.xlsx')
ws = wb.active

for page in range(1, 3):
    url = f'http://browse.gmarket.co.kr/search?keyword={word}&p={page}'
    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        products = soup.select('div.box__information-major')  # 클래스 선택자 수정
        for product in products:
            title_tag = product.select_one('.box__item-title')
            title = title_tag.select_one('.text__item')['title']
            link = product.select_one('.link__item')['href']
            price = product.select_one('strong').text

            # 데이터프레임에 추가
            ws.append([title, link, price])
            print(title)
            print(link)
            print(price)

wb.save('./gmarket.xlsx')
