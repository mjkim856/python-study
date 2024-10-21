# 클래스 a로 만든 객체 b가 있다면, b는 a의 인스턴스이다 / b는 객체이다 이렇게 표현하는 것이 어울린다.

class FourCal:

    # 객체에 first, second와 같이 초깃값이 필요한 경우는 생성자를 구현하는 것이 안전한 방법이다.
    # 생성자는 객체가 생성될 때 자동으로 호출되는 메서드이다. __init__를 사용해 구현한다.
    # setdata()와 이름만 다르지만, __init__를 사용했기에 객체가 생성되는 시점에 자동으로 호출된다는 차이점이 있다. 
    def __init__(self, first, second):
        self.first = first
        self.second = second

    # 계산할 숫자를 받아서 변수에 설정하는 메서드 (= 클래스 내의 함수)
    # self에는 setdata()를 호출한 객체가 자동으로 전달된다.
    # 자바는 이거 명시 안 했는데... 파이썬만의 특징이라고 한다! self라는 이름이 아니어도 된다고 함. (특이하군요)
    def setdata(self, first, second):   
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(2, 4)
b = FourCal(3, 8)
c = FourCal(3, 0)

# b = FourCal()     __init__ 사용하니까 이렇게 하면 오류 발생함
# a.setdata(4, 2)   __init__ 사용해서 이제 이거 사용할 필요 없다.

# print(type(FourCal()))  # <class '__main__.FourCal'>, 근데 이것도 파라미터 설정 안 하니까 오류 난다.
print(type(FourCal(4, 8)))  # __init__ 설정하니까 생성자 때문인지 꼭 이렇게 파라미터를 넣어줘야 함
print(type(a))          # <class '__main__.FourCal'>

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print()

print(b.add())
print(b.sub())
print(b.mul())
print(b.div())

# print(c.div())        ZeroDivisionError: division by zero

print()
print("=================== [ 상속 ] ===================")

# class 클래스_이름(상속할_클래스_이름)
class MoreCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

print(MoreCal(4, 8).pow())
print(MoreCal(4, 8).add())

print()
print("=================== [ 메소드 오버라이딩 ] ===================")

class OverrideCal(FourCal):
    def div(self):
        if self.second == 0: return 0
        else: return self.first / self.second

d = OverrideCal(4, 0)
print(d.div())      # 오류 아닌 0 출력

print()
print("=================== [ 클래스 변수 ] ===================")

class Family:
    lastname = "kim"    # 이게 클래스변수, 이 클래스를 사용해서 만든 모든 객체에 공유된다.
                        # 근데 객체변수보다는 사용 비율이 낮음!
e = Family()

print(Family.lastname)
print(e.lastname)

f = Family()
f.lastname = "park"     

print(Family.lastname)      # kim
print(e.lastname)           # kim
print(f.lastname)           # park