# 예시 1. 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

print()

# 예시 2. 다양한 for문
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

print()

# 예시 3. for문의 응용
score = [90, 25, 67, 45, 80]
for i in score:
    if i >= 60: print("합격입니다.")
    else: print("불합격입니다.")

print()

# 예시 4. for문과 continue문
score = [90, 25, 67, 45, 80]
for i in score:
    if i >= 60: print("축하합니다!")
    else: continue

print()

# for문과 range() 함수
# range(a, b) 라면 a 이상 b 미만이다.
a = range(10)       # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(a)

b = range(2, 18)    # 2, 3, 4, ... 16, 17
print(b)

score = [90, 25, 67, 45, 80]
for i in range(len(score)):
    if score[i] >= 60: print("%d번 학생, 축하합니다!" % (i + 1))
    else: continue

# for + range() = 100까지 더하기
result = 0
for i in range(1, 101):
    result += i
print(result)

print()

# 예시 5-1. 2단 구구단 만들기 !!
for i in range(1, 10):
    print("2 * %d = %d" % (i, 2*i))

print()

# 예시 5-2. 9단 구구단 만들기 !!
for i in range(2, 10):
    for j in range(1, 10):      
        print("%d단 출력 : %d * %d = %d" % (i, i, j, i*j))
    print()

print()

# 예시 6-1. 리스트 컴프리헨션 사용하기
# [표현식 for 항목 in 반복가능객체 (if 조건문)]
a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)

print()

# 예시 6-2. 리스트 컴프리핸션으로 구구단 리스트화하고 출력하기

nndan = [i*j for i in range(2, 10)
             for j in range(1, 10)]

print(nndan)

print()
