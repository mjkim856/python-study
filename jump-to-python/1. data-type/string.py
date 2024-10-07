# 파이썬에서 문자열 만드는 법
print("큰따옴표 사용")
print('작은따옴표 사용')
print("""큰따옴표 3개 연속 사용""")
print('''작은따옴표 3개 연속 사용''')
print()

# 문자열 안에 작따 / 큰따 포함시키는 법
print("'Hello, world!'")
print('"Hello, world!"')
print("\"Hello\'s world!\"")

print()
print("문자열 줄 바꿈은 \n\\n을 사용합니다.")
print('''혹은 이와 같이
\''' 혹은 \"""을 사용할 수 있습니다.''')
print()

# 문자열 연산
a = "aaa"
b = "bbb"
print(a + b)
print(a * 3)
print("a" * 3)
print(len(a)) # 문자열 길이 구하기
print()

# 문자열 인덱싱과 슬라이싱
a = "Life is too short, You need Python"
print(a[3]) # e
print(a[-1]) # n
print(a[-2]) # o
print(a[0] + a[1] + a[2] + a[3]) # Life
print(a[0:4]) # Life
              # 0, 1, 2, 3 포함
print(a[-11:-5]) # need P
print(a[1:]) # ife is too short, You need Python (1 포함)
print(a[:-1]) # Life is too short, You need Pytho (-1 미포함)
print(a[:]) # Life is too short, You need Python
print(a[:18]) # Life is too short,
print(a[18:]) #  You need Python 
print()

# 문자열 포매팅
print("I eat %d apples." % 3) # I eat 3 apples.
print("I eat %s apples." % "five") # I eat five apples.

number = 5
fruit = "복숭아"
print("I eat %d apples." % number) # I eat 5 apples.
print("I eat %d %s." % (number, fruit)) # I eat 5 복숭아.
print("I eat %s %s." % (number, fruit)) # I eat 5 복숭아. %s는 어떤 형태의 값이든 넣을 수 있다.

float = 97.86
print("I eat %s%% %s." % (float, fruit)) # I eat 97.86% 복숭아.
print()

# 문자열 포매팅 응용편
print("%10s" % "hi") #         hi 
print("%-10s" % "hi") # hi        (요까지)
print("%10.4f" % 3.141592) #     3.1416 (반올림?)
print("%7.2f" % 3.141592) #    3.14 (소숫점 뒤 2까지 표시 = 3.14 << 4자리가 나오고, 7자리를 맞추기 위해 앞에 공백 3자리 추기)
print()

print("I eat {0} {1} {2}".format(number, fruit, ".")) # I eat 5 복숭아 .

print("{0:<10}".format("hi"))  # hi            왼쪽 정렬
print("{0:>10}".format("hi"))  #         hi    오른쪽 정렬
print("{0:^10}".format("hi"))  #     hi        가운데 정렬
print("{0:*<10}".format("hi")) # hi********   왼쪽 정렬 + 남은 8자리 *로 채우기
print("{0:=^10}".format("hi")) # ====hi====   가운데 정렬 + 남은 8자리 =로 채우기

print("{0:0.4f}".format(3.141592)) # 3.1416
print("{0:=^10.4f}".format(3.141592)) # ==3.1416==
print("{{ 괄호 사용 }}".format()) # { 괄호 사용 }
print()

# f 문자열 포매팅
# 3.6 버전부터 사용 가능
name = "파이썬"
age = 3
print(f'나의 이름은 {name} 입니다. 내 나이는 {age} 살 입니다.')
print(f'나의 이름은 {name} 입니다. 내 나이는 {age + 1} 살 입니다.')
print(f'{"hi":<10}') 
print(f'{"hi":>10}') 
print(f'{"hi":=^10}') 
print(f'{1.2345:0.3f}') 
print(f'{{괄호}}') 
print()