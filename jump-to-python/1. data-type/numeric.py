# 아래와 같이 사용
a = 1
b = 2.3
c = 4.24E10     # 출력시 42400000000.0
d = a + b       # 3.3
e = b + c       # 42400000002.3
f = a + c       # 42400000001.0

print(d)
print(e)
print(f)
print()

# 연산자
a = 10
b = 5

# 더하기, 빼기, 곱하기, 나누기, a의 b 제곱 
# 만약 b가 정수인 경우 a + b = 15 이다.
# 만약 b가 소수인 경우 a + b = 15.0 이다.
print(a + b)
print(a - b)
print(a * b)
print(a / b)        # 2.0
print(a ** b)
print()

# a/b의 몫, a/b의 나머지
print(a // b)
print(a % b)