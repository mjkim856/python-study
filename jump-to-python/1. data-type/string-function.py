a = "Hello, World!"

print(len(a)) # 13
print(a.count('l')) # 3
print(a.find('o')) # 4
print(a.find('a')) # -1
print(a.index('o')) # 4
# print(a.index('a')) ValueError: substring not found, Error 발생
# print(a.find('a'))와 같이 문자열 중 문자 'o'가 처음으로 나온 위치를 반환하는 건 동일하나, Error가 발생한다.
print(",".join(a)) # H,e,l,l,o,,, ,W,o,r,l,d,!
print(a.upper()) # HELLO, WORLD!
print(a.lower()) # hello, world!
print()

b = "       Hello,      World!         "
print(b.lstrip()) # Hello,      World!         (end)
print(b.rstrip()) #        Hello,      World!
print(b.strip())  # Hello,      World!
print()

c = "I! like!dog!"
print(c.replace("dog", "cat")) # I! like!cat!
print(c.split())               # ['I!', 'like!dog!']
print(c.split("!"))            # ['I', ' like', 'dog', '']
print(type(c))                 # <class 'str'>

c = c.split("!")               
print(type(c))                 # <class 'list'>
