# file:p13_starPrint
# desc : 별찍기


for i in range(1,6):
      print('*' * i)

for i in range(1,6):
    print('*',end ='')
    for j in range(1,i):
            print('*',end ='')
    print()


for i in range(1,6):
    for j in range(i,6):
            print('*',end='')
    print()


for i in range(1,6):
    for j in range(i,6):
            print(' ', end ='')
    for j in range(6-i,6):
            print('*',end='')
    print()
for i in range(1,6):
    for j in range(6-i,6):
            print('*', end='')
    print()

for i in range(1,6):
    for j in range(i,6):
            print(' ', end ='')
    for k in range(6-i,6):
            print(' ', end ='')
            print('*',end='')
    print()



i = 0
while True:
    i += 1
    if i> 5 : break
    print('*'*i)

for i in range(1,101):
    print(i)

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
print(total)
avg =total/len(A)
print(avg)

numbers = [1,2,3,4,5]
result = [m for m in numbers if m % 2 != 0]
print(result)