import requests 
from bs4 import BeautifulSoup

url = "https://pedia.watcha.com/ko-KR"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser") 

# name = soup.find('div')
# print(name)
# print()

name_list = [element.text for element in soup.find_all(class_="css-5yuqaa")]
print(name_list)
print()
print(len(name_list))

# service_name = soup.find(class_="service_name", string="증권")
# print(service_name)
# print()
