# file : p54_captWeather.py
# desc : 네이버 날씨 화면 캡쳐

import pyautogui as auto
import pyperclip as clip
import time

# auto.mouseInfo()

auto.click(88, 154,duration=0.5)
auto.hotkey('ctrl','a')
time.sleep(0.05)

regions = ['서울','강원','대구','부산','대전']

for region in regions:
    auto.moveTo(90, 154,duration=0.5)
    auto.hotkey('ctrl','a')
    time.sleep(0.2)
    clip.copy(f'{region} 날씨')
    auto.hotkey('ctrl','v')
    time.sleep(0.2)

    auto.press('enter')
    time.sleep(1.0)

    startX, startY = 31,272
    endX,endY = 694,906
    auto.screenshot(f'day08/{region}날씨.png',region=(startX,startY,endX-startX,endY-startY))
# clip.copy('부산 용당동 날씨')

# auto.hotkey('ctrl','v')
# time.sleep(0.05)

# auto.press('enter')
# time.sleep(1.0)

# startX, startY = 31,272
# endX,endY = 694,906

# auto.screenshot('./day08/todayWeather.png',region=(startX,startY,endX-startX,endY-startY))

# print('저장완료')

