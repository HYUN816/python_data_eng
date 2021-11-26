import db.dao as dao

id = input('id>>')

# 메모리상으로는 낭비 하지만 통일성 부여
mem_list=[id]

dao.delete(mem_list)
