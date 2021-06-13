from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set 이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32): # 1 ~ 31
    listbox.insert(END, str(i) + "일") # 1일, 2일, ...
listbox.pack(side="right")

# ★ 정상적인 스크롤바 동작해줌.
scrollbar.config(command=listbox.yview)

root.mainloop()