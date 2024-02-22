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