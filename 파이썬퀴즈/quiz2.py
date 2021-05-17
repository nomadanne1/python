# Quiz2)

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
result = list("_"*i) 
print(result)
print("_"*i)

# 4. 사용자로부터 한글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct'출력 아니면 'Wrong'출력
input = input("input : ")
result = word.count(input)
if result == 0 :
    print("Wrong")
else :
    print("Correct")

# 5. 매번 입력을 받을 때마다 현재까지 맞힌 글자들을 표시 (맞히지 못한 글자는 밑줄 출력)
word_lst =list(word)
index_lst = list(filter(lambda e:word_lst[e] == input, range(len(word_lst))))

print(result(1))
i = 0
while len(word) > i :
    print(result[i])
    i += 1
    print(i)
print(result)




