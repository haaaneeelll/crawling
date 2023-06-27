import requests 
from bs4 import BeautifulSoup

base_url  = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword
print(url)


# headers = {
#   "user-Agent" : " Mozilla/5.0"
# }

# req = requests.get(url, headers = headers)

# print(req.request.headers)

# html =  req.text

# # print(html)

# soup = BeautifulSoup(html, "html.parser")

# logo = soup.select(".css-5yuqaa")

# # print(logo)


