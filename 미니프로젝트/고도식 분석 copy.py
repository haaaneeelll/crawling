from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

url = "https://m.place.naver.com/restaurant/1054116696/home"

if driver.current_url != url:
    driver.get(url)
    time.sleep(2)

driver.find_element(By.LINK_TEXT, "리뷰").click()
time.sleep(0.5)

driver.find_element(By.LINK_TEXT, "더보기").click()
time.sleep(0.5)

# Click on "더보기" until all entries are visible
while True:
    try:
        driver.find_element(By.LINK_TEXT, "더보기").click()
        time.sleep(0.3)
    except NoSuchElementException:
        break

chart_list = driver.find_element(By.CSS_SELECTOR, ".eCPGL")
items = chart_list.find_elements(By.CSS_SELECTOR, ".YeINN")

data = []
rank_num = 1
for item in items:
    try:
        title = item.find_element(By.CSS_SELECTOR, ".zPfVt").text
        artist = item.find_element(By.CSS_SELECTOR, ".sBWyy").text
        data.append([rank_num, title, artist])
        rank_num += 1
    except NoSuchElementException:
        continue

for entry in data:
    print(f"Rank: {entry[0]}")
    print(f"Title: {entry[1]}")
    print(f"Artist: {entry[2]}")
    print("---")

# Save data to Excel file
df = pd.DataFrame(data, columns=["Rank", "Title", "Artist"])
df.to_excel("naver_data.xlsx", index=False)
