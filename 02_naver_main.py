import requests 
from bs4 import BeautifulSoup

url  = "https://naver.com"

headers  =  {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

req = requests.get(url, headers = headers)

html =  req.text

soup = BeautifulSoup(html, "html.parser") 

# 찾는 다양한 방법...
# print(soup.h1)
# print()

# h1 = soup.find('h1')
# print(h1)
# print()

# h1 = soup.find(class_="search_logo") # class_임 주의
# print(h1)
# print()

# service_name = soup.find(class_="service_name", string="증권")
# print(service_name)
# print()

# find all도 가능.

