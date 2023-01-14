from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import time

# 데이터 저장파일
csv_filename = 'prac1_review.csv'
csv_open = open(csv_filename, 'w+', encoding = 'utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('star', 'keyword', 'rv_text'))

# driver 설정
URL = 'https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000166294&dispCatNo=90000010002&trackingCd=Today&curation&egcode&rccode&egrankcode'
ops = webdriver.ChromeOptions()
ops.add_experimental_option('excludeSwitches', ['enable-logging'])
sv = Service(executable_path= 'C:\\Users\\admin\\Downloads\\chroemdriver')
driver = webdriver.Chrome(service=sv, options=ops)

driver.get(url=URL)

driver.find_element(By.XPATH,f'//*[@id="reviewInfo"]/a').click()

for p in range(1,6):
    driver.find_element(By.XPATH,f'//*[@id="gdasContentsArea"]/div/div[8]/a[{p}]').click()
    time.sleep(5)
    
    html = driver.page_source
    
    rv_list = driver.find_elements(By.CLASS_NAME, 'review_cont')
    for i, rv in enumerate(rv_list):
        rating = rv.find_elements(By.CLASS_NAME, 'point')
        star = len(rating)
        
        keyword = rv.find_elements(By.CLASS_NAME, 'txt').text
        rv_text = rv.find_elements(By.CLASS_NAME, 'txt_inner').text
        
        print(star, keyword, rv_text)
    
    csv.writer.writerow((star, keyword, rv_text))
    
csv_open.close()
driver.close()
        
