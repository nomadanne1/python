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

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    # 흐림, 어제보다 00˚ 높아요
    soup.find("p", attrs={"class":"cast_txt"}).get_text()
    # 현재 00˚C (최저 00˚ / 최고 00˚)
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    min_temp = soup.find("span", attrs={})
    max_temp = None



if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
