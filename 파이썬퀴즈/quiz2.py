# Quiz2) 행맨 게임(영어 단어 퀴즈) 프로그램을 만드시오

# 내가 푼 방법

# 1. 리스트에 3개 이상의 단어를 추가
lst = ["apple", "banana", "orange"]

# 2. 위 리스트에서 랜덤을 1개의 단어를 선택
from random import *
shuffle(lst)
word_ = sample(lst,1)
word = ''.join(word_) # ★list-> str

# 3. 단어의 길이에 맞게 밑줄 출력
print("word : "+word)
i =len(word)
print("_"*i)
under_lst = list("_"*i) # 밑줄 str -> list

# # 4. 사용자로부터 한글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct'출력 아니면 'Wrong'출력
# input = input("input : ")
# cnt = word.count(input)
# if cnt == 0 :
#     print("Wrong")
# else :
#     print("Correct")

# # 5. 매번 입력을 받을 때마다 현재까지 맞힌 글자들을 표시 (맞히지 못한 글자는 밑줄 출력)
# word_lst =list(word)
# index_lst = list(filter(lambda e:word_lst[e] == input, range(len(word_lst))))
# print(index_lst)
# i = 0
# while len(index_lst) > i :
#     j = index_lst[i]
#     under_lst[j] = input    
#     i += 1
# print(''.join(under_lst))

# 4 && 5
while True :
    input_ = input("input : ")
    cnt = word.count(input_)

    if cnt == 0 :
        print("Wrong")
    else :
        print("Correct")
        word_lst =list(word) 
        # word_lst에 입력받은 문자와 일치하는 list 인덱스 index_lst에 list로 저장.
        index_lst = list(filter(lambda e:word_lst[e] == input_, range(len(word_lst))))
        
        i = 0
        while len(index_lst) > i :
            j = index_lst[i]
            under_lst[j] = input_   
            i += 1
        
        hangman =''.join(under_lst)
        print(hangman)

        # 6. 정답을 맞히면 Success 출력후 프로그램 종료
        if hangman.count("_") == 0 :
            print("Success")
            break 

# 나도코딩 문제풀이

from random import*
words = ["apple", "banana", "orange"]
word = choice(words) # choice() - list에서 rancom으로 가져옴. -> shuffle + sample
print("answer : " + word)
letters = "" # 사용자로부터 지금까지 입력받은 모든 알파벳 (보관)

while True:
    succeed = True
    
    for w in word: # ex) a p p l e
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()
    
    if succeed :
        print("Success")
        break

    letter = input("Input letter > ") # 사용자 입력 받기
    if letter not in letters : 
        letters += letter

    if letter in word :
        print("Correct")
    else :
        print("Wrong")


