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

before = 'i wanna go to '
after = 'Korea'
print(before + after) # +는 문자열을 합쳐서 하나의 문자열로 만듦

print(after * 3) # 문자열을 몇 번 반복