# 11-1. 모듈 (a.k.a. 부품, 확장자 - .py)

# 모듈사용 - import
import theater_module 
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_mornig(4) # 4명이서 조조 할인 영화 보러 갔을때
theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을때

# as 
import theater_module as mv
mv.price(3)
mv.price_mornig(4)
mv.price_soldier

from theater_module import * # theater_module 모듈 모두 사용
# from random import *
price(3)
price_mornig(4)
price_soldier(5)

from theater_module import price, price_mornig, price_soldier
price(5)
price_mornig(6)
price_soldier(7) # 오류

from theater_module import price_soldier as price
price(5) # == price_soldier(5) 

# 11-2. 패키지 (모듈들을 모아놓은 집합)

import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detatil()
 # import 맨뒤, 모듈이나 패키지만 가능 
 # (클래스나 함수는 import불가) -> from import에서는 가능 

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detatil()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# 11-3. __all__

# from random import *
from travel import *  # * - 공개 범위를 설정해줘야함. -> __init__.py 
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 11-4 모듈 직접 실행 - thialind.py (모듈에서)
'''
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
else:
    print("Thailand 외부에서 모듈 호출")
'''

# 11-5. 패키지, 모듈 위치 - inspect.getfile(모듈명)

import inspect 
import random
from travel import *
print(inspect.getfile(random)) # random 모듈 위치(경로) 알려줌
print(inspect.getfile(thailand))

# 11-6. pip install - 패키지 설치 (https://pypi.org/) 
''' 설치 패키지)
1. pip install beautifulsoup4 # 터미널에 복붙

2. 터미널
   pip list - 현재 설치 패키지 확인
   pip show beautifulsoup4 - 패키지에 대한 정보 
   pip install -- upgrade beautifulsoup4 - 패키지 upgrade
   pip uninstall beautifulsoup4 - 패키지 삭제
'''

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 11-7. 내장함수 (따로 import 필요 없이 바로 사용가능)

# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수
print(dir())
import pickle # 외장 함수
print(dir())

print(dir(random)) 

lst = [1, 2, 3]
print(dir(lst))

name = "Jim"
print(dir(name))

# 11-8. 외장 함수

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능 
import os
print(os.getcwd()) # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder) # 폴더 삭제
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir()) # 현재 디렉토리에 파일, 폴더 정보

# time : 시간 관련 함수
import time
print(time.localtime()) 
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today()) # 오늘 날짜는  2021-05-12

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일후
