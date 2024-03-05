# file : p66_imageEditor.py
# desc : PyQt 이미지 에디터

'''
qrc 파일을 사용하기 위해서는
> pyrcc5 "resources.qrc" -o "resoureces_rc.py"
'''

import sys
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent, QMouseEvent
from PyQt5.QtWidgets import *
# 리소스 파일 추가
import resources_rc
#OpenCV 추가
import cv2


class WinApp(QMainWindow): # QWidget이 아님
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        uic.loadUi('./day09/pyNewPaint.ui',self)
        self.setWindowIcon(QIcon('./day09/draw.png'))
        self.setWindowTitle('이미지 에디터v0.5')
        ## 이미지 추가 / 여러가지 UI에 대한 초기화
        pixmap = QPixmap('./images/tropical_beach.jpg')
        pixmapscaled = pixmap.scaled(801,481)
        self.lblCanvas.setPixmap(pixmapscaled)

        


        #초기화 끝
        self.show()
    
    def initSignal(self):
        #메뉴/ 툴바 액션에 대한 시그널처리함수 선언
        self.action_New.triggered.connect(self.actionNewClicked)
        self.action_Open.triggered.connect(self.actionOpenClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_PenRed.triggered.connect(self.actionPenRedClicked)
        self.action_Exit.triggered.connect(self.actionExitClicked)
        self.action_PenGreen.triggered.connect(self.actionPenGreenClicked)
        self.action_PenBlue.triggered.connect(self.actionPenBlueClicked)
        self.action_About.triggered.connect(self.actionAboutClicked)
        self.action_Eraser.triggered.connect(self.actionEraserClicked)
        self.action_Grayscale.triggered.connect(self.actionGrayscaleClicked)
        

    def actionNewClicked(self):
        canvas = QPixmap(self.lblCanvas.width(),self.lblCanvas.height())
        canvas.fill(QColor('white'))
        self.lblCanvas.setPixmap(canvas)

    def actionOpenClicked(self):
        image = QFileDialog.getOpenFileName(self,'이미지 열기','','Image file(*.jpg;*.png;*.jpeg)')
        imagePath = image[0]
        canvas = QPixmap(imagePath).scaled(801,481)
        self.lblCanvas.setPixmap(canvas)


    def actionSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self,'이미지 저장','','Image file(*.png)')
        if filePath == '':return
        pixmap = self.lblCanvas.pixmap()
        pixmap.save(filePath)

    def actionExitClicked(self):
        exit(0)

    def actionPenRedClicked(self):
        self.brushColor = Qt.red # 빨간색이 기본

    def actionPenGreenClicked(self):
        self.brushColor = Qt.green

    def actionPenBlueClicked(self):
        self.brushColor = Qt.blue

    def actionEraserClicked(self):
        self.brushColor = None

    def actionAboutClicked(self):
        QMessageBox.about(self,'알림','이미지 에디터 v0.5')

    def actionGrayscaleClicked(self):
        image = self.lblCanvas.pixmap()
        #gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # 현재 실행 안 됨
        #self.lblCanvas.setPixmap(gray)
        QMessageBox.about(self,'알림','그레이스케일')


    def mouseMoveEvent(self,QMouseEvent) -> None:
        print(QMouseEvent.x(),QMouseEvent.y()-54)
        brush = QPainter(self.lblCanvas.pixmap())
        try:
            brush.setPen(QPen(self.brushColor,3.5,style=Qt.SolidLine,cap=Qt.RoundCap))
            brush.drawPoint(QMouseEvent.x(),QMouseEvent.y()-54)
            brush.end()
            self.update()
        except:
            pass
        


    def closeEvent(self,QCloseEvent):
        re = QMessageBox.question(self,'종료','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    inst = WinApp()
    sys.exit(app.exec_())
