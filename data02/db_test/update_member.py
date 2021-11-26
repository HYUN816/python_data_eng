import db.dao as dao

id = input('id>>')
pw = input('pw>>')
tel = input('tel>>')

mem_list=list()
mem_list.append(pw)
mem_list.append(tel)
mem_list.append(id)

dao.update(mem_list)

