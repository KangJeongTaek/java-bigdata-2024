# file : p39_qtApp.py
# desc : PyQt5 앱 만들기(Continue)

'''
설치 pip install PyQt5

위젯 == 컨트롤

시그널 == 이벤트
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()


    def initUI(self):
        
        self.setGeometry((1920-300)//2,(1800-300)//2,320,230) # 바탕화면 정해진 위치에 넓이와 높이를 설정
        self.setWindowTitle('세번째 qt앱') # 타이틀
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 화면 UI에서 추가/변경할 것
        btn1 = QPushButton('클릭',self)
        btn1.setGeometry(210,180,100,40)
        btn1.clicked.connect(self.btn1Clicked) #함수인데 괄호가 없는 이유?
        self.show() # 윈도우 창 그리기

    def btn1Clicked(self):
        QMessageBox.information(self,'버튼클릭','버튼을 눌렀습니다.')

    def closeEvent(self, QCloseEvent): # 오버라이드(재정의)
        re = QMessageBox.question(self,'종료확인','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        if re == QMessageBox.Yes: #진짜 닫음
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
            QMessageBox.about(self,'취소','종료하지 않습니다.')

app = QApplication(sys.argv) #
inst = qtApp() #객체 생성

app.exec() # 실행

