#1
from unittest import result
print("\n1. 홀수, 짝수 판별하기")

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
    
print(is_odd(5))        # True
print(is_odd(10))       # False

#2
print("\n2. 모든 입력의 평균값 구하기")

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))            # <class 'float'>
print(avg_numbers(1, 2, 3, 4, 5))

#3
'''
print("\n3. 프로그램 오류 수정")

input1 = int(input("num 1 : "))     # 입력값은 string으로 취급된다
input2 = int(input("num 2 : "))

total = input1 + input2
print(total)
'''

# 4
print("\n4. 출력 결과가 다른 것")

print("you" "need" "python")                # youneedpython
print("you"+"need"+"python")                # youneedpython
print("you", "need", "python")              # you need python
print("".join(["you", "need", "python"]))   # youneedpython

# 5
print("\n5. 프로그램 오류 수정 2")

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()      # << 닫아줌

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

# 6
print("\n6. 사용자 입력 저장하기")

'''
user_input = input("저장할 내용을 입력하세요: ")
f = open('test.txt', 'a')
f.write("\n")       # << 이렇게 해야 줄바꿈 되는 거 같은데...?
f.write(user_input)
f.close()
'''

# 7
print("\n7. 파일의 문자열 바꾸기")

f = open('text.txt', 'r')
body = f.read()
f.close()

body = body.replace("java", "python")

f = open('text.txt', 'w')
f.write(body)
f.close()

# 8
print("\n8. 입력값을 모두 더해 출력하기")

'''
import sys

args = sys.argv[1:]

result = 0

for i in args: result += int(i)
print(result)
'''