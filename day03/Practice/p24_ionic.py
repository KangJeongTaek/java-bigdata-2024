# file : p25_ionic.py
# desc : 클래스 상속

from p22_carClass import Car

class ionic(Car): # 상속
    def __init__ (self,carNum,company,color,carType,fuelType):
        super().__init__(carNum,company,color,carType,fuelType)
    
    __fuelRate = 0.0 # 연비

    def setFuelRate(self,rate):
        self.__fuelRate = rate

    def getFuelRate(self) -> float:
        return self.__fuelRate
    
    def getColor(self) -> str:
        parent_color = super().getColor()
        return f'소중한 제 차는 {self._Car__color}입니다.' # 이름 맹글링


myCar =ionic('54라 9537','하이','흰색','타입',574)
myCar.company = '기아자동차'
myCar.setFuelRate(23.5)
print(myCar)
print(myCar.getColor())
print(f'내 차의 연비는 {myCar.getFuelRate()}km/1 입니다')