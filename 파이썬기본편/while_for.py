# while : 반복 횟수가 명확하지 않을 떄
# for : 반복 횟수가 명확할 때

# >> while문

'''
while 조건식 :
    실행문장
    실행문장
'''

# Q1. while문을 사용해서 "파이썬 최고!!"를 13번 출력하시오

num = 1
while num <=13:
    print("파이썬 최고!!")
    num += 1

# >> break - 반복문을 나가는 기능

number = 1
while True:
    print(number)
    number += 1
    if number > 3:
        break

# Q2. 두개의 정수를 입력 받아서 더 하는 코드를 작성하시오.
# (단, 두개의 정수가 0이 들어올 때 까지 반복한다.)

while True:
    a = int(input("첫 번째 정수 입력 >> "))
    b = int(input("두 번째 정수 입력 >> "))
    if a == 0 and b== 0:
        break
    
    print("두 정수의 합 : ", a+b)

# >> for문
# 문자열 또는 리스트 또는 튜플이 들어갔을 때 
# 안에 있는 요소를 하나씩 반복
'''
for 변수 in 문자열 (or 리스트 or 튜플) :
    print(변수)
'''

# for문 예시1 (문자열)
hi = "안녕하세요"
for s in hi:
    print(s)

'''
안
녕
하
세
요

'''

# for문 예시2 (리스트)
list_food = ["햄버거", "치킨", "피자"]
for food in list_food:
    print(food)

'''
햄버거
치킨
피자
'''

# for문 예시3 (튜플)
tuple_food = ("햄버거", "치킨", "피자")
for food in tuple_food:
    print(food)

'''
햄버거
치킨
피자
'''

# Q1. 5명에 대한 정보처리사 자격증 시험 점수가 리스트에 담겨있습니다.
# 이때 각 점수가 함격 졈수인지 불합격 점수인지 판별하여 출력하시오 (60점 이상 함격)

score_list = [90, 45, 70, 60, 55]
number = 1
for score in score_list:
    if score >= 60:
        result = "합격"
    else:
        result = "불합격"
    print("{0}번 학생은 {1}입니다".format(number,result))
    number += 1

# >> for문 range() 사용하기

'''
range() 함수 사용
- 필요한 만큼의 숫자를 만들어내는 유용한 기능

- range(시작할 숫자, 종료할 숫자, 증가량)
- range(1, 10, 1) -> 1부터 9까지 1씩 증가 >> [1,2,3,4,5,6,7,8,9] 
- range(1, 100, 3) -> 1부터 99까지 3씩 증가
- range(10, 1, -1) -> 10부터 2까지 1씩 감소 (-1씩 증가)

- range(기본값0, 종료할숫자, 기본값1)
- range(3, 10) -> 3부터 9까지 1씩증가
- range(10) -> 0부터 9까지 1씩 증가 >> *10번반복
'''

# Q1. for문을 이용하여 97부터 77까지 출력하시오.
for i in range(97, 76, -1):
    print(i, end=" ")

# Q2. for문을 이용하여 23부터 40까지 출력하시오
for i in range(23, 41): 
    print(i, end=" ")

# ★ 
list1 = [[1,2],[3,4],[5,6]]
for i in list1:
    print(i) 
'''
[1, 2]
[3, 4]
[5, 6]
'''

list1 = [[1,2],[3,4],[5,6]]
for i, j in list1:
    print(i)
    print(j)
'''
1
2
3
4
5
6
'''

# >> 반복문 예제

# 랜덤으로 1부터 50사이의 숫자를 뽑으면 뽑은 숫자를 맞추는 Up, Down게임 예제
from random import *
# import random

answer = randint(1, 50) # 1 ~ 50 사이의 숫자 랜덤 추출
print("정답 :",answer)
while True:
    num = int(input("숫자를 입력하세요 >> "))
    if num < answer :
        print("{}보다 큰 수 입니다.".format(num))
    elif num > answer :
        print("{}보다 작은 수 입니다.".format(num))
    else:
        print("정답을 맞추셨습니다.")
        break

# 두개의 정수를 키보드로 입력 받아 첫 번째 정수부터 두 번째 정수까지
# 출력되는 소스코드를 작성하시오

start = int(input("start >> "))
end = int(input("end >> "))
for i in range(start, end+1):
    print(i, end=" ")

# Q1. 1부터 100사이의 숫자 중 3의 배수인 값들의 합을 출력하세요
sum = 0
for i in range(1, 101):
    if i%3 ==0 :
        sum +=i
print(sum)

# Q2. for문을 이용하여 구구단 2단을 출력하시오.
for i in range(1,10):
    result = 2*i
    print(" 2 * {} = {}".format(i, result))

# 숫자를 입력 받고 입력 받은 숫자의 약수를 구하시오
# (약수란 어떤 수를 나누어 떨어지게 하는 수)
num = int(input("정수 입력 >> "))
print("약수 : ", end="")
for i in range(1, num+1):
    if num%i == 0:
        print(i, end=" ")