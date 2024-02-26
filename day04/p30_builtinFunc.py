#file :  p30_builtinFunc.py
#desc : 내장 함수

print(abs(-5))

print(all([1,2,3,4,4<2]))

print(chr(65))

print(chr(44032))

print(0xac00)
print(ascii('가'))
print(dir(list()))
print(dir(dict()))
print(dir(tuple()))
a = [1,2]
a.append(3)


print(divmod(7,2))

for i in ['Hello', 'World','Python']:
    print(i)

for i, data in enumerate(['Hello', 'World','Python']):
    print(f'{i}번 째 값은 {data}입니다.')

print(eval('sum([1,2,3])'))

print(hex(255))

a = [1.0,2.0,3.0,4.4]
print(list(map(int,a)))