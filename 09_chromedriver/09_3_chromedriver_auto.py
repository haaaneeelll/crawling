from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

service = Service(ChromeDriverManager().install()) # 1. 크롬드라이버 자동 설치하는 프로그램 만듬

driver = webdriver.Chrome(service = service)

driver.get("https://google.com")
time.sleep(2)