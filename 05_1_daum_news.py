import requests
from bs4 import BeautifulSoup

headers = { 
  "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  }

url = "https://news.daum.net/"

def get_news_nums(news_num_text):
  
    news_num = "".join([num for num in news_num_text if num.isdigit()])


    return news_num

req = requests.get(url, headers = headers)
html = req.text

soup = BeautifulSoup(html, "html.parser") 

item_issue = soup.select(".item_issue")

for rank, i in enumerate(item_issue,1):
    name = i.select_one(".logo_cp img")["alt"]   
    category = i.select_one(".txt_category")
    txt = i.select_one(".link_txt")
    txt_link = get_news_nums(txt["href"])
    print(f"{rank} : {name} - {category.string}")
    print(f"{txt.string.strip()} \n https://v.daum.net/v/={txt_link}")
    print()


# for rank, i in enumerate(item_issue,1):
#     name = i.select_one(".logo_cp img")["alt"] 
#     category = i.select_one(".txt_category")

#     txt = i.select_one(".link_txt")
#     txt_link = txt["href"]

#     print(f"{rank} : {name} - {category.text}")
#     print(f"{txt.text.strip()} \n {txt_link}")
#     print()
