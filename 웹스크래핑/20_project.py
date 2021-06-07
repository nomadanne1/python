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
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

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

# 2. 헤드라인 뉴스 3건을 가져온다
def scrape_headline_news():
    print("[헤드라인 뉴스]")




'''
if __name__ == "__main__" :

>> 해당 모듈이 임포트된 경우가 아니라 
>> 인터프리터에서 직접 실행된 경우에만,
>> if문 이하의 코드를 돌리라는 명령
'''

if __name__ == "__main__": 
    # scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news()
