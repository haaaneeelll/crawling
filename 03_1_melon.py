import requests
from bs4 import BeautifulSoup

headers = { 
  "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  }

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers = headers)
html = req.text

# print(html) # 1. html이 정상출력되는지 확인

soup = BeautifulSoup(html, "html.parser") # 2. html 파서로 분석을 할 것이다.and

lst50 = soup.select(".lst50") # 3. lst50 클래스를 전부 가져오자.

lst100 = soup.select(".lst100") # 6. 100위도 뽑자.

lst = lst50 + lst100 # 6 . 합쳐야함..

# 4. 랭크와 제목...여기까지 거의 루틴작업.. 기억하기
for rank, i in enumerate(lst, 1):
    title = i.select_one(".ellipsis.rank01 a")
    name = i.select_one(".ellipsis.rank02 a")
    album = i.select_one(".ellipsis.rank03 a")
    print(f"{rank} : {title.text}")
    print(f"{name.text} : {album.text}")
    print()
# -> 5. 출력을 했을 때  제목이 내려가는 현상이 발생함. 가져온 태그가 div태그인데 타이틀은 그  안의 a태그에 있음. text.strip()으로 해결
# 더 확실한 방법은 가져올려는 태그를 확실히 지정 i.select_one(".ellipsis.rank01 a")


  
