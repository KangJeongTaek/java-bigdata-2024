# file : p35_qtAppy.py
# desc : PyQt5 앱 만들기

'''
PyQt5 -> Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
Qt -> C,C++에서 사용할 수 있는 GUI(WinApp) 프레임워크(멀티플랫폼)

설치 pip install PyQt5
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
# QApplication 만들 앱의 전체를 관리하는 클래스, QWidget 메뉴가 없는 윈도우앱, QMainWindow 메뉴가 존재하는 윈도우앱
from PyQt5.QtWidgets import *

class qtApp(QWidget): #QWidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
    def __init__(self) -> None:
        super().__init__() # 생성자, 부모 클래스의 생성자 함수도 실행되어야 한다
        self.initUI()


    def initUI(self):
        self.resize(800,400)
        #self.setGeometry(300,500,300,400) # 바탕화면 정해진 위치에 넓이와 높이를 설정
        self.setWindowTitle('첫번째 윈도우앱') # 타이틀
        self.center() # 화면 중앙으로 옮기기
        self.setWindowIcon(QIcon('./images/windows.png'))
        self.show() # 윈도우 창 그리기


    # 화면 중앙으로 옮기기
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self,event) -> None:
        paint = QPainter() #윈도우 창 위에 그림을 그리는 객체
        paint.begin(self) # 그림을 그리기 시작하면
        paint.setPen(QColor(100,200,240)) # RGV값
        paint.setFont(QFont('Bauhaus 93',40))
        paint.drawText(270,400//2, 'Hello PyQt')

        paint.end() # 반드시 닫아야한다
        
    


app = QApplication(sys.argv) #
inst = qtApp() #객체 생성

app.exec() # 실행
