# 문제1
id = input('아이디를 입력해주세요 : ')
name = input('이름을 입력해주세요 : ')

print(f'아이디가 {id}인 {name}님이 로그인되었습니다.')

# 문제2
num1 = int(input('숫자1 : '))
num2 = int(input('숫자2 : '))

print('---------------------')
print(f'두 수의 합은 {num1+num2}')
print(f'두 수의 차은 {abs(num1-num2)}')
print(f'두 수의 곱은 {num1*num2}')
print(f'두 수의 나눗셈은 {num1/num2}')
print(f'나누고나서의 나머지는 {num1%num2}')

# 문제3
name = input('이름 : ')
age = int(input('나이 : '))

print(f'홍길동님의 10년 후의 나이는 {age+10}세입니다')

# 문제4
money = int(input('엄마 용돈 주세요 : '))
if money>10000 :
    print('엄마 용돈이 너무 많아요.')
else :
    print('엄마 용돈이 너무 적어요')

# 문제5
num3 = int(input('숫자를 입력하세요 : '))
if num3%2==0 :
    print('짝수입니다.')
else :
    print('홀수입니다.')

# 문제6
profit = int(input('실적을 입력하세요 : '))
if profit > 1000 :
    print('축하합니다. 실적을 달성하셨습니다.!')
    print(f'당신의 이번달 보너스는 {profit*0.2}만원입니다.')

# 문제7
buy =[]
for i in range(5) :
    want=input('사고싶은것 : ')
    buy.append(want)
print(buy)

# 문제8
wish= input('입력 : ')
wish = wish.split(',')
for i in wish :
    print(f'나는 {i}가 되고 싶어요!')

# 확인문제-중급(상속)
class Car :
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
    def run(self):
        print(self.speed)
    def start(self):
        print(self.color)

class Truck(Car) :
    def load(self):
        pass

Car1 = Car('red',11)
print(Car1.color)
print(Car1.speed)
Car1.run()
Car1.start()

Truck1 = Truck('blue', 20)
print(Truck1.color)
print(Truck1.speed)
Truck1.load()
Truck1.run()
Truck1.start()

# 확인문제 - 중급
class Member:
    def __init__(self,id,pw,grade,mileage):
        self.id = id
        self.pw = pw
        self.grade = grade
        self.mileage = mileage

users=[]
for _ in range(3):
    a= input('회원정보 입력').split(',')
    users.append(Member(a[0],a[1],a[2],a[3]))

mileage_sum = 0
for i in users:
    mileage_sum += int(i.mileage)

print(f'{users[0].id}의 비밀번호는 {users[0].pw}입니다')
print(f'{users[1].id}는 {users[1].grade}이고, 마일리지는 {users[1].mileage}입니다')
print(f'총 마일리지는 {mileage_sum}입니다')
print(f'총 마일리지는 {round(mileage_sum/len(users))}입니다')