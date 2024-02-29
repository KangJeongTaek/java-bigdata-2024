# file : p42_jsonHandle.py
# desc : json 읽고/쓰기

import json

# json 읽기
with open('./day07/p42_testData.json',mode='r',encoding='utf-8') as fp:
    data = json.load(fp)

# data로 출력 -> 파이썬 덕셔너리 출력 /json.dumps(data) ->json 형태로 출력


# json 데이터 접근은 파이썬 딕셔너리, 리스트와 동일하게 사용가능
print(data['name'])
print(data['languages'])

superCars = dict()
audi = dict()
audi['price'] = 300_000_000 #3억
audi['year'] = '2020'
audi['type'] = 'eletric'
superCars['audi'] = audi

car = dict()
car['price'] = 1_500_000_000 # 15억
car['year'] = '2019'
car['type'] = 'gasolin'
superCars['porshe'] = car

#json파일 저장
with open('./day07/superCars.json',mode='w',encoding='utf-8') as fp:
    json.dump(superCars, fp,indent='\t')


