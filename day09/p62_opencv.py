# file : p62_opencv.py
# desc : OpenCV 영상 처리

import cv2

samplePath = './day09/earth.mp4'
cap = cv2.VideoCapture(samplePath) #0은 웹캠, 또는 문자열로 동영상 경로

while True:
    ret, frame = cap.read()

    if not ret:
        cap = cv2.VideoCapture(samplePath)
        continue
    ## 영상 편집
    blur = cv2.blur(frame,(10,10),anchor=(-1,-1))
    cv2.imshow('blur',blur) # blur

    flip = cv2.flip(frame,0)
    cv2.imshow('Flip',flip) # flip 상하 반전


    cv2.imshow('original',frame)

    key = cv2.waitKey(5) # q 5ms 딜레이
    if key in [ord('q'),27]: # esc = 27,ord('q') = 키보드 q
        break
    elif key == ord('c'):
        cv2.imwrite('./day09/cap.jpg',frame)

cap.release()
cv2.destroyAllWindows()