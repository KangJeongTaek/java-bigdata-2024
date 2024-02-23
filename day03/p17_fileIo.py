#file : p17_fileIo.py
#desc : 파일 입출력


#컴퓨터에서 열면 무조건 닫아야 하는 것
#1. 파일 open(),close()
#2. 네트워크 open(),close()
#3. DB open or connect(),close()

#언어체계 추가 ASCII(한글 cp949), 유니코드(utf-8)
f = open("./sample.txt",mode ='w',encoding='utf-8')
f.write('안녕하세요. 파이썬')
f.write('가즈아')
#파일 쓰기 진행
f.close() #파이썬에서는 옵션이지만 다른 언어에서는 반드시 close() 해줘야한다