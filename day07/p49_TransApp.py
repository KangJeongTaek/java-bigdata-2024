# file : p49_TransApp.py
# desc : PyQt5 QR코드앱

# pip install pip install googletrans
import sys
from PyQt5 import QtGui,QtCore,QtWidgets,uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from googletrans import Translator
class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.myTrans = Translator()


    def initUI(self): # UI 파일을 로드해서 화면 디자인
        self.setWindowIcon(QIcon('./images/translate.png'))
        uic.loadUi('./day07/papagoApp.ui',self)
        self.setWindowTitle('구글번역기')
        #버튼 시그널 처리
        self.btnTrans.clicked.connect(self.btnTransClicked) #ui파일 내 위젯은 자동완성이 안된다.
        self.txtBaseText.returnPressed.connect(self.btnTransClicked)
        self.show() # 윈도우 창 그리기

    def btnTransClicked(self):
        text = self.txtBaseText.text()
        
        if len(text.strip()) == 0:
            QMessageBox.about(self,'경고','데이터를 입력해주세요.')
            return
        else:
            result = self.myTrans.translate(text,src='auto',dest = 'en')
            
            self.txtResult.append(result.text)

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

