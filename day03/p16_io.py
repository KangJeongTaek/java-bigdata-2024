# file : p16_io.py
# desc : 입출력 학습


# res = input('인사말을 적으세요 > ')

# print(res)

# num = int(input('곱할 수나이를 적으세요'))
# type(print(num))
# num = int(num)

# num = int(input('2로 곱할 숫자 입력 > '))
# print(num * 2)
#(a1,a2,a3) = input('합산할 세 값을 입력(구분자는 space)').split(' ')
# 튜플 괄호 중 할당을 받는 쪽의 괄호()는 생략 가능
#a1,a2,a3 = int(a1),int(a2),int(a3)

(a1,a2,a3) = map(int,input('합산할 세 값을 입력(구분자는 space)').split(' '))
sum = a1+a2+a3
print(sum)