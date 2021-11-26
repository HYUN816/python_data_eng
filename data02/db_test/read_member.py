import db.dao as dao

id = input('검색할 id>>')

row = dao.read(id) # 튜플형태로 받음

print('------------------------')
print('결과는 ' + row[0] + " " + row[1] +" " + row[2] + " "+row[3])

# 모듈을 만들 때는 각자의 역할에 충실하도록, 역할을 섞어서 만들면 안된다.
# 응집도를 높게 만들어야
