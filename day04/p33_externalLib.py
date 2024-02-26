#file : p31_externalLib.py
# desc : 외부라이브러리 사용법
from faker import Faker

dummy = Faker('ko-KR')

print(dummy.name())
print()
print(dummy.address())
print(dummy.profile())

dummyData = [(dummy.profile()) for _ in range(10)]

print(dummyData)