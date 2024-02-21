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

# 다른 언어에는 없는 마이너스 슬라이싱
print(cp[-1])
print(cp[-6:-1])
print(cp[-6:])
print(cp[-11:-7]) #-로 슬라이싱 할 때도 : 뒤에는 +1을 해줘야 한다

## 문자열 포매팅 (format string)
##파이썬에서는 %d,%s,%c 등 포맷스티링용 연산자 사용 빈도가 낮다.

temp = 21
print('현재 온도는 %d도 입니다.'%temp)
temp = 17
print('현재 온도는 %d도 입니다.'%temp)

## format 함수로 포맷팅(가장 일반적)

print("현재 온도는 {0}도 입니다." .format(temp))

## 날짜를 포맷으로 만들 때
month = 2
day = 21
hour = 15
mins = 18
print('오늘은 {0:02d}월 {1:02d}일 {2:02d}시 {3:02d}분입니다.'.format(month,day,hour,mins))

income = 6000000 # 육백만원

print('이번 달 매출액은 {0:,d}원 입니다.'.format(income))

PI = 3.1415926536
print('파이는{0:.2f}'.format(PI))
print('{0:f}'.format(PI)) #실수형은 d(정수형 포맷팅) 불가

# f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은{name}입니다. 나이는 {age}세 입니다.')

name = '강정택'
age = 29
cont =f'나는 {name}이고, 나이는 {age}세 입니다.'
print(cont)
print(f'나는 {name:>10}이고, 나이는 {age:03.1f}세 입니다.') # 정수는 f포맷 사용가능. 실수는 d포맷 사용 불가능


## 문자열 관련 함수들

a = 'Life is too short, You need Python'
print(a.count('Life'))
print(a.count('o')) # 문자열 중 o의 개수
print(a.find('sh')) #문자가 처음 나온 위치 < 찾지 못 하면 -1 반환
print(a.index('t')) #첫번째 t의 위치 < 찾지 못 하면 오류 #index()는 count()로 갯수가 0이 아닐 때만 호출]
print(','.join('abcde')) #문자열 abcde 사이에 ','를 삽입
print(a.upper()) #대문자 만들기
print(a.lower()) #소문자 만들기
print(a.capitalize()) #제일 첫번째 글자만 대문자로 만들기

origin = '      Hi        '
print(f'++{origin}++')
print(f'++{origin.lstrip()}++')
print(f'++{origin.rstrip()}++')
print(f'++{origin.strip()}++')

print(cp.replace('too','').replace(' short','long'))
cpwords = cp.split(' ')
print(cpwords)


