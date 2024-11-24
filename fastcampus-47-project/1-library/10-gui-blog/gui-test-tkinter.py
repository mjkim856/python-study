from tkinter import *

root = Tk()                                   # tkinter 객체(창) 생성
label = Label(root, text='Hello World !')     # root 창에 Label 컴포넌트(위젯) 추가
label.pack()                                  # label 객체를 창에 표시

root.mainloop()                               # root 창을 메인 루프에 태우기
                                              # 종료되지 않고 이벤트 수신 등의 역할을 수행
