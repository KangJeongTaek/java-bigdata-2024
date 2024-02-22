# file:p05_dict.py
# desc : 딕셔너리 자료형 학습

spiderman = {'name':'Peter Parker','age':18,'weapon':'Web shooter', 'friends':['ironMan','Thor','Captain America']}

print(spiderman)

print(spiderman['name'])

spiderman['job'] = 'CameraMan'

print(spiderman)

del spiderman['friends']

print(spiderman)

print(spiderman.keys())

print(list(spiderman.keys()))

print(spiderman.items())

print(spiderman.get('job')) #딕셔너리 값 가져오기

print('firends' in spiderman) #딕셔너리 안에 키가 있는지 확인
print(spiderman.values())

res = spiderman.pop('job')
print(res)
print(spiderman)

spiderman.clear() #데이터 삭제
print(spiderman)
del spiderman #완전 삭제
# print(spiderman) <- 에러