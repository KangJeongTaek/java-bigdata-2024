# file:p07_variable.py
# desc : 변수에 대하여

from copy import copy
a= [1,2,3]
print(id(a))

b = a
print(id(b))

c= 1
d= c
print(id(c))
print(id(d))
e = [1,2,3]
print(id(e))

e = copy(a)