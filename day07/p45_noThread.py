# file : p44_noThread.py
# desc : PyQt5 스레드 학습용(스레드 사용 안 함)

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
        uic.loadUi('./day07/testThread.ui',self)
        self.setWindowTitle('노쓰레드앱')
        #버튼 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) #ui파일 내 위젯은 자동완성이 안된다.
        self.show() # 윈도우 창 그리기

    def btnStartClicked(self):
        self.txbLog.clear()
        self.pgbTask.setValue(0) #재설정
        self.pgbTask.setRange(0,100) #프로그래스바 범위설정
        self.btnStart.setDisabled(True)
        #UI(메인)스레드가 화면을 그릴 수 있는 여유가 없음(응답없음 발생)
        for i in range(0,100): #0~999,999 #1_000_000
            print(f'노스레드 진행 >> {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'노스레드 진행 >> {i}')

        self.btnStart.setEnabled(True)

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

