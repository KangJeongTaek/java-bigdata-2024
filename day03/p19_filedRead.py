f5= open('G:/Source/java-bigdata-2024/CHANGELOG.md',mode='r',encoding ='utf-8')
f6 = open('./day03/CHANEGELOG.txt',mode='w',encoding='utf-8')

while True:
    read = f5.readline()
    if not read : break # 더 이상 읽을 값이 없으면 반복문 탈출
    print(read.replace('\n',''))

f5.close()