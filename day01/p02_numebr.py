# file : p02_number.py
# desc : 숫자형 자료타입 및 연산

#일반 숫자형
age = 40 # int형을 담는 변수 선언

taxRate = 8.8 # float형을 담는 변수 선언

highFloats = 4.24E10 # 지수승(float)

print('나이는 ', age) #문자열이 "",'' 둘다 사용 가능.
print('세율은', taxRate)
print('지수값',highFloats)

#특수 숫자형

binVal = 0b11111111 # 10진수로 255
octVal = 0o11 # 9 1~7
hexVal = 0xFF # 255 0~9ABCEDF



print('이진수', binVal)
print('8진수', octVal)
print('16진수', hexVal)

#타입을 적을 필요가 없다


#사칙 연산
a, b, c= 3, 4, 9
print(a+b)
print(a-c)
print(a*c)
print(c/b) #정확하게 실수로 나누기
print(c // b) #정확하게 정수로 나누기 
print(c %b) #정수로 나눈 나머지
# 단, 나누기는 3가지로 분류된다. / , // , %

print(2 ** 10) # 1024 import.math; math.pow() 제곱승
