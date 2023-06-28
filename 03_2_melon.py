import requests
from bs4 import BeautifulSoup

# 1. 자바스크립트 안에 있는 숫자를 꺼내오고 싶다.
def get_song_nums(song_num_text):
    # song_num = []
    # for num in song_num_text:
    #     if num.isdigit(): # 받은 문자가 숫자인지 판단을 해줌
    #         song_num.append(num)  # 입력 받은게 숫자면 리스트에 넣는 것.

    # song_num = "".join(song_num)
    # return song_num

    # 6. 리스트 컴프리헨션- 한줄로 가능하다.

    song_num = "".join([num for num in song_num_text if num.isdigit()])
    # 위 식을 분해해보면 for num in song_num_text는 반복문
    # 그 다음 if문
    # 맨앞의 num의 변수에 list에 append를 적용해서 저장... append과정없이 바로 num으로

    return song_num

headers = { 
  "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  }

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers = headers)
html = req.text



soup = BeautifulSoup(html, "html.parser") 

# 방법 1
# lst50 = soup.select(".lst50") 

# lst100 = soup.select(".lst100") 

# lst = lst50 + lst100 

# 방법 2
# lst = soup.select(".lst50, .lst100") # 5. 위에있는 3줄을 한줄로 가능함.

# 방법 3
lst = soup.find_all(class_=["lst50", "lst100"]) # find_all은 리스트 형태!


# 2. 가수 링크와 앨범 링크를 가져 올 수 있도록
# 3. 여기서 그냥 실행을 하면 javascript:melon.link.goAlbumDetail('11033394'); 이런식으로 링크가 나옴. 근데 난 숫자만 원해
# 이때 해야할 것은 위에서 만든 함수를 링크에 적용한다. get_song_nums(singer['href'])
for rank, i in enumerate(lst, 1):
    title = i.select_one(".ellipsis.rank01 a")

    singer = i.select_one(".ellipsis.rank02 a")
    singer_link = get_song_nums(singer['href'])   # 필요한 번호만 가져온다.

    album = i.select_one(".ellipsis.rank03 a")
    album_link = get_song_nums(album["href"])
    print(f"{rank} : {title.text}")
    print(f"{singer.text} : https://www.melon.com/artist/timeline.htm?artistId={album_link}")
    print(f"{album.text} : https://www.melon.com/album/detail.htm?albumId={album_link}") # 4. 이동가능한 링크를 넣어서 완벽한 링크를 출력한다.

    print()



  
