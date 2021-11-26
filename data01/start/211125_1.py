# 문제풀이 2번
x = int(input('숫자1>>')) #"300"
y = int(input('숫자2>>')) #"100"
sum = str(x+y) + '입니다.'
# +연산자 = 타입이 다르면 연결할 수 없다.
print(sum)

# 문제풀이 7
# list = [] / 가변길이 / linked list / python list의 특징
buy=[]
wish=list()

for _ in range(0,5) :
    #0~4번
    # _ : index이용안할 때
    buy.append(input('사고 싶은 것>>'))
print(buy)

# c언어 방식
for i in range(0,5) :
    print(buy[i])

# for-each 방식
for e in buy :
    print(e)


# 클래스 만들기
class Phone :
    # 부품(객체 object)을 만들기 위해서는 틀이 필요
    # 틀 = class (부류)
    # 공통적으로 가지는 특성(성질)을 가지고 틀을 만들어야 함
    # 전화기 만의 공통적인 성질로 틀을 만들어 보자

    # 공통적인 성질 : 특성, 속성 (property, attribute) => 멤버변수
    color = None
    ram = 0

    # 객체 생성시 자동호출 함수 : 생성자 함수
    def __init__(self, c, r):
        # 내장된 함수 : __붙는다
        self.color = c
        self.ram = r

    # 공통적인 동작 : 기능(function) => 멤버함수
    def call(self):
        #self : class를 의미(phone) / 다른 언어에서는 this라는 키워드 사용
        print('전화하다.')

    def game(self):
        print('게임하다.')

    def __str__(self):
        # 주소 대신에 주소가 가르키고 있는 멤버 변수의 값을 출력(프린트)
        return self.color + ' ' + str(self.ram)


# 실제 사용 : 틀을 찍어낸다
# myPhone = Phone()
# yourPhone=Phone()
myPhone = Phone('red', 256) #객체생성
yourPhone = Phone('blue', 128)

#멤버변수와 멤버함수는 객체 생성 후 사용할 수 있다.

# 컴퓨터의 흐름 : 동적인 모든 것 =cpu
# 26분 다시
# cpu는 ram에 넣었다가 빼는 방식을 취하고 있다

# 주소 print
# 해시값 = unique 15분 다시
print('주소>>', myPhone)
print('주소>>', yourPhone)

myPhone.color = 'red'
print(myPhone.color)
# . : 접근 연산자
# None : 주소가 아직 안들어와있다.
yourPhone.color = 'blue'
print(yourPhone.color)
# => init(생성자) 을 만들자

# 대문자로 시작하고 () 있다면 -> 객체를 생성한 것

# 오버라이딩
# 오버로딩 : 파이선에서 지원하지 않는다.


#확인문제 -중급 풀이

    # 클래스의 인스턴스 = object
    # 인스턴스 =?
    # 부품을 언제 만드는가?

