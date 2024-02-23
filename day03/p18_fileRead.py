# file : fileRead.py
# desc : 텍스트 파일 읽기

f = open('./day03/sample.txt',mode='r',encoding='utf-8')
f2 =open('./day03/dest.txt',mode='w',encoding='utf-8')
f3 = open('C:\Windows/PFRO.log',mode='r')
f4 = open('./day03/PFRO.txt',mode='w',encoding='utf-16')
f5= open('./day03/PFRO.txt',mode='r',encoding ='utf-16')
f6 = open('./day03/CHANEGELOG.txt',mode='w',encoding='utf-16')


read1 = f3.readlines()
read = f.readlines()
read2 = f5.readline()

while True:
    read2 = f5.readline()
    if not read2 : break
    print(read2.replace('\n', ''))


print('파일에서 읽은 내용 >', read)

for line in read1:
    print(line)

    
for line in read1:
    print(line.replace('\n',''))
    f4.write(line)

for line in read:
    print(line.replace('\n',''))
    f2.write(line)
###
    
    
f.close()
f3.close()