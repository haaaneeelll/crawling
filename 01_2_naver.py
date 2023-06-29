import requests 
from bs4 import BeautifulSoup

base_url  = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword
print(url)


headers = {"user-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}


req = requests.get(url, headers = headers)

html =  req.text

soup = BeautifulSoup(html, "html.parser") 

items = soup.select(".timeline_inner.api_ani_send")

rank_num = 1
for area in items:
    ad = area.select_one(".link_ad")
    if ad:
        continue

    print(f"<<<{rank_num}>>>")
        
    title = area.select_one(".api_txt_lines.total_tit")
    name = area.select_one(".sub_txt.sub_name")    
    print(name.text)
    print(title.text)
    print(title["href"])
    print()  

    rank_num += 1

