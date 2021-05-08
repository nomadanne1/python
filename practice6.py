# 8-1. 표준입출력

print("Python" , "Java") # Python Java
print("Python", "Java", sep=",") # Python,Java - sep="띄어쓰기 대신에 들어가는 값"
print("Python", "Java", sep=",", end="?") 
print("무엇이 더 재밌을까요?") # Python,Java?무엇이 더 재밌을까요? - end="마지막에 줄바꿈 대신에 들어가는 값"
print("Python")

# import sys
# print ("Python", "Java", file=sys.stdout) # stdout 표준출력 
# print ("Python", "Java", file=sys.stderr) # stderr 표준에러

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100} # 사전 {key : value}
for subject, score in scores.items(): # .items - key, value 쌍으로 출력
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4),sep=":") #ljust(칸) - (8칸을 확보하고)왼쪽정렬 , rjust(칸) - (4칸을 확보하고)오른쪽정렬
'''
수학      :   0
영어      :  50
코딩      : 100
'''

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) #.zfill(칸) 칸만큼의 공간을 확보하고 값이 없으면 0을 채운다

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer)) # 사용자 입력을 받으면 항상 String
# print("입력하신 값은 " + answer + "입니다.")

# 8-2. 다양한 출력포맷 -> ex) {0:^<+30,} 순서 외우기!

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) #       500 - : > (빈자리는 빈공간으로 두고, 오른쪽 정렬)
# print("{0: >10}".format(+500)) #      500
# print("{0: >10}".format(-500)) #      -500

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500)) #      +500
print("{0: >+10}".format(-500)) #      -500

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500)) #+500______

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000)) # 100,000,000

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000)) # +100,000,000
print("{0:+,}".format(-100000000)) # -100,000,000

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니깐 빈자리는^ 로 채워주기
print("{0:^<+30,}".format(100000000)) # +100,000,000^^^^^^^^^^^^^^^^^^

# 소수점 출력
print(5/3) # 1.6666666666666667
print("{0:f}".format(5/3)) # 1.666667

# 소수점 특정 자리수 까지만 표시 (소수점 3째자리에서 반올림)
print("{0:2f}".format(5/3))

# 8-3. 파일입출력
''' open("파일명","w/a/r", encoding="인코딩정보") 
* w : 쓰기전용,덮어쓰기 (write)
  a : 이어쓰기 (append) 
  r : 읽기전용 (read) 
'''
# write - 쓰기전용, 덮어쓰기
score_file = open("score.txt", "w", encoding="utf8") 
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # *열었으면 꼭 닫아줘야한다.

# append - 이어쓰기
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# read - 읽기전용 * .read() / .readline()
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # .read() - 모든내용 출력
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # readline() - 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # *print때문에 줄바꿈 한번 더 됨 -> , end=""
print(score_file.readline(), end="") 
print(score_file.readline(), end="") 
score_file.close

# 파일내용이 몇줄인지 모를때
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break # 반복문 탈출
    print(line, end="")
score_file.close()

# list에 값을 넣어서 처리 - .readlines()
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

# 8-4.pickle 
'''
import pickle / b : 바이너리
우리가 가지고 있는 데이터를 피클.dump을 이용해서 파일에 저장.
파일을 피클.load를 통해서 불러와서 변수에 저장해서 쓸수 있게 해주는 유용한 라이브러리
'''

import pickle

# write - pickle.dump()
profile_file = open("profile.pickle", "wb") # b - 바이너리 *피클을 쓰러면 항상 정의해줘야함
profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # ★profile에 있는 정보를 file에 저장
profile_file.close()

# read - pickle.load()
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # 파일에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

# 8-5. with 

# with & pickle 파일
import pickle

with open("profile.pickle", "rb") as profile_file: # close 해줄필요 없이 자동 종료
    print(pickle.load(profile_file))

# with & 일반파일
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

# 8-6. Quiz) 

# 내가 푼 방법
i = 1
while i <=50:
    with open(str(i)+"주차.txt", "w", encoding="utf8") as weekly_roport: 
        weekly_roport.write("- {0} 주차 주간 보고 - ".format(i))
        weekly_roport.write("\n부서 : ")
        weekly_roport.write("\n이름 : ")
        weekly_roport.write("\n업무 요약 : ")
    i += 1

# 나도코딩 문제풀이

for i in range(1, 51): 
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file: # *str(i)
        report_file.write("- {0} 주차 주간보고 - ".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")










