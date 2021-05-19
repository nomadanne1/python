# # Quiz3)

# # 내가 푼 방법

# for seat in range(1, 21):
#     if (seat%2) == 1 :
#         print("A{0}".format(seat), end=" ")

# # 나도코딩 문제풀이

# for i in range( 1, 21):
#     if i % 2 == 1: # i 를 2로 나눈 나머지
#         print("A" + str(i), end=" ")

# tip. 1, 2, 3, 4, 5, 6, 7, ..., 20
for i in range(1, 21)[::2]: # 2 칸씩 건너 뛰어서
    print("A" + str(i), end= " ")


        

        