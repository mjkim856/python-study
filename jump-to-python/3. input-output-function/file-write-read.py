# 파일 생성하기

'''
# w 쓰기, r 읽기, a 파일의 마지막에 내용 추가하기
f = open("파이썬실습파일", 'w')
# f = open("C:/doit/파이썬실습파일.txt", 'w')   # 이렇게 디렉터리 지정해서 할 수도 있음
f.close()       # 자동으로 close되지만 명시적으로 닫아주는 것 추천

f = open("doit.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''

f = open("doit.txt", 'r')
print(type(f))          # _io.TextIOWrapper

while True:
    line = f.readline()
    # print(type(line))   # str
    if not line: break
    print(line)
f.close()
  
'''
1번째 줄입니다.

2번째 줄입니다.

3번째 줄입니다.

...

이렇게 출력되는데, 줄 끝에 \n 문자가 있어서 빈 줄도 같이 출력된다고 함. 
'''

f = open("doit.txt", 'r')
lines = f.readlines()
# print(type(lines))      # list
for line in lines:
    line = line.strip()     # 이렇게 .strip() 사용하면 줄 바꿈 문자 \n을 제거해 준다
    print(line)
f.close()