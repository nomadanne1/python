import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# > 우리가 가져온 html 문서(res.text)를 lxml parser를 통해서 BeautifulSoup 객체로 만듦. 
# > (★ soup이 모든 정보를 가지고 있음.)

print(soup.title) # <title>네이버 만화 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
print(soup.title.get_text()) # 네이버 만화 > 요일별  웹툰 > 전체웹툰

# 기본1. 네이버웹툰

print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
print(soup.a.attrs) # a element 의 속성 정보를 출력 
print(soup.a["href"]) # a element 의 href 속성 '값' 정보를 출력

print(soup.find("a", attrs={"class": "Nbtn_upload"})) # class="Nbtn_upload" 인 a element 를 찾아줘
print(soup.find(attrs={"class": "Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element 를 찾아줘

print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)

# 기본2. 네이버웹툰

# > parent, next_sibling, previous_sibling
print(rank1.a.get_text())
print(rank1.next_sibling)
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
print(rank1.parent)

# > find_next_sibling("li"), find_previous_sibling("li")
rank2 = rank1.find_next_sibling("li") # 계행포함x
print(rank2.a.get_text()) 
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

# > find_next_siblings("li") 
print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text= "갓 오브 하이스쿨-514화")
print(webtoon)