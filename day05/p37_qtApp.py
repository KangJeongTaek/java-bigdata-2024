# file : p35_qtAppy.py
# desc : PyQt5 앱 만들기

'''
PyQt5 -> Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
Qt -> C,C++에서 사용할 수 있는 GUI(WinApp) 프레임워크(멀티플랫폼)

설치 pip install PyQt5
'''

import sys
# QApplication 만들 앱의 전체를 관리하는 클래스, QWidget 메뉴가 없는 윈도우앱, QMainWindow 메뉴가 존재하는 윈도우앱
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
