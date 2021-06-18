import time
from PIL import ImageGrab

# pip install Pillow >> PIL 파이썬 이미지 라이브러리 

time.sleep(5) # 5초 대기 : 사용자가 준비하는 시간

for i in range(1, 11): # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴 (스크린샷 찍음) >> img에 저장
    img.save("image{}.png".format(i)) # 파일로 저장 (image1.png ~ image10.png)
    time.sleep(2) # 2초 단위