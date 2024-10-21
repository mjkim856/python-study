# from 모듈이름 import 모듈함수1, 모듈함수2 ... 
# from mod1 import add, sub
# from mod1 import *

# if __name__ == "__main__":
#   print("어쩌구...")
# 직접 이 파일을 실행했을 때는 실행되나,    << __name__ 에 __main__ 이 저장됨.
# 다른 파일에서 이 모듈을 불러 사용할 때는 수행되지 않는다.     << __name__에 mod1이 저장된다.

# 모듈 안에 클래스, 변수 등을 포함할 수 있다. 