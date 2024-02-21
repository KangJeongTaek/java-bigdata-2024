# file : p04.list.py
# desc : 리스트

##파이썬엔 배열이 없다. 리스트로 대신함
even = [2,4,6,8,10]
odd = [1,2,3,5,7,9]
print(even)
print(even[4])

even[4] = 20
print(even)

datas = [123,45.6,True,'hello', odd, None] #형지정이 없기 때문에 어떤 자료형이든 다 리스트에 할당 가능

print(datas)

print(even[0] + odd[0])

cpWord = ['Life', 'is', 'short']
print(cpWord[0] + cpWord[2])

print(even[1:4])

##2차원 리스트
# 3행 4열
#[[1,2,3,4]],
#[5,6,7,8],
#[9,10,11,12]]

d2Data = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

print(d2Data)
for i in d2Data:
    print(i)

dm1col1 = [1,2,3,4]
dm1col2 = [5,6,7,8]
dm1col3 = [9,10,11,12]

print(even + odd)
print(odd * 2)

even[3] = 10
print(even)

del even[2] ##값 삭제

print(even)

## 리스트 함수
# append 리스트 제일 뒤에 추가
even.append(30)
print(even)

# insert 원하는 위치 값 추가
even.insert(2, 6) # 인덱스 2에다 6을 추가하겠따

print(even)

# 정렬

origin = [45, 23,9,17,1,5,11,3,20,29, 30]
origin.sort
print(origin)
origin.sort(reverse=True) # 내림차순(descending)
print(origin)

aa = ['a','f','e','b']
aa.reverse()
print(aa)

print(aa.count('a'))
print(aa.index('e'))
bb = [1,3,5,6,7,3,1]

bb.remove(3)
print(bb)

print(even.pop())
print(even.pop())
print(even)

##튜플
#리스트랑 동일, 단 , 삭제, 편집 불가

tVal = (1,3,5,7,9)
