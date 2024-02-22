#file : p08_review.py
#desc : 변수 리뷰

a = 13
if (a % 2 == 0):
    print('짝수')
else :
    print('홀수')

pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)

a = "a:b:c:d"
b = a.replace(":","#")
print(b)

a = {'A':90,'B':80,'C':70}
result = a.pop('B')
print(a)
print(result)
del a[0]
print(a)