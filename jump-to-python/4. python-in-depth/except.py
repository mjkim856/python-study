# try-execpt문
# try: ... except ...                   오류 발생하면 except 블록 실행
# try: ... except 발생오류: ...           오류 발생시 except에 정해둔 오류와 동일한 경우에만 except 블록 실행
# try: ... except 발생오류 as 변수         오류 발생시 오류의 내용까지 알고 싶은 경우

try: 
    4/0
except ZeroDivisionError as e: 
    print(e)        # division by zero

# try-finally문
# 오류 여부와 관계 없이 항상 수행된다. 보통 사용한 리소스를 close해야 할 때 사용한다.
try:
    f = open('어쩌구', 'w')
finally:
    f.close()

# 여러 개의 오류 처리하기
try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
# except (ZeroDivisionError, IndexError) as e:      << 이렇게 하면 한번에 처리할 수 있음

# try-else문
# 오류가 없을 때만 else절이 수행된다. 
try:
    age = int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else: 
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

# 오류 회피하기
'''
try:
    어쩌구
except 발생오류:
    pass
'''

# 오류 발생시키기   >>   raise
# 만약 부모 클래소를 상속받는 자식 클래스는 반드시 특정 함수를 구현하도록 하고 싶다면 아래와 같이 구현한다.
'''
class 부모
    def 필수(self):
        raise NotImplementedError

class 자식(부모):
    def 필수(self):
        print('구현 안 하면 오류 발생')
'''

# 예외 만들기
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 이름입니다."  # 오류 메세지를 출력했을 때 보이게 하려면 __str__을 사용해서 구현해야 한다.

def say_name(name):
    if name == "aaa":
        raise MyError()
    print(name)

say_name("bbb")     
# say_name("aaa") # in say_name raise MyError()

try:
    say_name("bbb")
    say_name("aaa")
except MyError as e:
    print(e)