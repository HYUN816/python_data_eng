import db.daoClass2 as dao

writeday = input('writeday>>')
title = input('title>>')
content = input('content>>')

diary=list()
diary.append(writeday)
diary.append(title)
diary.append(content)

dao2 = dao.DAO()
dao2.create(diary)

