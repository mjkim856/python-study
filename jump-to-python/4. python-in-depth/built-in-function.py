# 내장함수

print("abs() : 절댓값 리턴")
print(abs(-10)) # 10
print(abs(1.2)) # 1.2
print()

print("all() : 모든 요소가 참이면 트루, 아니면 false")
print(all([1, 2, 3])) # True
print(all([0]))       # False
print()

print("any() : 하나라도 참이면 트루, 모두 거짓이면 false")
print(any([1, 2, 3, 0]))    # True
print(any([]))              # False
print()

print("chr : 유니코드 => 문자")
print(chr(97))      # a
print(chr(44032))   # 가
print()

print("dir() : 객체가 지닌 변수나 함수를 보여줌")
print(dir([1, 2, 3])) # ['__add__', '__class__', '__class_getitem__' ...
print(dir({'1':'a'})) # ['__class__', '__class_getitem__', '__contains__', ...
print()

print("divmod : a, b의 몫과 나머지 리턴")
print(divmod(7, 3)) # (2, 1)
print()

print("enumerate : 열거하다, 순서가 있는 데이터를 받아 인덱스값을 포함하는 enumerate 객체 리턴\n보통 for문과 함께 쓴다.")
for i in enumerate(['a', 'b', 'c']):
    print(i)
print()