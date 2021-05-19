import requests
# res = requests.get("http://naver.com") # url정보 가져와서 res변수에 담는다.
res = requests.get("https://blog.naver.com/dddaegaed") 
print("응답코드 : ", res.status_code) # 200 : 정상, 403 : 접근권한없음

# # 방법1
# if res.status_code == requests.codes.ok: # requests.codes.ok => 200
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

# # 방법2
# res.raise_for_status() # 문제가 생기면 오류를 내뱉고 바로 프로그램 종료.
# print("웹 스크래핑을 진행합니다")

#################################################

res = requests.get("https://www.google.com/") 
res.raise_for_status()
# -> ★ 두줄은 항상 같이쓴다.

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)