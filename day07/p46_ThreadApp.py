# file : p45_Thread.py
# desc : PyQt5 스레드 학습용(스레드 사용)

import sys
from PyQt5 import QtGui,QtCore,QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackgroundWorker(QThread): #PyQt용 쓰레드
    initUiSignal = pyqtSignal(int) # 스레드로 진행시 UI에서 초기에 처리할 초기화 부분 시그널 전달
    setPgbSignal = pyqtSignal(int) # 스레드 진행시 변경되는 숫자를 UI로 전달
    setTxbSignal = pyqtSignal(str) # 스레드 진행시 화면에 출력될 문자열 UI쪽으로 전달
    setBtnSignal = pyqtSignal(bool)
    MessageSignal = pyqtSignal(str)

    def __init__(self,parent) -> None: # 부모는 qtApp 클래스
        super().__init__(parent)
        self.parent = parent

    def run(self) -> None:
        maxVal = 10_000
        self.initUiSignal.emit(maxVal) #나는 값을 보내니 Ui쪽(qtApp)에서 받아서 처리해라
        self.setBtnSignal.emit(True)
        for i in range(maxVal):
            print(f'스레드 진행 >> {i}')
            self.setPgbSignal.emit(i)
            self.setTxbSignal.emit(f'스레드 진행 >> {i}')

        self.setBtnSignal.emit(False)
        self.MessageSignal.emit('작업 완료!!!')
        
            #self.parent.pgbTask.setValue(i) #UI스레드의 권한을 백그라운드 스레드에게 주지 않는다
            #self.parent.txbLog.append(f'스레드 진행 >> {i}') # 사용불가


class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()


    def initUI(self): # UI 파일을 로드해서 화면 디자인
        self.setWindowIcon(QIcon('./images/windows.png'))
        uic.loadUi('./day07/testThread.ui',self)
        self.setWindowTitle('스레드앱')
        #버튼 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) #ui파일 내 위젯은 자동완성이 안된다.
        
        self.show() # 윈도우 창 그리기




    def btnStartClicked(self):

        self.txbLog.clear()
        th = BackgroundWorker(self)
        th.start() # 스레드 내 run() 함수 실행
        th.setBtnSignal.connect(self.setBtn)
        th.initUiSignal.connect(self.initPgbTask)
        th.setPgbSignal.connect(self.setPgbTask)
        th.setTxbSignal.connect(self.setTxbLog)
        th.MessageSignal.connect(self.openMessagebox)

        

        
        
        
        
        

    @pyqtSlot(int)
    def setPgbTask(self,val):
        self.pgbTask.setValue(val)

    @pyqtSlot(int) # pyqtSignal에서 넘어온 값을 처리해주는 부분이라고 선언
    def initPgbTask(self,maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0,maxVal -1)
    @pyqtSlot(str)
    def setTxbLog(self,msg):
        self.txbLog.append(msg)

    @pyqtSlot(str)
    def openMessagebox(self,msg):
        QMessageBox.about(self,'작업 완료!!!',msg)

    @pyqtSlot(bool)
    def setBtn(self,isStart):
        if isStart == True:
            self.btnStart.setDisabled(True)
        elif isStart == False:
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

