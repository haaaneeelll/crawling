from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

url = "https://section.cafe.naver.com/ca-fe/"

driver = webdriver.Chrome()

driver.get(url)
time.sleep(3) # 3초동안 기다렸다가 


html = driver.page_source

print(html)

# req = requests.get(url, headers = headers)
# html =  req.text
# 1. 위의 셀레니움 할 때 랑 비슷하네 리퀘스트랑

# soup = BeautifulSoup(html, "html.parser") 
# logo = soup.select_one("#special-input-logo")
# print(logo)




