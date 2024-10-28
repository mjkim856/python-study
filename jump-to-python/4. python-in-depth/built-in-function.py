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
# 출력
# (0, 'a')
# (1, 'b')
# (2, 'c')
print()

print("eval : 문자열로 된 표현식을 입력으로 받아 => 해당 문자열을 실행한 결과값을 리턴")
print(eval('1+2'))           # 3
print(eval('divmod(4, 3)'))  # (1, 1)
print(eval('1+2*3'))         # 7
print(eval("'hi' + 'ai'"))   # hiai
print()

print("filter : filter(함수, 반복_가능한_데이터)\n반복 가능한 요소 순서대로 함수 호출시 리턴값이 True인 것만 걸러내 묶어 리턴한다.")
print("예시1 : filter 미사용 - 양수값만 리턴하는 함수")
def positive1(li):
    result = []
    for i in li:
        if i > 0:
            result.append(i)
    return result

print(positive1([-1, 2, -3, 4, 0])) # [2, 4]

print("\n예시2 : filter 사용 - 양수값만 리턴하는 함수")
def positive2(i):
    return i > 0

print(list(filter(positive2, ([-1, 2, -3, 4, 0])))) # [2, 4]

print("\n예시3 : filter + lambda 사용 - 양수값만 리턴하는 함수")
print(list(filter(lambda x: x > 0, [-1, 2, -3, 4, 0])))

print("\nlambda 예시") # lambda 설명을 따로 올리지 않은 거 같아 여기에 추가...
addl = lambda a, b: a+b
print(addl(1, 2)) # 3
