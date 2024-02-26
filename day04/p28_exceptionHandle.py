# file : p28_exceptionHandle
# desc : 예외처리2

# while True:
#     try:
#         select = int(input('메뉴입력 1. 저장, 2. 검색, 3. 종료 >> '))
#         if select == 1:
#             print('저장')
#         elif select == 2:
#             print('검색')
#         elif select == 3:
#             print('종료')
#             break
#         else:
#             continue

#     except :
#         print('숫자만 입력하세요.')

#     finally:
#         pass

class Chicken:
    def fly(self):
        raise NotImplementedError
    
koko = Chicken()
try:
    koko.fly()
except Exception as e:
    print('닭은 날 수 없습니다.',e.args) # NotIplementedError는 추가 예외 메시지가 없다