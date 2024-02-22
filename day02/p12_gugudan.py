# file : p12_gugudan.py
# desc : 구구단 프로그램

print('구구단 프로그램 v99')
for i in range(1,10):
    print()
    print(f'---{i}단---')
    print()
    for j in range(1,10):
        print(f'{i} x {j} = {(i*j):02d}',end = '\t')
    print()


