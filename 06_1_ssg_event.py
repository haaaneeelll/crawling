import requests
from bs4 import BeautifulSoup

url = "https://emart.ssg.com/event/eventMain.ssg"

headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

req = requests.get(url, headers = headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

cmplan_gridlist = soup.select_one(".cmplan_gridlist") # ul태그

event = cmplan_gridlist.select(".cmplan_unit") # a태그 

# 1. 원하는 태그를 불러오기 위해서는 상위 태그를 부르고..그 다음으로

# print(len(cmplan_link_clickable)) 

for rank, i in enumerate(event,1):
    card_date = i.select_one(".cmplan_date_tit")
    card_name = i.select_one(".cmplan_tit")
    card_unit = i.select_one(".cmplan_imgbx img")["alt"]
    card_unit_link = i.select_one(".cmplan_link.clickable")
    card_unit_link2 = card_unit_link["href"]
    print(f"{rank} : {card_date.text.strip()} \n {card_name.text}")

    if card_unit_link2.startswith("https"):
        print(f"{card_unit} \n {card_unit_link2}")
    else:
        print(f"{card_unit} \n https://emart.ssg.com/{card_unit_link2}")
    print()

### 크롤링을 할 때 주소가 잘려나오면 for문을 통해 출력한다.
