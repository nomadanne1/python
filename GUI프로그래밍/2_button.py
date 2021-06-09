from tkinter import *

root = Tk() 
root.title("Nado GUI")

btn1 = Button(root, text="버튼1") # text
btn1.pack() # pank()

btn2 = Button(root, padx=5, pady=10, text="버튼2") # padx: 좌우여백, pday: 상하여백
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # width, height (고정된 크기)
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # fg: 글자색, bg: 배경색
btn5.pack()

photo = PhotoImage(file="GUI프로그래밍/img.png")
btn6 = Button(root, image=photo) # image
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd) # command
btn7.pack()

root.mainloop()