# 10-1. 예외처리
'''
    try:
        (실행문장)

    except ValueError:
        (오류발생시 실행문장)
'''
try:
    print("나누기 전용 계산기 입니다.")
    nums = [] # 리스트
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # ZeroDivisionError - 0으로 나눌때 발생하는 에러
    print(err)
except Exception as err: # ValueError, ZoroDivisionError 제외 나머지 모든 에러 처리
    print("알 수 없는 에러가 발생하였습니다.")
    print(err) 

# 10-2. 에러 발생시키기(의도적으로) - raise

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError # raise 의도적 에러 생성
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# 10-3. 사용자 정의 예외처리

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # BigNumberError(msg) - 사용자 정의 에러 발생
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)

# 10-4. finally - 예외 발생하든 안하든 무조건 실행

finally: 
    print("계산기를 이용해 주셔서 감사합니다.")

# 10-5. Quiz)

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#          출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량을 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다." 

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작
while(True):

    try: 
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if( order > chicken) : # 남은 치킨보다 주문량이 많을때
            print("재료가 부족합니다.")
        elif(order <= 0): # 조건1
            raise ValueError 
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -= order  
        if chicken == 0: # 조건2
            raise SoldOutError
    except ValueError: 
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break # 프로그램종료 (while문 탈출)
