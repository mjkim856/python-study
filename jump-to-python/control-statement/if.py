# 들여쓰기 뎁스가 다르면 오류 발생할 수 있으니 주의
# if 조건문 뒤에 :를 반드시 붙여야 함 주의

# 예시 1
# > < == !- >= <=
# elif 조건
money = 15000
if money >= 30000:
    print("배민을 시켜먹어라")
elif money == 20000:
    print("가게에서 먹어라")
else:
    print("편의점에서 먹어라")

print()

# 예시 2
# and, or, not
money = 20000
point = 10000
if money > 30000 and point > 10000:
    print("배민을 시켜먹어라")
elif money > 20000 or point > 5000:
    print("가게에서 먹어라")
else:
    print("편의점에서 먹어라")

print()

# 예시 3
# in, not in
pocket = ['money', 'card', 'coin', 'paper']
if 'card' not in pocket:
    print("집으로 가라")
elif 'money' or 'coin' in pocket:
    print("포장해서 먹어라")
else:
    print("종이를 버려라")

print()

# 예시 4
# pass
money = 15000
if money >= 30000:
    print("배민을 시켜먹어라")
elif money == 15000:
    pass
else:
    print("잔액 부족")

print()

# 예시 5
# 한 줄 if문
money = 15000
if money >= 30000: print("배민을 시켜먹어라")
else: print("잔액 부족")

print()

# 예시 6
# 조건부 표현식
score = 55
message = "success" if score >= 60 else "fail"
print(message)

print()
