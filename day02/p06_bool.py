# file : p06_bool.py
#desc : 붍타입, None 타입 학습

# 참 거짓

a = True
b = False

print(a)
print(type(a))
print(type(1))
print(type(1))
print(type(3.14))
print(type('hi'))
print(type([1,2,3]))
print(type({1,2,3}))
print(type((1,2,3)))
print(type({'key':123}))
print( a== b)
print(a != b)
print(a == (not b))

#참 / 거짓 구분
#빈값,None,0,False 이 외의 값들은 True

print(bool(0)) #False
print(bool(1)) #True
print(bool(-1)) #True
print(bool({1,2,3})) # True
print(bool({})) #False
print(bool('')) #False
print(bool('H')) #True
print(bool(None)) #False

c = None
print(c)

print(a+b)

print(True+False)