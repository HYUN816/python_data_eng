import db.dao as dao

rows = dao.read_all()

print('------------------------')

# for i in range(0,len(rows)) :
#     print(rows[i])

# 아래 코드를 더 선호
# for one in rows :
#     print(one)

for row in rows :
    print('결과는 ' + row[0] + " " + row[1] + " " + row[2] + " " + row[3])

# 모듈을 만들 때는 각자의 역할에 충실하도록, 역할을 섞어서 만들면 안된다.
# 응집도를 높게 만들어야
