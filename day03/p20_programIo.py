#file : p20_programio.py
#desc : 프로그램 입출력, 프로그램으로 명령 실행시 파라미터를 받을 수 있음

import sys
args = sys.argv[1:]
for i in args:
    if i == '--version':
        print('Python 3.12.2')
    elif i == 'h':
        print('도움말 >>')
    else:
        print('재입력')
        
    break