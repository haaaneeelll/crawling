import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

headers = {
  "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)

html = req.text
soup = BeautifulSoup(html, "html.parser")

sect_movie_chart = soup.select_one(".sect-movie-chart")
box_image = sect_movie_chart.select(".box-contents")

for rank, movie in enumerate(box_image, 1):
    title = movie.select_one(".title")
    score = movie.select_one(".score")
    ticketing = score.select_one(".percent")
    egg_score = score.select_one(".egg-gage.small > .percent") # 2. 정확하게 찾으려는 태그 지정
    date = movie.select_one(".txt-info > strong").next_element # srtrong앞의 태그에 텍스트를 가져온다
    movie_link = movie.select_one("a")["href"]

    print(f"<<<{rank}위>>>")
    print(f"{title.text}")
    print(ticketing.get_text(" : ") ) # 1.get_text사용하면 출력양식 지정가능
    print(f"에그스코어: {egg_score.text.strip()}")
    print(f"개봉일자: {date.text.strip()} 개봉")
    print(f"연결링크: http://www.cgv.co.kr/{movie_link}")
    print()
