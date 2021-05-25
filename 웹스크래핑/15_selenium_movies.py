import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language":"ko-KR,ko" # Ko-KR,ko - 한글페이지 있으면 한글페이지 반환
    }
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies)) # 0 -> headers (User-Agent, Accept-Language) 설정후 : 10

# movies 길이 : 0 > why? (파일로 확인) 
# requests로 접속했을때 미국에서 접속하는것으로 디폴트 접속 > User Agent로 해결

# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text) # 내용이 너무 많음.
#     f.write(soup.prettify()) # html 문서를 보기 좋게 만들어준다.

# movies 길이 : 10 > why? 처음 10개보이고 스크롤내려야.. 10개씩 추가된다 
# ★동적페이지 > Selenium으로 해결

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)