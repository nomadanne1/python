from tkinter import *

root = Tk() 
root.title("Nado GUI")
root.geometry("640x480") 

txt = Text(root, width=40, height=5) # Text() - 텍스트 위젯 생성
txt.pack()
txt.insert(END, "글자를 입력하세요") # insert(index, chars)

e = Entry(root, width=30) # Entry()
e.pack()

e.insert(0, "한 줄만 입력해요") # cf. 현재는 값이 비어있기때문에 0대신 END를 써도 동일.

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # .get("1.0", END) >> txt 처음부터 끝까지 가져옴 *1 : 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END) # insert 할때 '0'넣었기 때문에 >> 0

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() 