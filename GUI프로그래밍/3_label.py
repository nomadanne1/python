from tkinter import *

root = Tk() 
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="GUI프로그래밍/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요") # config >> 값 변경

    global photo2 # ★ 함수 내에서 레이블에 이미지 변경하려면 전역변수 설정 꼭 해줘야한다!!
    photo2 = PhotoImage(file="GUI프로그래밍/img2.png")
    label2.config(image=photo2)

'''
global photo2 전역변수 설정 안했을경우 
>> 이미지 변경 안됨 why??
>> 전역변수 설정 해줘야 GC이 쓰레기 줍지 않음.
>> *Garbage Collection : 불필요한 메모리 공간 해제
'''
btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()


