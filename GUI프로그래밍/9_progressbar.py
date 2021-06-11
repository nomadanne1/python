import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # maximum=100 >> 100%,  mode="indeterminate" >> 결정되지 않음 (불확실한)
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # mode="determinate" >> (한정된)
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="중지", command=btncmd) 
# btn.pack()

p_var2= DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.001) # import time // 0.01 초 대기

        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get()) # 현재 % 출력 cf print(p_var2) >> PY_VAR0
        
        '''
        progressbar2.update()

        >> for문 동작 할때 마다 GUI 업데이트 
        >> 없을경우 동작 다 끝난다음에 한번에 보여줘서 바로 꽉차있음
        '''
btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()