# 1
print("\n1. 클래스 상속받고 메서드 추가하기 - 1")

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

# 위 클래스를 상속하는 UpgradedCalculator 클래스 생성 후 minus 메서드 추가하기
class UpgradedCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradedCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# 2
print("\n2. 클래스 상속받고 메서드 추가하기 - 2")
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if (self.value > 100): self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# 3
print("\n3. 참과 거짓 예측하기")
print(all([1, 2, abs(-3)-3]))   # False, 3-3 = 0으로 처리되어서 그런 듯?
print(chr(ord('a')) == 'a')     # True

# 4
print("\n4. 음수 제거하기")
print(list(filter(lambda x: x>0, [1, -2, 3, -5, 8, -3])))

# 5
print("\n5. 16진수 => 10진수로 변경")
print(int('0xff', 16))  # 아하!!
print(int(0xff))        # 255

# 6
print("\n6. 리스트 항목마다 3 곱해서 리턴하기")
print(list(map(lambda x: x*3, [1, 2, 3, 4])))

# 7
print("\n7. 최댓값과 최솟값의 합")
li = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(li) + min(li))    # -1

# 8
print("\n8. 소수점 반올림하기")
print(round(17/3, 4))       # 5.6667

# 9
print("\n9. 디렉터리 이동하고 파일 목록 출력하기")
import os
print(os.system("ls"))
# file1.txt file3.txt file4.txt ...

# 10
print("\n10. 파일 확장자가 .py인 파일만 찾기")
import glob
print(glob.glob("/Users/mjk/git_python/*.py"))

# 11
print("\n11. 날짜 표시하기")
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))   # 2024/10/31 14:38:40

# 12
print("\n12. 로또 번호 출력하기")
import random

for i in range(6):
    print(random.randint(1, 45))        # 아항항 잘못 적음... 중복됨

# 12-1
print("\n12-1. 로또 번호 출력하기") 


# 12-2
print("\n12-2. 로또 번호 출력하기")  
print(sorted(random.sample(range(1,46),6)))

# 13
print("\n13. 누나는 연상")
import datetime
d1 = datetime.date(1995, 11, 20)
d2 = datetime.date(1998, 10, 6)
print((d2 - d1).days)   # 1051일

# 14
print("\n14. 데이타 순으로 정렬하기")
from operator import itemgetter
data = [('b', 14.1), ('박', 11.1), ('우', 16.1), ('양', 16.1), ('강', 124.1), 
        ('이', 13.4), ('a', 14.1), ('미', 34.1), ('가', 154.1), ('이', 14.12)]

print(sorted(data, key=itemgetter(1)))
# [('박', 11.1), ('이', 13.4), ('b', 14.1), ('a', 14.1), ('이', 14.12),
# ('우', 16.1), ('양', 16.1), ('미', 34.1), ('강', 124.1), ('가', 154.1)]

# 15
print("\n15. 청소 당번 두 명 구하기")
import itertools
dang = ['당1', '당2', '당3', '당4']
print(len(list(itertools.combinations(dang, 2))))   # 6     이것도 잘못 푼 듯? ㅋㅋㅋㅋㅋㅋㅋㅋ
print(list(itertools.combinations(dang, 2)))        
# >> 이케 나와야 함! [('당1', '당2'), ('당1', '당3'), ('당1', '당4'), ('당2', '당3'), ('당2', '당4'), ('당3', '당4')]

# 16
print("\n16. 문자열 경우의 수 나열하기")
print(list(itertools.permutations("abcd", 4)))
# 아 근데... 이것도 잘못 푼 듯 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 다 합쳐야 한다? 고 한? 다?
'''
[('a', 'b', 'c', 'd'), ('a', 'b', 'd', 'c'), ('a', 'c', 'b', 'd'), ('a', 'c', 'd', 'b'), 
('a', 'd', 'b', 'c'), ('a', 'd', 'c', 'b'), ('b', 'a', 'c', 'd'), ('b', 'a', 'd', 'c'), 
('b', 'c', 'a', 'd'), ('b', 'c', 'd', 'a'), ('b', 'd', 'a', 'c'), ('b', 'd', 'c', 'a'), 
('c', 'a', 'b', 'd'), ('c', 'a', 'd', 'b'), ('c', 'b', 'a', 'd'), ('c', 'b', 'd', 'a'), 
('c', 'd', 'a', 'b'), ('c', 'd', 'b', 'a'), ('d', 'a', 'b', 'c'), ('d', 'a', 'c', 'b'), 
('d', 'b', 'a', 'c'), ('d', 'b', 'c', 'a'), ('d', 'c', 'a', 'b'), ('d', 'c', 'b', 'a')]
'''

# 17
print("\n17. 5명에게 할일 부여하기")        # 이거 출력을 l2로만 ... 
import random
l1 = ['1번', '2번', '3번', '4번', '5번']
l2 = ['청소', '빨래', '설거지', '휴식', '휴식']
random.shuffle(l1)

print(list(itertools.zip_longest(l1, l2)))

# 18
print("\n18. 벽에 타일 구하기")
import math

min = math.gcd(200, 80)
all = 200*80
print(all//(min*min))

# https://docs.python.org/3/library/math.html
# 함수 내부를 직접 보는 건 어려운 거 같기도 하고... 

