
f  = open('test.text',mode='w',encoding='utf-8')
f.write('Life is too short\nyou need java')

f.close

f = open('test.text',mode='r')
body = f.read()
f.close
##단 read()는 텍스트가 길면 문장이 잘려나온다
body = body.replace('java','python')

f = open('test.text',mode='w')
f.write(body)


f.close


f = open('test.text',mode='r')
for line in f.readlines():
    if line.find('python') > -1:
        print(line)



