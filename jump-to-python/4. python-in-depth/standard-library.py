# 표준 라이브러리
print("=====[1. import datetime]======")
import datetime
day1 = datetime.date(2024, 10, 29)
day2 = datetime.date(2024, 10, 25)
dayy = day1 - day2
print(dayy) # 4 days, 0:00:00 (반대면 -4일)
print(dayy.days) # 4

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

print()

print("=====[5. import functools]=====")

print()

print("=====[6. import itemgetter]====")

print()

print("=====[7. import shutil]========")

print()

print("=====[8. import glob]==========")
print()


print("=====[9. import pickle]========")

print()

print("=====[10. import os]===========")

print()


print("=====[11. import tempfile]=====")

print()

print("=====[12. import trackback]====")

print()

print("=====[13. import datetime]=====")
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


