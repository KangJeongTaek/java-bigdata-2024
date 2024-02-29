# file : p48_QRcodeApp.py
# desc : PyQt5 QR코드앱

# pip install pip install qrcode
import sys
from PyQt5 import QtGui,QtCore,QtWidgets,uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qrcode
class qtApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()


    def initUI(self): # UI 파일을 로드해서 화면 디자인
        self.setWindowIcon(QIcon('./images/qr-code.png'))
        uic.loadUi('./day07/qrApp.ui',self)
        self.setWindowTitle('Qr코드 생성기')
        #버튼 시그널 처리
        self.btnGenerate.clicked.connect(self.btnGenerateClicked) #ui파일 내 위젯은 자동완성이 안된다.
        self.show() # 윈도우 창 그리기

    def btnGenerateClicked(self):
        data = self.txtQrData.text()

        if len(data.strip()) == 0:
            QMessageBox.about(self,'경고','데이터를 입력해주세요.')
            return
        else:
            imgPath = './day07/qr.png'
            qrImage = qrcode.make(data)
            qrImage.save(imgPath)
            img = QPixmap(imgPath)
            self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(300))

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

