# 예시 1
treehit = 0  
while treehit < 10:
    treehit = treehit + 1   
    print("%d treehit!" % treehit)
    if treehit == 10:
        print("The tree falls")  

print()

# 예시 2
prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())

# 예시 3
coffee = 1800
count = 0
while True:
    print("카드를 넣어주세요")
    money = int(input())
    if money >= coffee:
        print("결제가 완료되었습니다.")
        money = money - coffee
        print("잔액은 %d원 입니다." % money)
        break
    else:
        print("잔액이 부족합니다. 현재 카드 잔액은 %d원입니다." % money)
        break

# 예시 4
# continue
a = 0
while a < 10 :
    a = a + 1
    if a % 2 == 0: continue
    print(a)

# 예시 5
# while문 무한루프
'''
while True:
    print("무한루프 진행!")
'''
