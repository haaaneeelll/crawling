from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = Options()

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")

options.add_argument("--start-maximized")

options.add_experimental_option("detach", True)

options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

url = "https://www.genie.co.kr/"

driver.get(url)
time.sleep(2)

print(driver.current_url)

if driver.current_url != url:
    driver.get(url)
    time.sleep(2)

driver.find_element(By.LINK_TEXT, "지니차트").click()
time.sleep(2)

data = []
rank_num = 1
for page in range(2):  # Assuming there are 2 pages with 50 rankings each
    chart_list = driver.find_element(By.CSS_SELECTOR, ".list-wrap")
    items = chart_list.find_elements(By.CSS_SELECTOR, "tr.list")

    for item in items:
        # Extract the title
        title = item.find_element(By.CSS_SELECTOR, "a.title").text

        # Extract the artist
        artist = item.find_element(By.CSS_SELECTOR, "a.artist").text

        data.append([rank_num, title, artist])

        print(f"Rank: {rank_num}, Title: {title}, Artist: {artist}")

        rank_num += 1

    if page < 1:
        driver.find_element(By.LINK_TEXT, "51 ~ 100 위").click()
        time.sleep(2)

driver.quit()

# Save data to Excel file
df = pd.DataFrame(data, columns=["Rank", "Title", "Artist"])
df.to_excel("chart_data.xlsx", index=False)
