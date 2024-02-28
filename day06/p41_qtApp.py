# file : p41_qtApp.py
# desc : 검색

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
        self.setWindowIcon(QIcon('./images/news.png'))
        uic.loadUi('./day06/naverNews.ui',self)

        self.show()

app = QApplication(sys.argv) #
inst = qtApp() #객체 생성

app.exec() # 실행
