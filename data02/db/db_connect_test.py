# interface : 함수들의 묶음, class의 묶음, 프로그램 사용

import pymysql

# db 연결
conn = pymysql.connect(host='localhost', port=3306, user='root',
                       password='*tld5rk1vhfm', db='cloth', charset='utf8')
                        # python의 default 문법 host = '', 'localhost'도 가능
                        # but 좀더 명확히 해주고 싶어서 =사용

# int, str 함수 cpu에서 ~~

print('db연결 성공', conn)

