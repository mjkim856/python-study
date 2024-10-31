# 표준 라이브러리
print("=====[1. import datetime]======")
import datetime
day1 = datetime.date(2024, 10, 29)
day2 = datetime.date(2024, 10, 25)
dayy = day1 - day2
print(dayy) # 4 days, 0:00:00 (반대면 -4일)
print(dayy.days) # 4

print(datetime.datetime.now())  # 2024-10-31 15:16:11.939999

print("\n요일 확인법")
print(day1.weekday())       # 0 월요일, 1 화요일, 2 수요일 ... 
print(day1.isoweekday())    # 1 월요일, 2 화요일, 3 수요일 ... 

print()

print("=====[2. import time]=========")
import time
print(time.time())                  # 1730213186.2682922
print(time.localtime(time.time()))  # time.struct_time(tm_year=2024, tm_mon=10, tm_mday=29, tm_hour=23, tm_min=46, tm_sec=26, tm_wday=1, tm_yday=303, tm_isdst=0)
print(time.asctime(time.localtime(time.time())))    # Tue Oct 29 23:46:26 2024       입력받은 튜플 time.localtime 형태의 값을 알아보기 쉬운 형태로 리턴
print(time.ctime())                 # Tue Oct 29 23:46:26 2024       항상 현재 시간만을 반환
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  #  2024-10-29 23:46:26

# for i in range(5):      # 1초에 한 번 출력
#     print(i)
#     time.sleep(1)

print()

print("=====[2. import math]=========")
import math
print(math.gcd(60, 100, 80))       # 20, 최대공약수 출력
print(math.lcm(60, 100, 80))       # 1200, 최소공배수 출력

print()

print("=====[3. import random]========")
import random
print(random.random())   # 0.7063754302294685 // 0.0 ~ 1.0 사이의 실수 출력
print(random.randint(1, 100))   # 53 // 1 ~ 100 사이의 실수 출력

print()

print("=====[4. import itertools]=====")
import itertools
# zip 함수와 똑같이 동작하나, zip_longest()는 긴 객체의 길이에 맞춘다.
zip1 = ['a', 'b', 'c' , 'd', 'e']
zip2 = [1, 2, 3]

print(list(itertools.zip_longest(zip1, zip2)))
# [('a', 1), ('b', 2), ('c', 3), ('d', None), ('e', None)]

print(list(itertools.permutations([1, 2, 3], 2))) 
# 순열 리턴, [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

print(list(itertools.combinations([1, 2, 3], 2))) 
# [(1, 2), (1, 3), (2, 3)]
# 겹친 거 리턴 안 함

print()

print("=====[5. import functools]=====")
import functools

data1 = [1, 2, 3, 4, 5]
result1 = functools.reduce(lambda x, y: x + y, data1)
print(result1)  # 15

# 람다가 익숙하지 않아서 그런지 잘 이해가 가지 않아서 람다 없는 reduce()로 변경해봄
def ex_reduce(a, b):
    return a + b

result2 = functools.reduce(ex_reduce, data1)

print(result2)  # 15

# 최댓값 구하기
max = functools.reduce(lambda x, y: x if x > y else y, data1)
print(max)  # 5

print()

print("=====[6. import itemgetter]====")
from operator import itemgetter

student = [
    ('jane', 54, "a"),
    ('mike', 12, "n"),
    ('tom', 43, "a")
]
print(sorted(student, key=itemgetter(1)))   # [1] 번째 요소를 기준으로 정렬
# [('mike', 12, 'n'), ('tom', 43, 'a'), ('jane', 54, 'a')]

student = [
    {"name": "jane", "age": 22, "grade": "a"},
    {"name": "mike", "age": 24, "grade": "n"},
    {"name": "tom", "age": 56, "grade": "a"}
]
print(sorted(student, key=itemgetter('age')))   # age 요소를 기준으로 정렬
#[{'name': 'jane', 'age': 22, 'grade': 'a'}, {'name': 'mike', 'age': 24, 'grade': 'n'}, {'name': 'tom', 'age': 56, 'grade': 'a'}]

print()

