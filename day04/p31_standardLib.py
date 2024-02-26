# file : p31_standardLib.py
# desc : 표준 라이브러리(빌트인) 학습
import datetime
import time
import random

day1 = datetime.date(2024,2,26) # 현재의 os에 맞춰서 날짜형으로 변경
print(day1)

curr = datetime.datetime.now()
print(datetime.datetime.now())

print(curr.weekday()) # 0은 월요일

print(curr.year)

print(curr.month)

print(curr.minute)

print(curr.second)

print(f'{curr.year}년 {curr.month:02d}월 {curr.day:02d}일 {curr.hour:02d}시 {curr.minute:02d}분 {curr.second:02d}초')

curr2 = time.localtime()
print(curr2)

# odd = [1,3,5,7,9]
# even = [2,4,6,8,10]

# total = list(zip(odd,even))
# print(type(zip(odd,even)))
# for i in total:
#     print(sum(i))
#     time.sleep(0.7)

print(random.randint(1,46))
print(random.random())

## 로또
result = []
total  = []
for i in range(5):
    while True:
        val  = random.randint(1,45)
        while val not in result:
            result.append(val)
        
        if len(result) == 6:
            break
    result.sort()
    total.append(result)
    result =[]
print(total)