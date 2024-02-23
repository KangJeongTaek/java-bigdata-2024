#file : p22_carClass.py
#desc : 객체지향 클래스 학습

class Car:
    __carNum =''
    company =''
    __releaseYear = 1960
    __color = '흰색'
    __carType = ''
    __fuelType = '가솔린'
    

    def __init__(self, carNum) -> None: # 생성자 ->None 리턴할 게 없음
        self.__carNum = carNum
        print(f'{self.__carNum} 客体を生成します')

    def __str__(self) -> str: # 객체 변수를 print()할 떄 출력 커스터마이징 함수
        return f'제 차는 {self.company}, {self.__carNum} 입니다.'
    
    def getColor(self) -> str:
        msg = f'{self.__color}'
        return msg

    def start(self):
        print(f'{self.__carNum}이(가) 시동을 겁니다.')

    def accel(self):
        print(f'{self.__carNum}, 엑셀을 밟습니다')

    def breakOn(self):
        print(f'{self.__carNum},브레이크를 밟습니다')

    def turnLeft(self):
        print(f'{self.__carNum},좌회전합니다.')
    
    def turnRight(self):
        print(f'{self.__carNum},우회전합니다.')







