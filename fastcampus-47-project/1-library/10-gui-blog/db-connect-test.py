import sqlite3

conn = sqlite3.connect('blog.db')

# 테이블 생성
c = conn.cursor()  # 커서 생성
c.execute('''CREATE TABLE blog (id integer PRIMARY KEY, subject text, content text, date text)''')

# 데이터 입력
# 커밋해야 데이터 입력이 완료됨
c.execute("INSERT INTO blog VALUES (1, '첫 번째 블로그', '첫 번째 작성글입니다.', '20221022')")
conn.commit()

c.execute("INSERT INTO blog VALUES (2, '두 번째 블로그', '두 번째 작성글입니다.', '20221022')")
conn.commit()

c.execute("INSERT INTO blog VALUES (3, '세 번째 블로그', '세 번째 작성글입니다.', '20221022')")
conn.commit()

# 데이터 조회
c.execute('SELECT * FROM blog')
all = c.fetchall()
print(all)

# DB 접속 종료
conn.close()