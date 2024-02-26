# file : test.py
# desc : 되새김 문제

class Calculator:
    def __init__(self) -> None:
        self.value =0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def __init__(self) -> None:
        super().__init__()

    def minus(self, val):
        self.value -= 7

class MaxLimiteCalculaotr(Calculator):
    def __init__(self) -> None:
        super().__init__()

    def add(self,val):
        if self.value == val < 100:
            self.value += val
        else:
            self.value = 100


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

cal1 = MaxLimiteCalculaotr()

cal1.add(50)
cal1.add(60)

print(cal1.value)


def multithree(x):
    return x*3

a = list(map(lambda x : x*3,[1,2,3,4]))

b = list(map(multithree,[1,2,3,4]))
print(a)
print(b)


listNum = [-8,2,7,5,-3,5,0,1]
maxN = max(listNum)
minN = min(listNum)
print(maxN +minN)

import datetime

curr = datetime.datetime.now()

print(f'{curr.year}/{curr.month:02d}/{curr.day:02d} {curr.hour}:{curr.minute}:{curr.second}')


import random

lotto = []
while len(lotto) < 6:
    number = random.randint(1,46)
    while number not in lotto:
        lotto.append(number)

lotto.sort()
print(lotto)


print(chr(ord('a')) == 'a')


from itertools import *

printList = list(permutations('abcd',4))

for i in printList:
    print(','.join(i))
print(printList)

print(len(printList))





