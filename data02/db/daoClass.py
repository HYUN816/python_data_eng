import pymysql

# 대문자로 사용할 수 있는 경우 : class명, 상수
class DAO():
    def __init__(self):
        # 클래스 안의 함수에서 반복되는 내용을 넣어준다.
        pass
    def create(self, data):

        # db connection
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='*tld5rk1vhfm',
                               db='cloth',
                               charset='utf8')
        print('1. db연결 성공', conn)

        # 접근권한
        cur = conn.cursor()
        print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

        # sql
        # sql = "insert into member values('" + id + "','" + pw + "','" + name + "','" + tel + "')"
        # sql = "insert into member values('"+ data[0] +"','"+ data[1] +"','"+ data[2] +"','"+ data[3] +"')"
        # result = cur.execute(sql)

        # 아래 코드가 속도가 제일 빠르다
        # 모든 sql문의 결과는 int값이다.
        sql = "insert into member values(%s,%s,%s,%s)"
        result = cur.execute(sql, data)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과 값>>', result)

        # 22분 다시 /반영시키기
        conn.commit()
        conn.close()

    def update(self,data):
        # db connection
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='*tld5rk1vhfm',
                               db='cloth',
                               charset='utf8')
        print('1. db연결 성공', conn)

        # 접근권한
        cur = conn.cursor()
        print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

        # sql
        sql = "update member set pw=%s,tel=%s where id = %s"
        result = cur.execute(sql, data)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과 값>>', result)

        conn.commit()
        conn.close()

    def read(self,id):
        # db connection
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='*tld5rk1vhfm',
                               db='cloth',
                               charset='utf8')
        print('1. db연결 성공', conn)

        # 접근권한
        cur = conn.cursor()
        print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

        # sql
        sql = "select * from member where id=%s"
        result = cur.execute(sql, id)

        # 스트림안에 갖혀있는 걸 꺼내자!
        # but 출력된 내용은 다른 모듈에 만들어야한다 / 모듈 역할을 따로따로(입력,출력, 처리...)
        row = cur.fetchone()
        print(row)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과 값>>', result)

        conn.commit()
        conn.close()

        # return은 제일 마지막에
        return row #튜플형태로 반환

    def read_all(self):
        # db connection
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='*tld5rk1vhfm',
                               db='cloth',
                               charset='utf8')
        print('1. db연결 성공', conn)

        # 접근권한
        cur = conn.cursor()
        print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

        # sql
        sql = "select * from member"
        result = cur.execute(sql)

        # 스트림안에 갖혀있는 걸 꺼내자!
        # but 출력된 내용은 다른 모듈에 만들어야한다 / 모듈 역할을 따로따로(입력,출력, 처리...)
        rows = cur.fetchall() #fetchmany : sizing가능
        print(len(rows))
        print(rows)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과 값>>', result)

        conn.commit()
        conn.close()

        # return은 제일 마지막에
        return rows #튜플형태로 반환

    def delete(self,data):
        # db connection
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='*tld5rk1vhfm',
                               db='cloth',
                               charset='utf8')
        print('1. db연결 성공', conn)

        # 접근권한
        cur = conn.cursor()
        print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

        # sql
        sql = "delete from member where id=%s"
        result = cur.execute(sql, data)
        print('3. sql문을 만들어서 mysql로 보낸 후 결과 값>>', result)

        conn.commit()
        conn.close()

if __name__ =='__main__' :
    dao = DAO()
    dao.create([test,test,test,test])