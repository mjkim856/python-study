# 내장함수

print("1. abs() : 절댓값 리턴")
print(abs(-10)) # 10
print(abs(1.2)) # 1.2
print()

print("2. all() : 모든 요소가 참이면 트루, 아니면 false")
print(all([1, 2, 3])) # True
print(all([0]))       # False
print()

print("3. any() : 하나라도 참이면 트루, 모두 거짓이면 false")
print(any([1, 2, 3, 0]))    # True
print(any([]))              # False
print()

print("4. chr : 유니코드 => 문자")
print(chr(97))      # a
print(chr(44032))   # 가
print()

print("5. dir() : 객체가 지닌 변수나 함수를 보여줌")
print(dir([1, 2, 3])) # ['__add__', '__class__', '__class_getitem__' ...
print(dir({'1':'a'})) # ['__class__', '__class_getitem__', '__contains__', ...
print()

print("6. divmod : a, b의 몫과 나머지 리턴")
print(divmod(7, 3)) # (2, 1)
print()

print("7. enumerate : 열거하다, 순서가 있는 데이터를 받아 인덱스값을 포함하는 enumerate 객체 리턴\n보통 for문과 함께 쓴다.")
for i in enumerate(['a', 'b', 'c']):
    print(i)
# 출력
# (0, 'a')
# (1, 'b')
# (2, 'c')
print()

print("8. eval : 문자열로 된 표현식을 입력으로 받아 => 해당 문자열을 실행한 결과값을 리턴")
print(eval('1+2'))           # 3
print(eval('divmod(4, 3)'))  # (1, 1)
print(eval('1+2*3'))         # 7
print(eval("'hi' + 'ai'"))   # hiai
print()

print("9. filter : filter(함수, 반복_가능한_데이터)\n반복 가능한 요소 순서대로 함수 호출시 리턴값이 True인 것만 걸러내 묶어 리턴한다.")
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
# print(filter(lambda x: x > 0, [-1, 2, -3, 4, 0]))     >> <filter object at 0x1005e1490> 이게 출력되네???

print("\nlambda 예시") # lambda 설명을 따로 올리지 않은 거 같아 여기에 추가...
addl = lambda a, b: a+b
print(addl(1, 2)) # 3
print()

print("10. hex : 10진수 => 16진수 변경해주는 함수")
print(hex(255)) # 0xff
print()

print("11. id : 객체의 고유 주소값 (레퍼런스) 반환하는 함수")
a = 3
b = a
c = 3
print(id(a))    # 4343196016
print(id(b))    # 4343196016
print(id(3))    # 4343196016
print(id(c))    # 4343196016
print()

print("12. input() : 사용자 입력값 입력받는 함수")
print()

print("13. int : 문자열 / 소수 형태의 숫자를 정수로 리턴하는 함수")
print(int(3.0))
print(int("3"))
print

print("14. isinstance(object, class) : 객체가 클래스의 인스턴스인지를 참 거짓으로 판별한다.")
class istrue: pass
a = istrue()
print(isinstance(a, istrue)) # True
print(isinstance(b, istrue)) # False
print()

print("15. len: 입력값 길이(요소의 총 개수) 리턴하는 함수")
print("16. list: 반복 가능한 데이터를 리스트로 만드는 함수 (리스트 입력하면 똑같은 리스트 복사해 리턴)")
print(list("whatislistfunction"))        # ['w', 'h', 'a', 't', 'i', 's', 'l', 'i', 's', 't', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n']
print(len(list("whatislistfunction")))   # 18
print()

print("17. map(함수, 반복_가능한_데이터): 입력받은 반복 가능한 데이터에 함수를 적용한 결과를 리턴한다.")
print("코테 진행시 아래와 같은 코드 많이 사용했던 듯. input으로 입력받은 띄어쓰기가 있는 두 숫자를 int 함수를 사용해 적용하는 것")
# print(list(map(int, input().split())))
print()

print("18. max : 최대값 리턴하는 함수")
print("19. min : 최솟값 리턴하는 함수")
print((max([1, 2, 3])))
print((min([1, 2, 3])))
print(max('abcde'))  # e
print()

print("20. oct : 10진수 => 8진수 변경해주는 함수")
print(oct(1))        # 0o1
print()

print("21. open(filename, [mode]): 파일 이름과 읽기 방법을 입력받아 파일 객체 리턴\n기본 모드는 읽기(r)")
print("22. ord : 문자의 유니코드 값을 리턴하는 함수")
print(ord('a'))      # 97
print()

print("23. pow : x의 y값을 리턴하는 함수")
print(pow(2, 3))     # 8
print()

print("24. range : 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴하는 함수")
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(5, 0, -1)))    # [5, 4, 3, 2, 1]
print()

print("25. round : 숫자 입력받아 반올림하는 함수이다.")
print(round(3.12345))           # 3
print(round(3.12345, 2))        # 3.12
print()

print("26. sorted : 입력 데이터를 정렬하고 결과를 리스트로 리턴한다. \n리스트 자료형의 sort 함수는 정렬만 하고 결과를 리턴하진 않는다.")
print(sorted('dbghcfeac'))      # ['a', 'b', 'c', 'c', 'd', 'e', 'f', 'g', 'h']
print()

print("27. str : 입력값을 문자열로 만들어 리턴하는 함수")
print(str(3))           # '3'
print()

print("28. sum : 반복 가능한 데이터의 합을 리턴하는 함수") 
print(sum([1, 2, 3]))   # 6
print()

print("29. type(object) : 입력값의 자료형을 리턴하는 함수")
print("30. tuple(iterable) : 반복 가능한 데이터를 튜플로 바꾸어 리턴하는 함수")
print()

print("31. zip(iterable) : 동일한 개수로 이루어진 데이터를 묶어서 리턴")
print(list(zip([1, 2, 3], [4, 5, 6]))) # [(1, 4), (2, 5), (3, 6)]







