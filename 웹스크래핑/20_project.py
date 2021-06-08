# Project) 웹 스크래핑을 이용하여 나만의 비서를 만드시오

'''
[조건]
1. 네이버에서 오늘 서울의 날씨정보를 가져온다
2. 헤드라인 뉴스 3건을 가져온다
3. IT 뉴스 3건을 가져온다
4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다
'''

import requests
from bs4 import BeautifulSoup 

# soup 만드는 부분  함수로 만듦
def create_soup(url):
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language":"ko-KR,ko" 
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("  (링크 : {})".format(link))

# 1.
def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    # 흐림, 어제보다 00˚ 높아요
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    # 현재 00˚C (최저 00˚ / 최고 00˚)
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","") # 현재 온도
    min_temp = soup.find("span", attrs={"class":"min"}).get_text() # 최저 온도
    max_temp = soup.find("span", attrs={"class":"max"}).get_text() # 최고 온도
    # 오전 강수확률 00% / 오후 강수확률 00%
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip() # 오전 강수확률
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip() # 오전 강수확률

    # 미세먼지 00㎍/㎥ 좋음
    # 초미세먼지 00㎍/㎥ 좋음
    '''
     cf. 클래스 2개일 경우 >> attrs={"class":["indicator", "class2"]} (list 사용)
         class 말고 다른 속성도 함께 비교하고 싶은 경우 >> attrs={"class":"indicator", "id":"dust"} (, 사용)
         class와 text도 함께 찾고 싶을경우 >> attrs={"class":"indicator"}, text=["미세먼지", "초미세먼지]
          (*class가 indicator 이면서 text가 '미세먼지'이거나 '초미세먼지'인 것)
    '''
    dust = soup.find("dl", attrs={"class":"indicator"}) 
    pm10 = dust.find_all("dd")[0].get_text() # 미세먼지
    pm25 = dust.find_all("dd")[1].get_text() # 초미세먼지

    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()

# 2. 
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3) # ★ limit=3 - li 태그 3개까지만 찾아라!
    for index, news in enumerate(news_list):
        # title = news.div.a.get_text()
        title = news.find("a").get_text().strip() # find("a") 첫번째 a태그
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()

# Connection aborted.', RemoteDisconnected('Remote end closed connection without response') 오류 >> user-agent 정의하니 해결

'''
>> enumerate 함수
리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가집니다.
enumerate는 “열거하다”라는 뜻입니다.
이 함수는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴합니다.
보통 enumerate 함수는 for문과 함께 자주 사용됩니다.

[예시 참고]
https://wikidocs.net/20792
'''

# 3.
def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li", limit=3) # 3개까지만 가져오기
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a 태그의 정보를 사용

        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()

# 4. 
import re

def scrape_english():
    print("[오늘의 영어 회화]")
    url="https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할 때 , index 기준 4~7 까지 잘라서 가져옴 2로나눠서 
        print(sentence.get_text().strip())
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할 때 , index 기준 0~3 까지 잘라서 가져옴 2로나눠서
        print(sentence.get_text().strip())

'''
정규식 기본 (Regular expression)

import re
>> p = re.compile ("원하는 형태")
'''
if __name__ == "__main__": 
    # scrape_weather() # 오늘의 날씨 정보 가져오기
    # scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
    # scrape_it_news() # IT 뉴스 정보 가져오기
    scrape_english() # 오늘의 영어 회화 가져오기

'''
if __name__ == "__main__" :

>> 해당 모듈이 임포트된 경우가 아니라 
>> 인터프리터에서 직접 실행된 경우에만,
>> if문 이하의 코드를 돌리라는 명령
'''