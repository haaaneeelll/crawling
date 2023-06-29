import requests
from bs4 import BeautifulSoup

base_url = "https://www.coupang.com/np/search?component=&q="

keyword = input("검색어 상품을 입력하세요 : ")

search_url = base_url + keyword

print(search_url)

headers = {
       "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
       "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}

cookie = {"a": "b"} # 1. 접속이 원천 차단될 때는 쿠키를 설정한다. 아무의미없는 쿠키

req = requests.get(search_url,timeout = 5, headers=headers, cookies = cookie)

# print(req.status_code) # 2.404에러같은...상태 코드

html = req.text

soup = BeautifulSoup(html, "html.parser") 

# items = soup.select(".search-product") # 2. 전과 같이 추출을 하려했는데...원하는 결과가 안나온다. 
items = soup.select("[class=search-product]") # 3. 클래스를 명확히 지정
print(len(items))


rank = 1 
for item in items:
    badge_rocket = item.select_one(".badge.rocket")
    if not badge_rocket: # 5. 로켓배송이 아니면 프린트를 안함. 넘어감.반복문 다시 실행
        continue

    name = item.select_one(".name")
    price = item.select_one(".price-value")
    thumb = item.select_one(".search-product-wrap-img")
    link = item.a["href"] # 6. 하위 a태그에 코드를 건다.

    print(f"{rank}위") 
    print(name.text) # 4. 쿠팡은 검색할 때마다 달라짐.
    print(f"{price.text}원")
    print(f"https://coupang.com{link}")

    if thumb.get("data-img-src"):
        img_url = f"http:{thumb.get('data-img-src')}" # 8. get을 넣는 것이 포인트

    else:
        img_url = f"http:{thumb['src']}"
    print(img_url)
    # print(thumb.get("data-img-src")) # 7. 1위부터 4위까지 None이 나옴. if문 필요함
    print()

    img_req = requests.get(img_url)

    with open(f"{rank}.jpg", "wb") as f:
      f.write(img_req.content)


    rank += 1 

    