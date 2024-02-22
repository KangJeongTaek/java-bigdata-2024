# file : p11_whilecondition.py
# desc : while 반복문
hit = 0
while hit <50:
    hit += 1
    if hit % 3 ==0:
        continue
    else:
        print(f'나무를 {hit:02d}번 찍었습니다.')
    if hit ==10:
        print(f'나무가 넘어갑니다.')
        break # 조건문에 상관없이 반복문 탈출

#무한루프
#hit = 0
#while True:
#    hit += 1
#    print(f'나무를 {hit:02d}번 찍었습니다')
import os

while True:
    os.system('cls')
    select = input('메뉴 입력 1. 입력 , 2. 수정, 3. 검색, 4. 삭제, 5. 종료')
    if select == '1':
        print('데이터를 입력합니다.')
        input()
    elif select == '2':
        print('데이터를 수정합니다')
        input()
    elif select== '3':
        print('데이터를 검색합니다')
        input()
    elif select == '4':
        print('데이터를 삭제합니다')
        input()
    elif select =='5':
        print('종료합니다')
        break
    else:
        print('입력 오류')
        continue