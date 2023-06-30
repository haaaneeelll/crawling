from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()

options.add_argument("--start-maximizes")
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

url = "https://naver.com"

driver.get(url)
time.sleep(2)

# driver.find_element(By.CLASS_NAME)
# driver.find_element(By.ID)
# driver.find_element(BY.CSS_SELECTOR)
# driver.find_element(BY.NAME)
# driver.find_element(BY.TAG_NAME)
# driver.find_element(BY.XPATH)

# driver.find_element(By.LINK_TEXT)
# driver.find_element(BY.PARTIAL_LINK_TEXT)


"""
<input id="query" name="query" type="search" title="검색어를 입력해 주세요." 
placeholder="검색어를 입력해 주세요." maxlength="255" 
autocomplete="off" class="search_input" data-atcmp-element="">
"""

# driver.find_element(By.XPATH, '//*[@title="검색어를 입력해 주세요."]').send_keys("블랙핑크", Keys.ENTER)
# time.sleep(2)

# # driver.find_element(By.XPATH, '//*[text()="VIEW"]').click() 
# driver.find_element(By.LINK_TEXT, "VIEW").click()
# time.sleep(2)

# driver.find_element(By.PARTIAL_LINK_TEXT, "인플루언").click() 
# # xpath 대신 사용가능함.

link_service = driver.find_elements(By.CLASS_NAME, "link_service")

# print(link_service)
# print()
# print(dir(link_service[0]))
# print()
# print(len(link_service))


for num, link_service in enumerate(link_service, 1):
    print(num)  
    print(link_service.get_attribute("outerHTML"))
    print(link_service.text)
    print()
# 1. Link service를 품고 있는 html을 출력한다. 즉 클래스가 포함된 전체 html을 출력
    if link_service.text == "쇼핑":
        link_service .click()
        break

time.sleep(2)

driver.quit()