from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # 1. find문에 필요함
from selenium.webdriver.common.keys import Keys # 8. 엔터키나 스페이스에 필요함
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

options = Options()

options.add_argument("--start-maximized") # 화면 풀
options.add_experimental_option("detach", True) # 계속 뜸

service = Service(ChromeDriverManager().install()) # 크롬드라이브 자동 설치

driver = webdriver.Chrome(service = service, options=options)

url = "https://map.naver.com/v5/"
time.sleep(2)

# driver.find_element(By.ID, "query").send_keys("뉴진스") # 2. id를 찾는거니
# time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, ".btn_search").click() # 3. id대시 셀렉터 사용해도 됨, 셀렉터는 클래스 아이디 다가능,  검색버튼 누르는 쿼리
# time.sleep(2)
# # 4. 뉴진스 검색하고 버튼 누르는 것 까지..

# # driver.find_elements(By.CLASS_NAME, "menu")[2].click() 
# # # 5. view탭을 클릭하기 위해서... 클래스 네임이 메뉴에서 3번째 클릭 지정
# # # 근데 이건 어려운 이유가 검색어마다 탭의 위치가 달라. 더 정확한게 필요해
# # # view가 확실히 가는 것은 텍스트밖에 없어

# driver.find_element(By.XPATH, '//*[text()="VIEW"]').click() 
# time.sleep(2)
# # 6. //* = "하위에 있는 모든 것에서"라는 뜻임.
# # xpath는 텍스트같은 것 찾을 때나 사용하자. 복잡하기 때문에...

# driver.find_element(By.NAME, "query").clear()
# time.sleep(2)
# # 7. name이 쿼리인 것을 지우는 코드

# driver.find_element(By.NAME, "query").send_keys("에스파")
# time.sleep(2)

# driver.find_element(By.NAME, "query").send_keys(Keys.ENTER)
# time.sleep(2)

# # 9. 에스파를 검색, 엔터까지하는 코드

# for i in range(10):
#     driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
#     time.sleep(2)
# # 10. 스크롤도 살짝 내림
# # page_down 말고 End가 더 많이 내려감

# html = driver.page_source # req.text와 같은 역할

# ############################################크롤링
# soup = BeautifulSoup(html, "html.parser") 

# items = soup.select(".timeline_inner.api_ani_send")

# rank_num = 1
# for area in items:
#     ad = area.select_one(".link_ad")
#     if ad:
#         continue

#     print(f"<<<{rank_num}>>>")
        
#     title = area.select_one(".api_txt_lines.total_tit")
#     name = area.select_one(".sub_txt.sub_name")    
#     print(name.text)
#     print(title.text)
#     print(title["href"])
#     print()  

#     rank_num += 1
# ############################################크롤링


# # driver.save_screenshot("/Users/haneul/Desktop/웹 크롤링/크롤링/09_chromedriver/11_selenium_naver/naver.jpg")
# # print("저장완료")

# driver.quit()






