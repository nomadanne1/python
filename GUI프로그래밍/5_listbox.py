from tkinter import *

root = Tk() 
root.title("Nado GUI")
root.geometry("640x480")

'''
selectmode >> extended : 여러개 선택, single : 하나만 선택 
height=0 >> 0으로 설정하면 리스트가 포함한 크기 만큼 보여줌, 1.2.3... n : n개의 항목만큼 보인다
'''
listbox = Listbox(root, selectmode="extended", height=0) 
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") # END 가장 맨 뒤에 값을 넣어줌
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # # 삭제
    listbox.delete(END) # 맨 뒤 항목을 삭제
    listbox.delete(0) # 맨 앞 항목을 삭제

    # 갯수 확인
    print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    print("1번째 부터 3번째 까지의 항목 : ", listbox.get(0,2)) # 0, 1, 2 인덱스 항목 출력

    # # 선택된 항목 확인 (위치로 반환 ex. (1, 2, 3))
    # print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() 