#file : p27_exceptionHendle.py
#desc : 에외처리
# 오류(Error) : 코드상 빨간색(노란줄) 밑줄이 그어지는 것
# - 예외(Exception) : 프로그램 실행 중에 생기는 오류(비정상적 종료)
# try except는 다주응로 사용지 속도에 저하가 올 수 있다 
try:
    with open('./sanple.txt',mode='r',encoding='utf-8') as f:
        pass
except:
    print('파일 오픈 예외 발생!')

try:
    f = open('./sanple.txt',mode ='r' , encoding='utf-8')
except:
    print('파일 오픈 예외발생!!')
else: #오류가 없는 경우에만 수행
    f.close()
# finally:
#     try:
#         f.close()
#     except NameError as e:
#         print('파일 오픈 실패')


try:
    print(5/0)
except ZeroDivisionError as e:
    print('나누기 예외 발생')
finally:
    pass
a, b = 5,3

if a > b:
    print(True)