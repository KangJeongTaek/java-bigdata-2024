# file: p03_string.py
# desc: 문자열 자료형과 연산

a = "Hello World"
print(a)
b = 'Hello World'
print(b)

c = "Hello, 'Ashley'"
print(c)
#되도록이면 파이썬에서는 이스케이프 문자를 잘 쓰지 않는다. \n ,\t 정도만

#문장을 여러 줄 쓰고 싶으면
d = 'Hello~'\
"I'm JeongTaek"\
'Nice to meet you'
print(d)

# 문장을 여러줄 쓸 때에는 ''',"""
d= '''hello
I'm
Nice to meet you, too.'''

print(d)

# 문자열 연산은 +,*

before = 'I wanna go to '
after = 'Korea'
print(before + after) # +는 문자열을 합쳐서 하나의 문자열로 만듦

print(after * 3) # 문자열을 몇 번 반복


##문자열 길이 구하기
print('글자길이 = ' ,len(before))
print('한글글자길이', len('안녕하세요'))



##문자열 인덱싱과 슬라이싱
cp = 'Life is too short, You need Python'

#슬라이싱
print(cp[8])
print(cp[17])

# cp[8] = 'd' # 문자열은 배열이긴 하나, 값을 변경할 수 없다
print(cp[12:16 +1]) # : 뒤에 있는 숫자는 항상 +1

print(ascii('안'), ascii('녕'),ascii('하'),ascii('세'),ascii('요'))

# 기존 문자열로 새로운 문자열을 만들 때는 슬라이싱, 다른 문자열로 대체
print(cp[0:7], 'long', cp[17:])

print(cp[-1])
print(cp[-6:-1])
print(cp[-6:])
print(cp[-11:-7])