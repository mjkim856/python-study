# sys 모듈 사용하여 프로그램에 인수 전달 가능
'''
doit.py 라는 파일 안에 아래의 식을 기재했다.

import sys

args = sys.argv[1:]    
for i in args:
    print(i)
'''    

# 실행 결과
'''
>> 아래는 오류 발생
python doit.py aaa bbb ccc
zsh: command not found: python

>> python3 으로 사용해야 함
python3  doit.py   aaa  bbb  ccc    
 sys모듈  프로그램(?) 인수1 인수2 인수3       

 aaa
bbb
ccc
'''