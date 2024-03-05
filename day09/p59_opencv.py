# file : p59_opencv.py
# desc : OpenCV 활용

'''
OpenCV 실시간 이미지 프로세싱 라이브러리
> pip install opencv-python
'''

import cv2

# print(cv2.__version__)

image = cv2.imread('./images/coby.jpg',cv2.IMREAD_UNCHANGED) # cv2.IMREAD_GRAYTSCALE -> 칼라 이미지를 흑백으로 변환해주는 기능
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

height, width, channel = image.shape

print(width,height,channel)

sizeSmall = cv2.resize(image, (width//2, height//2))

img_wcropped = image[:,:(width//2)] # x축을 반으로 잘라 반만 나오도록
img_hcropped = image[(height//2):,:] # y축을 반으로 잘란 반만 나오도록

cv2.imshow('Coby the Cat Color',image) # 원본
cv2.imshow('Reduce Coby',sizeSmall) # 반으로 줄인 사이즈
cv2.imshow('Half Coby',img_hcropped)
cv2.imshow('Coby the Cat Gray',gray) # 흑백
cv2.imshow('Half Coby',img_wcropped)

cv2.waitKey(0)

cv2.destroyAllWindows()
