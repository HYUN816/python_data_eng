import db.daoClass2 as dao

diary=[]
id = int(input('id>>'))
writeday = input('writeday>>')
title = input('title>>')
content = input('content>>')

diary.append(writeday)
diary.append(title)
diary.append(content)
diary.append(id)

dao2 = dao.DAO()
dao2.update(diary)


