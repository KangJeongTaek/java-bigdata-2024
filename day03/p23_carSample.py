# file : p23_carSample.py
# desc : Car클래스 사용해보기

from p22_carClass import Car

myCar = Car('50호 7456') #클래스를 사용, 객체를 한 ㅏ생성(instance)

yourCar = Car('64가 7875')

#print(YourCar)


#print(myCar)

myCar.carNum ='52서 9312'
myCar.company = '현대자동차'
myCar.fuelType = '가솔린'
myCar.carType = '하이브리드'
myCar.color = '흰색'
myCar.releaseYear = 2020

myCar.getColor()
myCar.start()
myCar.accel()
myCar.turnLeft()
myCar.turnRight()
myCar.breakOn()

yourCar.carNum = '87호 8733'
yourCar.start()
print(yourCar.getColor())
print(yourCar)