# 9-1. 클래스

# 마린 : 공격 유닛, 군인. 총을 촐 수 있음
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쓸 수 있는데, 일반 모드 / 시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# tank1, 2, ... -> 클래스 (하나의 틀) - 연관있는 변수와 함수의 집합
''' 
class 클래스이름:

*self - 자기자신
클래스내에서 메소드 앞에 항상 self적어 줘야한디.
'''
# 일반 유닛
class Unit: 
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 하나의 클래스로 서로다른 마린1, 마린1, 탱크 생성 *전달값에 self빼고 전달 
marine1 = Unit("마린1", 40, 5)
marine2 = Unit("마린2", 40, 5)
tank = Unit("탱크", 150, 35)
# marine3 = Unit("마린") - 오류
# marine3 = Unit("마린". 40) - 오류

# 9-2. __init__ (생성자) - 객체 만들때 자동으로 호출.
# 객체 : ex) marine1, marine2, tank.. = Unit 클래스의 인스턴스

# 9-3. 멤버변수 - 클래스내에서 정의된 변수.
# ex) self.name, self.hp, self.damage...

# 레이스 : 공중 유닛, 비행, 클로킹 (상대방에게 보이지 않음) 
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 멤버변수 외부에서 쓸 쑤 있음

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)

# 객체에 추가로 외부에서 변수를 만들어서 사용가능.
# *wraith2.clocking(o), wraith1.clocking(x) -> 확장을 한 객체에만 적용됨)
wraith2.clocking = True 

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 9-4. 메소드

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage): # self 자기자신
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 9-5. 상속

# 일반 유닛
class Unit: 
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # *공격유닛은 일반유닛 상속을 받는다.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # ★부모클래스 초기화.
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 메딕 : 의무병 - 공격력없음.

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 9-6. 다중 상속 - 부모클래스가 둘 이상.

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 + 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # AttackUnit, Flyable 클래스 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage) # AttackUnit(부모클래스1) 초기화
        Flyable.__init__(self, flying_speed) # Flyable(부모클래스2) 초기화

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사. 
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) 
valkyrie.fly(valkyrie.name, "3시") # 발키리 : 3시 방향으로 날아갑니다. [속도 5]

# Unit > AttackUnit > FlyablAttackUnit, Flyable > FlyableAttackUnit

# 9-7. 메소드 오버라이딩 - 부모클래스 메소드를 자식클래스에서 재정의

# 일반 유닛
class Unit: 
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): 
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) 
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 + 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): 
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed) 

    def move(self, location): # 부모클래스 move() 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")

# 9-8. pass

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 일단넘어가 

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.pass
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

# 9-9. super

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super() - *self는 없이 사용.
        location = self.location

# *super() - 다중상속할때 문제발생!

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# ★ 두개이상 다중 상속시 super()사용하면 맨처음에 상속받는 클래스만 생성자 호출
# -> super()사용하지 말고 따로 명시적으로 상속클래스.__init__로 초기화 해줘야한다.

# 드랍쉽 - 수송만가능 (공격x)
dropship = FlyableUnit()  
