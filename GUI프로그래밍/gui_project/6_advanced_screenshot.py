'''
키보드 pip install keyboard 
: 사용자가 키 입력을 하면 
  키 값을 받아서 처리 할 수 있는것 
  => 후킹
'''
import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2020년 6월 1일 1시 20분 30초 -> _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab(curr_time)
    img.save("image{}.png".format(curr_time)) # ex) image_20200601_102030

keyboard.add_hotkey("F9", screenshot) # 사용자가 F9 키를 누르면 스크린 샷 저장
keyboard.add_hotkey("a", screenshot) # 사용자가 'a' 키를 누르면 스크린 샷 저장
keyboard.add_hotkey("ctrl+shift+s", screenshot) # 사용자가 'ctrl + shift + s'를 누르면 스크린 샷 저장

keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행