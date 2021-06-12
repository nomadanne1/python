import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    if response == 1: # 재시도
        print("재시도")
    elif response == 0: # 취소
        print("취소")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n 저장 후 프로그램을 종료하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답:", response) # True, False, None -> 예 1, 아니오 0, 그 외
    if response == 1: # 네, ok
        print("예")
    elif response == 0: # 아니오
        print("아니오")
    else:
        print("취소")

'''
각 자료형 리스트, 문자열들의 
True, False 기준이 있는데 정리를 한번 해보겠습니다.

""	빈 문자열	False
" "	공백만 있는 문자열	False
"abc"	값이 있는 문자열	True
[]	빈 리스트	False
[1, 2]	값이 있는 리스트	True
1	숫자 1	True
0	숫자 0	False
-1	숫자 -1	True
{}	비어있는 딕셔너리	False
()	비어있는 튜플	False

숫자는 0이 아닌 모든숫자는 True 이고, 딱 0만 False 입니다.
비어있는 리스트, 튜플, 딕셔너리, 문자열은 모두 False 입니다.

출처: https://blockdmask.tistory.com/460 [개발자 지망생]
'''

Button(root, command=info, text="알림").pack() # msgbox.showinfo()
Button(root, command=warn, text="경고").pack() # msgbox.showwarning()
Button(root, command=error, text="에러").pack() # msgbox.showerror()

Button(root, command=okcancel, text="확인 취소").pack() # msgbox.askokcancel()
Button(root, command=retrycancel, text="재시도 취소").pack() # msgbox.askretrycancel()
Button(root, command=yesno, text="예 아니오").pack() # msgbox.askyesno() 
Button(root, command=yesnocancel, text="예 아니오 취소").pack() # msgbox.askyesnocancel()

root.mainloop()