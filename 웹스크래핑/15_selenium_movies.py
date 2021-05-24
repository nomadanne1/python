import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies)) # 0

# movies 길이 0 ?.? -> 파일로 확인해보자 !.!
with open("movie.html", "w", encoding="utf8") as f:
    # f.write(res.text) # 내용이 너무 많음.
    f.write(soup.prettify()) # html 문서를 보기 좋게 만들어준다.