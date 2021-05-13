# 분기 - 이런상황에서는 이런코드 저런상황에서는 저런코드 사용
# 6-1. if
'''if 조건 : 
    실행 명령문
'''

weather = input("오늘 날씨는 어때요? ") # input() - 입력받은값 *String형태로 변수에 저장된다.
if weather == "비" or weather == "눈" :
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else :
    print("준비물 필요 없어요.")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요") 

# 6-2. for - 반복문 1

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# print("대기번호 : 5")

for waiting_no in [1, 2, 3, 4, 5]: # list내에 값들이 하나씩 변수에 들어간다. 
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5): # 0, 1, 2, 3, 4 *0에서 5직전까지
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6): # 1, 2, 3, 4, 5 *1에서 6직전까지
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# 6-3. while - 반복문 
'''while 조건: *조건이 만족하지 않을때까지 계속 실행.
    실행할 문장
''' 

customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨" # - 무한루프 *ctrl + c - 강제종료
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1

customer = "토르"
person = "Unknown"
while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

# 6-4. continue 와 break *반복문에서 사용

absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if student in absent:
        continue # 더이상 실행 하지 않고 다음 반복으로 넘어간다.
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(no_book))
        break # 반복문 탈출
    print("{0}, 책을 읽어봐".format(student))

# 6-5. 한줄 for

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# 6-6. Quiz) 카카오 택시기사님이 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객의 수를 구하는 프로그램을 작성하시오.
# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다. 

# 내가 푼 방법
from random import*

sum = 0
for guest in range(1, 51):
 time = randint(5, 50)
 if 5 <= time <=15:
     print("[o] {0}번째 손님 (소요시간 : {1}분)".format(guest, time))
     sum += 1
 else:
     print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(guest, time))
print("총 탑승 승객 : {0} 분".format(sum))

# 나도코딩 문제풀이
from random import* 
cnt = 0 # 총 탑승 승객수
for i in range (1, 51): # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 쇼요시간
    if 5 <= time <= 15:
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))