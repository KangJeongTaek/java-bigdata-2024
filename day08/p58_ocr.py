#file : p58_ocr.py
# desc : 이미지 내 글자 인식

'''
pip install pytesseract
테서렉트 설치(https://github.com/UB-Mannheim/tesseract/wiki)
'''

import pytesseract as pt

from PIL import Image

imgPath = './day08/originalImage.png'
im = Image.open(imgPath)

im.show()

pt.pytesseract.tesseract_cmd = 'G:/DEV/Tesseract-OCR/tesseract.exe' #테서렉트 설치 경로를 입력

text = pt.image_to_string(Image.open(imgPath),lang='kor')

print(text)
