# 필수 라이브러리 로딩
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import time

# driver 설정
URL = 'https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000176292&dispCatNo=100000100010008&trackingCd=Cat100000100010008_MID'
ops = webdriver.ChromeOptions()
ops.add_experimental_option('excludeSwitches', ['enable-logging'])

sv = Service(executable_path= 'C:\\Users\\admin\\Downloads\\chroemdriver')
driver = webdriver.Chrome(service=sv, options=ops)

driver.get(url=URL)
driver.find_element(By.XPATH,f'//*[@id="reviewInfo"]/a').click()

# driver 설정
URL = 'https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo=100000100010008&isLoginCnt=0&aShowCnt=0&bShowCnt=0&cShowCnt=0&gateCd=Drawer&trackingCd=Cat100000100010008_MID'
ops = webdriver.ChromeOptions()
ops.add_experimental_option('excludeSwitches', ['enable-logging'])

sv = Service(executable_path= 'C:\\Users\\admin\\Downloads\\chroemdriver')
driver = webdriver.Chrome(service=sv, options=ops)

driver.get(url=URL)
driver.find_element(By.XPATH,f'//*[@id="Contents"]/ul[2]/li[1]').click()

for i in range(1,6):
    star = driver.find_element(By.XPATH, f'//*[@id="gdasList"]/li[{i}]/div[2]/div[1]/span[1]').text
    print(star)
    keyword = [driver.find_element(By.XPATH, f'//*[@id="gdasList"]/li[{i}]/div[2]/div[2]/dl[{j}]/dd/span').text for j in range(1,4)]
    print(keyword)
    rv_text = driver.find_element(By.XPATH, f'//*[@id="gdasList"]/li[{i}]/div[2]/div[3]').text
    print(rv_text)
    
# brand
driver.find_element(By.XPATH,'//*[@id="gdasList"]/li[1]/div[2]/div[1]/span[1]').text
# pname
driver.find_element(By.XPATH,'//*[@id="Contents"]/div[2]/div[2]/div/p[2]').text
# price
driver.find_element(By.XPATH,'//*[@id="Contents"]/div[2]/div[2]/div/div[1]').text
# star
driver.find_element(By.XPATH,'//*[@id="repReview"]').text
# 페이지 이동
driver.find_element(By.XPATH,f'//*[@id="reviewInfo"]/a').click()
# rstar
driver.find_element(By.XPATH,'//*[@id="gdasList"]/li[1]/div[2]/div[1]/span[1]/span').text
# rkeyword
driver.find_element(By.XPATH,'//*[@id="gdasList"]/li[1]/div[2]/div[2]').text
# rtext
driver.find_element(By.XPATH,'//*[@id="gdasList"]/li[1]/div[2]/div[3]').text
# 한사람의 리뷰 내용만 리스트로 만들기
rstar = driver.find_element(By.XPATH,'//*[@id="gdasList"]/li[1]/div[2]/div[1]/span[1]/span').text
rkeyword = driver.find_element(By.XPATH,'//*[@id="gdasList"]/li[1]/div[2]/div[2]').text
rtext = driver.find_element(By.XPATH,'//*[@id="gdasList"]/li[1]/div[2]/div[3]').text
review = [rstar, rkeyword, rtext]

# 리뷰를 2중 리스트로 
review = []
for i in range(1,6):
    rstar = driver.find_element(By.XPATH,f'//*[@id="gdasList"]/li[{i}]/div[2]/div[1]/span[1]/span').text
    rkeyword = driver.find_element(By.XPATH,f'//*[@id="gdasList"]/li[{i}]/div[2]/div[2]').text
    rtext = driver.find_element(By.XPATH,f'//*[@id="gdasList"]/li[{i}]/div[2]/div[3]').text
    review.append([rstar, rkeyword, rtext])
    
# 하나의 상품을 한번에 출력시키는 구문 정리
brand = driver.find_element(By.XPATH,'//*[@id="Contents"]/div[2]/div[2]/div/p[1]').text
pname = driver.find_element(By.XPATH,'//*[@id="Contents"]/div[2]/div[2]/div/p[2]').text
price = driver.find_element(By.XPATH,'//*[@id="Contents"]/div[2]/div[2]/div/div[1]').text
star = driver.find_element(By.XPATH,'//*[@id="repReview"]').text
review = []

for i in range(1,6):
    rstar = driver.find_element(By.XPATH,f'//*[@id="gdasList"]/li[{i}]/div[2]/div[1]/span[1]/span').text
    rkeyword = driver.find_element(By.XPATH,f'//*[@id="gdasList"]/li[{i}]/div[2]/div[2]').text
    rtext = driver.find_element(By.XPATH,f'//*[@id="gdasList"]/li[{i}]/div[2]/div[3]').text
    review.append([rstar, rkeyword, rtext])
print(brand, pname, price, star, review)
driver.close()
