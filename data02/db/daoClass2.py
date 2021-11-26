import pymysql

class DAO():
    def __init__(self):
        # db connection
        self.conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='*tld5rk1vhfm',
                               db='cloth',
                               charset='utf8')
        print('1. db연결 성공', self.conn)

        # 접근권한
        self.cur = self.conn.cursor()
        print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', self.cur)

    def create(self, data):
        sql = "insert into diary(writeday, title, content) values(%s,%s,%s)"
        # sql = insert into diary values(null, ~~)
        # writeday datetime으로 썼을 때
        # sql = "insert into diary(writeday, title, content) values(now(),%s,%s)"

        result = self.cur.execute(sql, data)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과 값>>', result)

        # 22분 다시 /반영시키기
        self.conn.commit()
        self.conn.close()

    def update(self,data):
        # sql
        sql = "update diary set writeday=%s, title=%s, content=%s where id = %s"
        result = self.cur.execute(sql, data)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과 값>>', result)

        self.conn.commit()
        self.conn.close()

    def read(self,id):
        # sql
        sql = "select * from diary where id=%s"
        result = self.cur.execute(sql, id)

        row = self.cur.fetchone()
        print(row)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과 값>>', result)

        self.conn.commit()
        self.conn.close()

        return row

    def read_all(self):

        # sql
        sql = "select * from diary"
        result = self.cur.execute(sql)

        # 스트림안에 갖혀있는 걸 꺼내자!
        # but 출력된 내용은 다른 모듈에 만들어야한다 / 모듈 역할을 따로따로(입력,출력, 처리...)
        rows = self.cur.fetchall() #fetchmany : sizing가능
        print(len(rows))
        print(rows)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과 값>>', result)

        self.conn.commit()
        self.conn.close()

        return rows

    def delete(self,id):

        # sql
        sql = "delete from diary where id=%s"
        result = self.cur.execute(sql, id)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과 값>>', result)

        self.conn.commit()
        self.conn.close()

if __name__ =='__main__' :
    dao = DAO()
    dao.create([test,test,test,test])