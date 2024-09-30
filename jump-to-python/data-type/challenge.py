#1
print("\n1. 평균 점수 구하기")
ko = 80
en = 75
math = 55

print((ko+en+math)/3)

#2
print("\n2. 홀수 짝수 판별하기 ")
num = 13
print("홀수" if num%2==1 else "짝수")

#3
print("\n3. 주민등록번호 나누기 ")
pin = "881212-1212112"
print("앞자리: " + pin[:6])
print("뒷자리: " + pin[7:])

#4
print("\n4. 주민등록번호 성별 인덱싱 ")
pin = "881212-1212112"
print(pin[7])

#5
print("\n5. 문자열 바꾸기 ")
a = "a:b:c:d"
print(a.replace(":", "#"))
print()

#6
print("\n6. 리스트 역순 정렬 ")
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#7
print("\n7. 리스트를 문자열로 변경\n")
a = ['Life', 'is', 'too', 'short']
print(type(a))

a = " ".join(a)
print(a)
print(type(a))

#8
print("\n8. 튜플 더하기 ")
a = (1, 2, 3)
b = (4, )
# b = (4) 이렇게 하면 type을 int로 인식하여 에러 발생
# TypeError: can only concatenate tuple (not "int") to tuple
a = a + b
print(a)

#9
print("\n9. 딕셔너리의 키 ")
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python' TypeError: unhashable type: 'list'
# key에 list를 사용할 수 없으며, 이는 key가 변하는(mutable) 값이기 때문이다.
a[250] = 'python'

#10
print("\n10. 딕셔너리 값 추출 ")
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

#11
print("\n11. 리스트 중복 제거 ")
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b) # [1, 2, 3, 4, 5]

#12
print("\n12. 파이썬 변수 심화 ")
a = b = [1, 2, 3]
a[1] = 4
print(a) # [1, 4, 3]
print(b) # [1, 4, 3]

# 리스트 a의 값을 변경했지만 리스트 b의 값도 변경되는 이유는 a와 b가 같은 객체를 참조하고 있기 때문이다.
print(id(a)) # 4343054080
print(id(b)) # 4343054080

# 만약 각각 다른 객체를 참조하게 하고 싶다면 b(혹은 a)에 복사본을 할당해야 한다.
b = a[:]
a[1] = 10

print(a) # [1, 10, 3]
print(id(a)) # 4343054080

print(b) # [1, 4, 3]
print(id(b)) # 4344180672
