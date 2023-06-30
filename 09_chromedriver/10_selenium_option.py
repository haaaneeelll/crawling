from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.0.0 Safari/537.36"

user_data = "/Users/haneul/Desktop/웹 크롤링/크롤링/09_chromedriver/user_data"


options = Options() 

options.add_experimental_option("detach", True) # 1. 구글창이 계속 떠있는 옵션

options.add_argument(f"user-agent={user_agent}") # 7. 접속을 할 때 나의 정보를 바꿀 수 있다. 
options.add_argument(f"user-data-dir={user_data}") 
# 10. 유저 데이터를 만드는 것. 크롬에서 나가도 초기화되지않고 연결성있게 사용가능함. 기록이 남아있어
# 사용할 때마다 여러명의 유저인 척을 할 수 있음. # ****자주사용# ****자주사용# ****자주사용


# options.add_argument("--start-maximized") # 2. 화면을 가득히 ****자주사용
# options.add_argument("window-size=500,500") # 3. 원하는 크기로

# options.add_argument("--headless") # 4. 화면없이 사용하는 모드
# options.add_argument("--disable-gpu") # 4. 안되면 같이 사용하자.

# options.add_argument("--mute-audio") # 6.음소거
# options.add_argument("incognito") # 5. 시크릿 모드/ 웹서핑 기록이 남지않음

# options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 8, 시크릿모드 실행시 위에 뜨는 그 검은문구 뭐시기 사라짐 ****자주사용
# options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 9. 불필요한 메세지 삭제 ****자주사용


service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options = options)

url = "https://naver.com"

driver.get(url)
# temp = driver.page_source[:2000]
print(driver.page_source[:1000]) # 2000자까지
# print(len(temp))

# driver.quit()