# file : p40_qtApp.py
# desc : PyQt5,QtDesigner 같이 사용

'''
설치 pip install PyQt5
설치 pip install PyQt5Designer
위젯 == 컨트롤

시그널 == 이벤트
'''

import sys
from PyQt5 import QtGui,QtCore,QtWidgets,uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()


    def initUI(self): # UI 파일을 로드해서 화면 디자인
        self.setWindowIcon(QIcon('./images/windows.png'))
        uic.loadUi('./day06/firstApp.ui',self)
        
        #버튼 시그널 처리
        self.btnMsg.clicked.connect(self.btnMsgClicked) #ui파일 내 위젯은 자동완성이 안된다.
        self.show() # 윈도우 창 그리기

    def closeEvent(self, QCloseEvent): # 오버라이드(재정의)
        re = QMessageBox.question(self,'종료확인','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        if re == QMessageBox.Yes: #진짜 닫음
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
            QMessageBox.about(self,'취소','종료하지 않습니다.')

    def btnMsgClicked(self):
        self.label.setText('Hello!!')
        QMessageBox.about(self,'Qt디자이너','클릭했습니다.!!!')
        if QMessageBox.Ok:
            self.label.setText('Hi')

app = QApplication(sys.argv) #
inst = qtApp() #객체 생성

app.exec() # 실행

