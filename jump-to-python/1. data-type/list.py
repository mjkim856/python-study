# 리스트의 형태
a = list() # 빈 리스트 생성하기, 혹은 a = [] 로도 가능하다.
b = [1, 2, 'list', ['list', 'in', 'list']] 

print(b[0])         # 1
print(b[3])         # ['list', 'in', 'list']
print(b[3][1])      # in
print(type(b[0]))   # <class 'int'>
print(type(b[2]))   # <class 'str'>
print(type(b[3]))   # <class 'list'>

print(b[0] + b[1])          # 3
# print(b[1] + b[2])        TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 만약 다른 타입을 더하고 싶다면 아래와 같이 형변환을 해야 한다.
print(str(b[1]) + b[2])     # 2list
print()

# 리스트의 슬라이싱
c = [1, 2, 3, 4, 5]
print(c[0:2])       # [1, 2] idx 0 이상 2 미만
print(c[:2])        # [1, 2] idx 2 미만
print(c[2:])        # [3, 4, 5] idx 2 이상
print(b[3][:2])     # ['list', 'in']
print()

# 리스트 연산
d = [1, 2, 3]
e = [4, 5, 6]
print(d + e)        # [1, 2, 3, 4, 5, 6]
print(d * 3)        # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(len(d))       # 3
print()

# 리스트의 수정과 삭제
f = [1, 2, 3, 4, 5]
f[1] = 10
print(f)        # [1, 10, 3, 4, 5]

del f[1]
print(f)        # [1, 3, 4, 5]

del f[2:]
print(f)        # [1, 3]
print()

# 리스트 관련 함수