from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = Options()

user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"

options.add_argument(f"user-agent={user_agent}")

options.add_argument("--start-maximized")

options.add_experimental_option("detach", True)

options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

url = "https://m2.melon.com/index.htm"

driver.get(url)
time.sleep(2)

print(driver.current_url)

if driver.current_url != url:
    driver.get(url)
    time.sleep(2)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(2)

driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()
time.sleep(2)

chart_list = driver.find_element(By.CSS_SELECTOR, "#_chartList")

items = chart_list.find_elements(By.CSS_SELECTOR, ".list_item")

data = []
rank_num = 1

for item in items:
    title = item.find_element(By.CSS_SELECTOR, ".title.ellipsis").text
    artist = item.find_element(By.CSS_SELECTOR, ".name.ellipsis").text
    data.append([rank_num, title, artist])
    rank_num += 1

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=["Rank", "Title", "Artist"])

# Save the DataFrame to an Excel file
df.to_excel("chart_data.xlsx", index=False)

driver.quit()
