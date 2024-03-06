import sys
from PyQt5 import QtGui,QtCore,QtWidgets,uic
from PyQt5.QtCore import Qt,QThread,pyqtSignal, pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QtBackGroundWorker(QThread):
    textChanged = pyqtSignal()
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent


    def run(self): # 저장된 값과 현재의 텍스트가 다르면 *를 붙이자
        previousTxt = self.parent.plainTextEdit.toPlainText()
        self.working = True

        while self.working:
            currentTxt  = self.parent.plainTextEdit.toPlainText()
            if previousTxt != currentTxt:
                self.textChanged.emit()

            previousTxt = currentTxt
            self.usleep(100*1000)
    def stop(self):
        self.working = False
        self.quit()

class WinApp(QMainWindow): 



    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        uic.loadUi('./day10/notepad.ui',self)
        self.setWindowTitle('메모장 v0.5')




        self.show()
        self.worker_thread = QtBackGroundWorker(self)
        self.worker_thread.textChanged.connect(self.updateWindowTitle)
        self.worker_thread.start()
        


    def initSignal(self):
        self.actionOpen_O.triggered.connect(self.actionOpen_Clicked)
        self.actionSave_S.triggered.connect(self.actionSave_Clicked)
        self.action_Save_AS.triggered.connect(self.actionSave_as_Clicked)
        self.action_About.triggered.connect(self.action_About_Clicked)
        self.action_E_Exit.triggered.connect(self.action_Exit_clicked)
        

    def updateWindowTitle(self):
        title = self.windowTitle()
        if '*' not in title:
            self.setWindowTitle(f'{title}*')


    def actionOpen_Clicked(self):
        text = QFileDialog.getOpenFileName(self,'텍스트 열기','','Txt file(*.txt)')
        global textPath
        textPath = text[0]
        if textPath:
            self.plainTextEdit.setPlainText(open(textPath,encoding='UTf-8').read())
            global title
            title = textPath.split('/')[-1]
            if '*' in title:
                title = title.rstrip('*')
            self.setWindowTitle(title)


    def actionSave_Clicked(self):
        try:
            if filePath:
                with open(filePath,mode='w',encoding='UTF-8') as f:
                    f.write(self.plainTextEdit.toPlainText())
                    self.setWindowTitle(self.windowTitle().rstrip('*'))
            else:
                with open(textPath,mode='w',encoding='UTF-8') as f:
                    f.write(self.plainTextEdit.toPlainText())
                    self.setWindowTitle(self.windowTitle().rstrip('*'))
        except NameError:
            self.actionSave_as_Clicked()

    def actionSave_as_Clicked(self):
        global filePath
        filePath, _ = QFileDialog.getSaveFileName(self,'텍스트 저장','','Txt file(*.txt)')
        try:
            with open(filePath,'w',encoding='UTF-8') as f:
                f.write(self.plainTextEdit.toPlainText())
                self.setWindowTitle(filePath.split('/')[-1])
        except FileNotFoundError:
            pass
            

    def action_About_Clicked(self):
        QMessageBox.about(self,'메모장 v0.5','아직 조잡합니다.')


    def action_Exit_clicked(self):
        re = QMessageBox.question(self,'종료확인','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            self.worker_thread.working = False
            self.worker_thread.wait()  
            exit(0)
        else:
            QMessageBox.about(self,'취소','종료하지 않습니다.')


    def closeEvent(self, QCloseEvent): 
        re = QMessageBox.question(self,'종료확인','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: 
            self.worker_thread.working = False
            self.worker_thread.wait()  
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
            QMessageBox.about(self,'취소','종료하지 않습니다.')


        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    inst = WinApp()
    sys.exit(app.exec_())