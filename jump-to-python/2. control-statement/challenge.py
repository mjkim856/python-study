#1
print("\n1. 조건문의 참과 거짓")

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")       # shirt가 출력된다.
elif "need" in a: print("need")
else: print("none")

#2
print("\n2. 3의 배수의 합 구하기")
result = 0
i = 1

while i <= 1000:
    if i%3 == 0:
        result += i
    i += 1

print(result)

#3
print("\n3. 직각 별 찍기 !!! ")

i = 0
while True:
    i += 1
    if i == 6: break
    print("*" * i)

print()

# 나였다면 이렇게 했을 듯? (for문 사용)
num = 5
for i in range(num):
    print("*" * (i+1))

'''
결과물은 아래와 같다. 

*
**
***
****
*****
'''
    
#4
print("\n4. 1부터 100까지 숫자 출력")
for i in range(1, 101):
    print(i)

#5
print("\n5. 평균 점수 구하기")
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in a:
    total += score

average = total / len(a)

print(average)

#6
print("\n6. 리스트 컴프리핸션 사용하기")
number = [1, 2, 3, 4, 5]
result = [i*2 for i in number if i%2 == 1]
print(result)       # [2, 6, 10]