print("=====[7. import shutil]========")
# 파일을 이동하거나 복사할 때 사용하는 모듈이다.
import shutil
# shutil.copy("file1.txt", "file3.txt")   # file1.txt의 내용이 file3.txt으로 복사된다.
# shutil.move("file5.txt", "file4.txt")   # file5.txt의 내용이 file4.txt로 복사되고, file5.txt는 삭제된다.

print()

print("=====[8. import glob]==========")
import glob
print(glob.glob("/Users/mjk/git_python/*"))
# 디렉터리 안의 파일을 읽어서 리턴
# ['/Users/mjk/git_python/file3.txt', '/Users/mjk/git_python/file1.txt', ... ]

print()

print("=====[9. import pickle]========")
import pickle
# 객체의 상태를 그대로 유지하며 파일에 저장하고 불러올 수 있게 한다.
# f = open("test.txt", "wb")
# pickle.dump(data, f)
# f = open("test.txt", "rb")
# pickle.load(f)

print()

print("=====[10. import os]===========")
import os
# 추가 함수는 책 참고
print(os.environ)           # environ({'__CFBundleIdentifier': 'com.microsoft.VSCode' ... })
print(os.environ['PATH'])   # /usr/local/bin:/System/ ... 

print()

print("=====[11. import zipfile]=====")
import zipfile
# 여러 개의 파일을 zip 형식으로 합치거나 해제할 때 사용한다.

print()

print("=====[11. import threading]=====")
import threading
# 스레드 객체를 사용해 동시 작업을 가능하게 해준다.
# 스레드 생성 >> t = threading.Thread(target=long_task)
# 스레드 종료될때까지 기다리게 하기 = t.join()

print()

print("=====[11. import tempfile]=====")
# 임시 파일 만들어 사용하는 용도의 모듈
import tempfile
print(tempfile.mktemp())        # 이름만 반환, /var/folders/52/mltn2wv97fxf6g7j2d0k0c8h0000gn/T/tmpkl2s74pd
f = tempfile.TemporaryFile()    # 임시 저장 공간으로 사용할 파일 객체 리턴
f.close()                       # 파일 삭제됨

print()

print("=====[12. import traceback]====")
# 프로그램 실행 중 발생한 오류를 추적하고자 할 때 사용하는 모듈
import traceback

def a():
    return 1/0

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")
        print(traceback.format_exc())

main()

'''
Traceback (most recent call last):
  File "/Users/mzc01-mjk/git_python/python-study/jump-to-python/4. python-in-depth/standard-library.py", line 172, in main
    b()
  File "/Users/mzc01-mjk/git_python/python-study/jump-to-python/4. python-in-depth/standard-library.py", line 168, in b
    a()
  File "/Users/mzc01-mjk/git_python/python-study/jump-to-python/4. python-in-depth/standard-library.py", line 165, in a
    return 1/0
ZeroDivisionError: division by zero
'''

print()

print("=====[14. import json]=========")
import json

# 기존 json 파일을 파이썬에서 처리할 수 있도록 딕셔너리 자료형으로 리턴
with open('test.json', 'r') as f:
    json_data = json.load(f)

print(json_data)    # {'name': 'nnname', 'birth': '0525', 'age': 30}

# 딕셔너리 자료형을 JSON으로 변경
json_data1 = {'name': '파이썬', 'birth': '0222', 'age': 22}
with open('test.json', 'w') as f:
    json.dump(json_data1, f)

json_data2 = json.dumps(json_data1)
print(json_data2)               # {"name": "\ud30c\uc774\uc36c", "birth": "0222", "age": 22}
print(json.loads(json_data2))   # {'name': '파이썬', 'birth': '0222', 'age': 22}

print(json.dumps(json_data1, indent=2, ensure_ascii=False))
# {
#   "name": "파이썬",
#   "birth": "0222",
#   "age": 22
# }

print("import urllib.request를 사용해서 URL을 호출할 수 있다.\nurllib.request.urlopen(   )")

print()

print("=====[15. import webbrowser]===")
print("파이썬 프로그램에서 시스템 브라우저를 호출할 때 사용한다.")
import webbrowser

# webbrowser.open_new("google.com")


