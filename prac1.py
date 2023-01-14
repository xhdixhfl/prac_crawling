from bs4 import BeautifulSoup
from selenium import webdriver

import re
import csv
import time

# 실제 데이터 저장 파일명
csv_filename = 'prac1_review.csv'
csv_open = open(csv_filename, 'w+', encoding = 'utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('star', 'keyword', 'review_text'))
print('ok')
driver = webdriver.Chrome('/Users/admin/Downloads/chromedriver_win32')
driver.implicitly_wait(3)
driver.get('https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000166294&dispCatNo=90000010002&trackingCd=Today&curation&egcode&rccode&egrankcode')

driver.find_element_by_xpath(f'//*[@id="gdasContentsArea"]/div/div[7]').click()
time.sleep(2)
print('ok1')
html = driver.page_source
bs = BeautifulSoup(html, 'html.parser')
print('ok2')
rv_list = driver.find_elements_by_class_name('review_cont')
print('ok3')
for i, review in enumerate(rv_list):
    rating = review.find_elements_by_class_name('point')
    star = len(rating)
    
    keyword = review.find_elements_by_class_name('txt').text
    review_text = review.find_elements_by_class_name('txt_inner').text
    
    print(star, keyword, review_text)
    
    csv.writer.writerow((star, keyword, review_text))

csv_open.close()
driver.close()