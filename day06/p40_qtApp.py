# file : p40_qtApp.py
# desc : PyQt5,QtDesigner 같이 사용

'''
설치 pip install PyQt5
설치 pip install PyQt5Designer
위젯 == 컨트롤

시그널 == 이벤트
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()


    def initUI(self):
        
        self.setGeometry((1920-300)//2,(1800-300)//2,320,230) # 바탕화면 정해진 위치에 넓이와 높이를 설정
        self.setWindowTitle('네번째 qt앱') # 타이틀
        self.setWindowIcon(QIcon('./images/windows.png'))

        
        self.show() # 윈도우 창 그리기

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

