# 파이썬 함수의 기본 구조
# 입력값 있고, 리턴값 있다
def add(a, b):          # 여기는 매개변수!      >> 책에서는 입력값으로 통일
    return a + b        # 책에서는 리턴값으로 통일

a = 1
b = 2
c = add(a, b)           # 여기는 인수!

print(c)

# 입력값이 없는 함수
def say():
    return "Hi"

d = say()

print(d)

# 리턴값이 없는 함수
def add2(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add2(3, 4)
print(add2(3, 4))        # 리턴값이 없으므로 None이 출력

'''
print(add2(3, 4))
>>  3, 4의 합은 7입니다.
    None
    ^ 이렇게 출력되길래 챗지피티에 물어봄

이 코드를 실행하면 다음과 같은 출력이 나타납니다:

1. add2(3, 4) 함수가 호출되면, 함수 내부에서 print() 문이 실행됩니다. 
이 부분에서는 3, 4의 합은 7입니다.라는 문자열이 출력됩니다.

2. 그 후, print(add2(3, 4))가 실행되는데, add2() 함수는 값을 반환(return) 하지 않으므로, 파이썬에서는 암묵적으로 None이 반환됩니다. 
이 때문에 최종적으로 print(None)이 호출됩니다.

아하!
'''

# 입력값도 리턴값도 없는 함수
def say():
    print("Hi")

say()
print(say())        # 리턴값이 없으므로 None이 출력

# 매개변수 지정한 함수
def sub(a, b):
    return a - b

result = sub(a = 5, b = 8)
print(result)

result = sub(b = 5, a = 8)      # << 이렇게 순서 변경하는 것도 가능
print(result)

print()
print("여러개의 입력값을 받는 함수")

# 여러개의 입력값을 받는 함수 - 1
def add_many(*args):        # arg는 관례적 이름이며, 다른 이름 사용해도 됨. (약간 for문의 i 느낌인 듯) 튜플이 된다. 
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1, 2, 3, 4, 5)) # 15
print(add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # 55

# 여러개의 입력값을 받는 함수 - 2
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul("add", 1, 2, 3, 4, 5)) # 15
print(add_mul("mul", 1, 2, 3, 4, 5)) # 120

# 키워드 매개변수
def print_kwargs(**kwargs):         # 딕셔너리가 된다. key=value 형태로 저장됨. 포인트는 kwarg가 아닌 ** 두 개 사용하는 것
    print(kwargs)

print_kwargs(a = 1) # {'a': 1}
print_kwargs(b = 'animal', c = 3) # {'b': 'animal', 'c': 3}

print()
print("함수의 결과값은 언제나 하나")

# 함수의 결과값은 언제나 하나!
def add_and_mul(a, b):
    return a + b, a * b     # 이 경우, (a + b, a * b)로 이루어진 튜플을 리턴하게 된다. 
  # return a - b            # 위의 리턴문 실행 후 리턴값을 돌려주고 함수를 빠져나간다. 즉, 아래의 리턴문은 실행되지 않는다. 

result = add_and_mul(3, 7)
result1, result2 = add_and_mul(3, 7)

print(result)       # (10, 21)
print(result1)      # 10
print(result2)      # 21

# return 사용하여 함수 빠져나가기
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)

print(say_nick("보바"))
print(say_nick("바보"))

print()
print("매개변수에 초깃값 설정하기")

def say_myself(name, age, man=True):
    print("내 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

# 람다로 하면 이렇게 할 수 있어요
say_myself1 = lambda name, age, man=True: print("내 이름은 %s 입니다." % name, 
                                                "나이는 %d살 입니다." % age, 
                                                ("남자입니다." if man else "여자입니다.")
                                                )

# def sey_myself(name, man=True, age):
    # 주의 : 위의 형식과 같이 초기값이 있는 변수를 초기값이 없는 변수 앞에 사용할 수 없음 !! 

say_myself("ann", 14) # 남
say_myself("bump", 23, False) # 여
say_myself1("cory", 23, True) # 남

print()
print("함수에서 선언한 변수의 효력 범위")

v = 1

def vartest(v):
    v = v + 1
    return v

print(vartest(v))   # 2
print(v)            # 1
# 만약 위의 v = 1 을 선언하지 않았다면 NameError: name 'v' is not defined가 발생한다. 
# v는 함수 안에서 선언되었기 떄문이다.

# x를 사용하기 위한 방법은 두 가지이다.
# 1. return 사용하기
def vartest1(x):
    x = x + 1
    return x

x = vartest1(1)     # 여기 x는 vartest1의 x와 다름
print(x)

# 2. global 명령어 사용하기 : 외부 변수에 종속되기에 좋은 방식은 아니다
y = 10
def vartest2():
    global y
    y = y + 1
    return y

vartest2()
print(y)

print()
print("Lambda 예약어")

# def와 동일한 역할이지만, 함수를 간결하게 만들 때 사용한다.
# 함수명 = lambda 매개변수: 표현식
add2 = lambda a, b: a + b

def add1(a, b):
    return a + b

print(add1(3, 4))       # 7
print(add2(3, 4))       # 7
