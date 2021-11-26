import db.daoClass2 as dao

id = int(input('검색할 id>>'))

dao2 = dao.DAO()
row = dao2.read(id) # 튜플형태로 받음

print('------------------------')
print('결과는 ' + str(row[0]) + " " + row[1] +" " + row[2] + " "+row[3])

