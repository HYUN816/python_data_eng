import db.dao as dao

id = input('id>>')
pw = input('pw>>')
name = input('name>>')
tel = input('tel>>')

# 추후에 수정하기 좋기 때문에 append 방식을 더 많이 사용한다.
mem_list=[id,pw,name,tel]
print(mem_list)

# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value object, VO)
# list 형태로 만들어서 전달 하는 경우가 많다

# db_test.dao.create(id, pw, name, tel)
dao.create(mem_list)

# 입력부분, 처리부분, 결과부분 세가지 부분으로 나눌 수 있다.