# 5-1. 리스트 [] - 순서를 가지는 객체의 집합

# 지히철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway) # [10, 20, 30]

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가? - index
print(subway.index("조세호")) # 1

# 하하가 다음 정류장에서 다음 칸에 탐 - append
subway.append("하하")
print(subway) # ['유재석', '조세호', '박명수', '하하'] 

# 정형돈을 유재석 / 조세호 사이에 태워봄 - insert
subway.insert(1, "정형돈") # ['유재석', '정형돈', '조세호', '박명수', '하하']
print(subway)

# 지하철에 있는 사람을 한 명씩 '뒤'에서 꺼냄 - pop
print(subway.pop()) # 하하
print(subway) # ['유재석', '정형돈', '조세호', '박명수'] 

print(subway.pop()) # 박명수
print(subway) # ['유재석', '정형돈', '조세호']

# 같은 이름의 사람이 몇명 있는지 확인 - count
subway.append("유재석")
print(subway) # ['유재석', '정형돈', '조세호', '유재석'] 
print(subway.count("유재석")) # 2

# 정렬도 가능 - sort
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집기 가능 - reverse
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기 - clear
num_list.clear()
print(num_list) # []

# 다양한 자료령과 함께 사용 가능
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list) # ['조세호', 20, True]

# 리스트 확장 - extend
num_list.extend(mix_list)
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True]

# 5-2. 사전 {key : value} 
'''
1. 키는 키에 해당하는 사물함만 열 수 있다.
2. 키는 중복이 안된다 

'''

cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

print(cabinet.get(3))  # 유재석
# print(cabinet[5]) - 값이 없는 경우 -> 오류 발생
print(cabinet.get(5)) # 값이 없는 경우 -> None 
print(cabinet.get(5), "사용 가능 ") # 값이 없는 경우 출력할 값 지정 가능

# in을 이용해서 사전안에 값이 있는지 확인
print(3 in cabinet) # True 
print(5 in cabinet) # False

# key값 문자열도 가능
cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

# 새 손님
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국" # - 이미 있으면 update(덮어씀)
cabinet["C-20"] = "조세호" # - 없으면 새로 insert
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님 - del
del cabinet["A-3"]
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

# key 들만 출력 - keys
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# value 들만 출력 - values
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력 - items
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점 - clear
cabinet.clear()
print(cabinet) # {}

# 5-3. 튜플 () - *내용변경이나 추가 불가능 -> 대신 속도가  'list' 보다 빠르다

menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

# menu.add("생선까스") - 추가 불가능

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

# ★튜플 사용 -  한번에 값을 선언할수 있다.
# name, age, hobby = "김종국", 20, "코딩" - *괄호 안써도 되긴함
(name, age, hobby) = ("김종국", 20, "코딩") 
print(name, age, hobby)

# 5-4. 집합(set) {}
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}
  
# set정의 방법 - 2가지
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python) # {'양세형', '박명수', '유재석', '김태호'} 
print(java.union(python)) # {'양세형', '박명수', '유재석', '김태호'}

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python) # {'김태호', '양세형'}
print(java.difference(python)) # {'김태호', '양세형'}

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python) # {'유재석', '박명수', '김태호'}

# java 를 잊었어요
java.remove("김태호")
print(java) # {'양세형', '유재석'}

# 5-5. 자료구조의 변형
menu = {"커피", "우유", "커피"}
print(menu, type(menu)) # {'커피', '우유'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['커피', '우유'] <class 'list'>

menu = tuple(menu) # ('우유', '커피') <class 'tuple'>
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu)) # {'우유', '커피'} <class 'set'>

# 5-6. Quiz) 1~20 댓글중 1명은 치킨, 3명은 커피쿠폰 (중복불가)
# * random모듈의 shuffle 과 sample 을 활용
#
# (활용예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst) # [1, 2, 3, 4, 5]
# shuffle(lst) - 무작위로 순서 변경
# print(lst) 
# print(sample(lst, 1)) - lst중에서 1개를 무작위로 뽑겠다.
# print(sample(lst, 2)) - lst중에서 2개를 무작위로 뽑겠다.

# 내가 푼 방법
from random import*
re = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(re)
win = sample(re,4)
# print("치킨 당첨자 :", win.pop())
# print("커피 당첨자 :", win)
print("치킨 당첨자 : "+str(win.pop()))
print("커피 당첨자 : "+str(win))

# ★ 나도코딩 문제풀이   
users = range(1, 21) # 1부터 20까지 숫자 생성
# print(type(users)) - <class 'range'>
users = list(users)
# print(type(users)) - <class 'list'>

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명중 한명은 치킨, 3명은 커피
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 --")












