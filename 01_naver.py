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

total_area = soup.select(".total_area")
timeline_area = soup.select(".timeline_area")

if total_area:
    areas = total_area
elif timeline_area:
    areas = timeline_area
else:
    print("확인요망")

# titles = soup.select(".api_txt_lines.total_tit")

# names = soup.select(".sub_txt.sub_name")

for area in areas:
    title = area.select_one(".api_txt_lines.total_tit")
    name = area.select_one(".sub_txt.sub_name")    
    print(name.text)
    print(title.text)
    print(title["href"])
    print()   
