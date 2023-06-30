from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()

user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"

options.add_argument(f"user-agent={user_agent}")

options.add_argument("--start-maximized") # 화면 풀

options.add_experimental_option("detach", True)

options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

url = "https://m2.melon.com/index.htm"


driver.get(url)
time.sleep(2)
## 여기까지 기본틀

print(driver.current_url)

if driver.current_url != url:
    driver.get(url)
    time.sleep(2)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(2)

driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click() 
time.sleep(2)

# 2. 여러개를 찾았기 때문에 elements...이해가 안되지..? more btn 검색을 해보면 3개가 있자나
# 그 3개를 가져오고 너가 찾으려는게 두번째 btn이자나 그러니까 [1]을 넣어줘야지

# driver.quit()

# 1. 이벤트창에 들어갈 때 이를 뚫고 들어가기 위한 코드 2번 불러일으킴
# 배너 같은건 닫힘 버튼 클래스 찾아서 클릭하자. 

# type.1
chart_list = driver.find_element(By.CSS_SELECTOR , "#_chartList")

items = chart_list.find_elements(By.CSS_SELECTOR, ".list_item")
# 3. 크롤링을 셀레니움으로 본격적으로 하는 코드다.
# 여기서 중요한점은 모두를 감싸는 class나 id를 찾고 그 하위 개념을 추출한다.



# 정제되어 있지 않은 코드를 거르려고 함.
# type2. 모든 코드가 좋은 코드는 아니다. 멜론처럼 차트리스트라는 전체를 아우르는 html코드가 없을수도 있다. 
# 밑은 다음과 같은 상황일 때 사용한다.

# items = driver.find_elements(By.CSS_SELECTOR, ".list_item")
# # 4. driver로 가져와야 100개 넘게 가져오지

# for item in items[:] : # [:]를 넣어주자. 전체를 의미함.
#     try:
#         ranking_num = item.find_element(By.CSS_SELECTOR, ".ranking_num") 
#     except NoSuchElementException:
#         print("랭크가 없어서 삭제합니다.")
#         items.remove(item) # 7. 랭크가 없는 item만 가져오면 1위부터 100위까지 나올꺼다
#     # 5. ranking_num만 가져와도 다가져올 수 있음..멜론 같은경우 뮤직비디오가 랭크가 없는듯

#     # 6. 찾으려고 하는데 찾을 수 없으면 뷰티플숲같은 경우 none을 출력하지만 셀레디움은 에러를 보낸다.
#     # 에러처리를 많이해야해



