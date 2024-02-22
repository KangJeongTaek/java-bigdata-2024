# file : p09+ifCondition
# desc : if 제어문
money = 5000
haveMoney = True
if(money>=5000):
    #indentation(들여쓰기) == space 4
    print("택시")
elif(money<5000 and money>=2500):
    print('기사는 홈플러스 앞까지만 가주세요')
else:
    print("걸어")


marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print(f"{number}번 학생 축하합니다. {mark:.1f}의 점수로 합격입니다. " )


a, b,c,d = 10,5,7,9
print(a>=b)
print(c>d)
print(a>=b and c> d)
print(a>=b or c>d)

print(1 in[1,3,5,7,9])
print(6 in[1,3,5,7,9])
print(6 not in[1,3,5,7,9])


##print() end옵션, sep옵션
print(1 in [1,3,5,7,9], end='')
print('13579','test',sep=',')
print()