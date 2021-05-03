# 4-1. 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""

print(sentence3)

# 4-2. 슬라이싱 (필요한정보만 잘라서 가져옴)
jumin = "990120-1234567"

print("성별 : " + jumin[7]) # 인덱스는 0부터시작
print("연 : " + jumin[0:2]) # ★ 0 부터 2 직전까지 (0 , 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨뒤에서 7번째부터 끝까지 *맨뒤 인덱스 -1

# 4-3. 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # python is amazing
print(python.upper()) # PYTHON IS AMAZING
print(python[0].isupper()) # True
print(len(python)) # 문자열 길이 (공백포함)
print(python.replace("Python", "Java")) # Java is Amazing

index = python.index("n") # 문자열 n이 위치한 인덱스 알려줌.
print(index)
index = python.index("n" , index + 1) # 위에서 찾은 index 이후부터 n이 위치한 인덱스 알려줌
print(index)

print(python.find("n")) # 문자열 n이 위치한 인덱스 알려줌. 
# * find와 index 다른점 - find는 찾는 문자열이 없으면 -1반환 index는 컴파일에러

print(python.count("n")) # 문자열 n이 몇번 등장하나 

# 4-4. 문자열 포맷
print("a" + "b")
print("a", "b")

# 방법 1 - % 사용
print("나는 %d살입니다." % 20) # %d - 정수
print("나는 %s을 좋아해요." % "파이썬") # %s - 문자열
print("Apple 은 %c로 시작해요." % "A") # %c - 단일문자
# %s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2 - {} 사용
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))

# 방법 4 (v3.6 이상 ~)
age = 20 
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 4-5. 탈출문자

# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다.
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\nomad\\Desktop\\PythonWorkspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # 커서를 맨앞으로 이동해서 *덮어쓴다

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple

# \t : 탭
print("Red\tApple")

# 4-6. Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 내가 푼 방법 *정수형 str로 감싸주는것 까먹지 말자 !!
site = "http://naver.com"
index = site.index(".")
pw_ = site[7:index]
pw= pw_[:3]+str(len(pw_))+str(pw_.count("e"))+"!"

print("생성된 비밀번호 : "+pw)

# 나도코딩 문제풀이
# url = "http://naver.com"
url = "http://youtube.com"
my_str = url.replace("http://","") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2
# my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다." .format(url, password))

