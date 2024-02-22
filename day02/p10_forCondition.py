#file : p10_forCondition.py
# desc : for 반복문

a = [1,2,3,4,5]

print(type(a))

for i in a:
    print(type(i), end=' ')


for i in ['one','two','three']:
    print(type(i), end=' ')

b = [(1,2),(3,4),(5,6)] #tuple의 리스트

for i in b:
    print(type(i),end ='')

print()
for first,second in b: #튜플의 괄호는 생략가능
    print(first,second)

c = {'key1':'value','key2':'value2'}

for i in c:
    print(c[i])

grade = [90,80,50,70,10]
sum = 0
for i in grade:
    sum += i
    print(sum)
    print(sum // len(grade))

print(range(0,10))

for i in range(0,10):
    print(i, end = " ")

print()
print(list(range(0,10)))

res = 0
for i in range(1,11):
    res += 1 ## 55

##list comprehension / 리스트 내포
#list(range()) 만으로도 리스트를 생성 할 수 있으나 여러 조건으로 리스트를 생성할 떄는 list comprehension을 사용한다.
print([i for i in range(10)])

print([num *3 for num in range(1,1001) if num % 10 ==0])