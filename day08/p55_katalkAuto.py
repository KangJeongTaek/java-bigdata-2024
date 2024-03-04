# file : katalkAuto.py
# desc : 카톡PC에서 자동으로 메시지 보내기
# pyautogui.ImageNotFoundException 예외 자주 발생
import pyautogui as auto
import os
import pyperclip as clip
import time
try:
    katalkLoc = auto.locateOnScreen('./day08/findLoc1.png')
    print(katalkLoc)
    clickPos = auto.center(katalkLoc)
    auto.doubleClick(clickPos)
    time.sleep(1)
except auto.ImageNotFoundException:
    katalkLoc = auto.locateOnScreen('./day08/findLoc5.png')
    print(katalkLoc)
    clickPos = auto.center(katalkLoc)
    auto.doubleClick(clickPos)
    time.sleep(1)


