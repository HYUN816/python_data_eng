import db.daoClass2 as dao


dao2 = dao.DAO()
rows = dao2.read_all()

print('------------------------')

for row in rows :
    print('결과는 ' + str(row[0]) + " " + row[1] + " " + row[2] + " " + row[3])

