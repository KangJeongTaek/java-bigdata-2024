# 빅데이터 언어 2024
빅데이터 자바 개발자 Python 학습 repository

## 1일차
- ### 파이썬 개발환경

    - [github](https://giyhub.com/) 가입

    - [git](https://git-scm.com/download/win) 설치

    - [githubdesktop](https://desktop.github.com/) 설치

    - [Python](https://python.org) 설치

    - [visualstudiocode](https://code.visualstudio.com/) 설치

    - [나눔고딕 코딩 글꼴](https://github.com/naver/nanumfont) 설치


- ### 파이썬 학습

    - #### 01 파이썬 개요

        - ##### 01-1 파이썬이란?
            - 1990년, 네덜란드계 귀도 반 로섬이 발표한 고급 프로그래밍 언어

        - ##### 01-2 파이썬의 특징
            - 인간다운 언어
            - 문법이 쉬워 빠르게 배울 수 있다
            - 무료이지만 강력하다
            - 간결하다
            - 프로그래밍을 즐기게 해 준다
            - 개발 속도가 빠르다

        - ##### 01-3 파이썬으로 할 수 있는 것
            - 웹 프로그래밍
            - 인공지능과 머신러닝
            - 수치 연산 프로그래밍과 데이터 분석
            - 데이터베이스 프로그래밍
            - 시스템 유틸리티 제작하기
            - GUI 프로그래밍
            - C/C++ 과 연결하기
            - 사물 인터넷
        
        - ##### 01-4 파이썬으로 할 수 없는 일
            - 시스템과 밀접한 프로그래밍 영역'
            - 모바일 프로그램 <- 현재는 가능


    - #### 02 파이썬 기초, 자료형
        
        - ##### 02-1 숫자형
            - 숫자 형태로 이루어진 자료형
                ```python
                123,345,0 # 정수
                123.45,-1234.5,3.4e1 0#실수
                0o34,0o25 #8진수
                0x2A, 0xFF #16진수
                ```
            - 사칙 연산
                ```python
                # 자바와 크게 다를 것 없지만, 나누기는 3가지로 분류된다.
                # '/' <- 정확하게 실수로 나누기
                # '//' <- 정수로만 나누기
                # '%' <- 정수로 나눈 나머지
                # '**' <- 제곱 연산
                ```

        - ##### 02-2 문자열 자료형
            - 파이썬에서 \n, \t 이외의 이스케이프 문자는 잘 사용되지 않는다.
            - 여러 줄 문장을 쓸 때
                ```python
                # """|| ''' || \n 가능
                ```
            - 문자열 연산
                ```python
                # +,*
                # +는 문자열을 합쳐서 하나의 문자열을 만듦
                # *는 문자열을 정수만큼 반복
                ```
            - 문자열 길이 구하기
                ```Python
                ## - len("문자열")
                ```
            - 문자열 인덱싱과 슬라이싱
                ```python
                # "문자열"[인덱스]
                # cp[8] = 'd'  잘못된 문법  # 문자열은 배열이긴 하나, 값을 변경할 수 없다
                # : 뒤에 있는 숫자는 항상 +1
                ```

            - 문자열 포매팅(format string)
                ```python
                ## 파이썬에서는 %d,%s,%c 등 포맷스트링용 연산자 사용 빈도가 낮다.
                ```
            - format 함수로 포맷팅(가장 일반적)
                ```Python
                ## 날짜를 포맷으로 만들 때
                month = 2
                day = 21
                hour = 15
                mins = 18
                print('오늘은 {0:02d}월 {1:02d}일 {2:02d}시 {3:02d}분입니다.'.format(month,day,hour,mins))

                income = 6000000 # 육백만원

                print('이번 달 매출액은 {0:,d}원 입니다.'.format(income))

                PI = 3.1415926536
                print('파이는{0:.2f}'.format(PI))
                print('{0:f}'.format(PI)) #실수형은 d(정수형 포맷팅) 불가
                ```

            - f문자열 포매팅
                ```Python
                name = '홍길동'
                age = 30
                print(f'나의 이름은{name}입니다. 나이는 {age}입니다.')
                ```

            - 문자열 관련 함수들
                ```Python
                a = 'Life is too short, You need Python'
                print(a.count('Life'))
                print(a.count('o')) # 문자열 중 o의 개수
                print(a.find('sh')) #문자가 처음 나온 위치 < 찾지 못 하면 -1 반환
                print(a.index('t')) #첫번째 t의 위치 < 찾지 못 하면 오류 #index()는 count()로 갯수가 0이 아닐 때만 호출]
                print(','.join('abcde')) #문자열 abcde 사이에 ','를 삽입
                print(a.upper()) #대문자 만들기
                print(a.lower()) #소문자 만들기
                print(a.capitalize()) #제일 첫번째 글자만 대문자로 만들기
                
                origin = '      Hi        '
                print(f'++{origin}++')
                print(f'++{origin.lstrip()}++')
                print(f'++{origin.rstrip()}++')
                print(f'++{origin.strip()}++')
              
                 print(cp.replace('too','').replace(' short','long'))
                # cp.split(' ') 공백을 기준으로 문자열을 잘라 배열로 반환
                ```
                    


        - ##### 02-3 리스트,튜플 자료형
            - 리스트 - 수정, 삭제 가능 []
            - 튜플 - 수정, 삭제 불가 그 외에는 리스트와 동일 ()


        
## 2일차

- ### 파이썬 학습

    - #### 02 파이썬의 기초, 자료형
        - ##### 02-4 딕셔너리, 집합
            - 딕셔너리 : 단어 그대로 '사전'이라는 뜻
            - Key와 Value를 한 쌍으로 가지는 자료형
                ```python
                {Key1: Value1,Key2:Value2,Key3:Value3, ...}

                dic = {'name':'pey','phone':010-9999-1234','birth':'1118}
                ```
            - 딕셔너리 출력 방법
                ```python
                print(dic['name'])
                ```
            - 딕셔너리 추가, 삭제
                ```python
                dic['home'] = 'Busan' # 값 추가
                del dic['name'] #값 삭제
                ```
            - 주의 사항
                - 키 값은 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다
                - 키값은 리스트로 쓸 수 없다. 그리고 되도록 문자로 사용하도록 하자

            - 딕셔너리 관련 함수
                - 딕셔너리에 현재 존재하는 키 목록
                    ```python
                    dic.keys()
                    ```
                - 딕셔너리의 Key,Value 한 쌍 얻기
                    ```python
                    dic.items()
                    ```
                -  딕셔너리 값 가져오기
                    ```python
                    dic.get('name')
                    ```
                - 딕셔너리 안에 키가 있는지 확인
                    ```python
                    'name' in dic
                    ```
                - 딕셔너리에 현재 존재하는 값 목록
                    ```python
                    dic.values()
                    ```
                - 딕셔너리에 현재 존재하는 값 삭제
                    ```python
                    dic.pop('name') # 삭제한 값 리턴

                    dic.clear() ## 데이터 삭제

                    del dic ## 완전 삭제
                    ```

            - 집합 : 중복을 허용하지 않으며 , 순서가 없다.
                ```python
                set([1,2,3,4,3,2,1]) = {1,2,3,4}
                ```
        - ##### 02-5 불 자료형
            - 참 또는 거짓
                ```python
                a = True # T 대문자
                b = False # F 대문자
                ```
            - 값이 있는 자료형은 참이며 값이 없으면 거짓이다
                ```python
                print(bool(0)) #False
                print(bool(1)) #True
                print(bool(-1)) #True
                print(bool({1,2,3})) # True
                print(bool({})) #False
                print(bool('')) #False
                print(bool('H')) #True
                print(bool(None)) #False

                #빈값,None,0는 False 이 외의 값들은 True
                True + False #가능  <- 1나옴
                ```

        - ##### 02-6 None형
            - None
                ```python
                c = None
                #c + 1  <- 불가능
                ```

        - ##### 02-7 변수
            - 얕은 복사
                ```python
                a = [1,2,3]
                b = a #얕은 복사, 같은 주소값을 공유한다.
                print(id(a))
                print(id(b))
                del b[2]
                print(a) #a 안에 있는 3도 삭제 된다.
                ```
            - copy 모듈 이용하기(깊은 복사)
                ```python
                from copy import copy
                a = [1,2,3]
                b = a
                d = copy(a) #깊은 복사, 다른 주소값을 가진다.
                del d[2]
                print(a)
                ```
    - #### 03 제어문
        - ##### 03-1 if 문
            - 파이썬에서는 들여쓰기 항상 신경쓰기!
            ```python
            indentation(들여쓰기) == space 4
            if 조건문 :
                실행문_문장1
                실행문_문장2
                ...
            elif 조건문 :
                실행문_문장1
                실행문_문장2
                ...
            else :
                실행문_문장1
                실행문_문장2
                ...
            ```
            - and , or, not
                ```python
                #x and y | x와 y 둘 다 True여야 True
                #x or y | x와 y 둘 중 하나가 True여도 True
                #not | True는 False로 False는 True로

                ##print() end옵션, sep옵션
                print(1 in [1,3,5,7,9], end='') # True13579,test
                print('13579','test',sep=',')
                ```

            - 조건부 표현식
                ```python
                #파이썬에선 조건 연산자를 잘 안 쓴다
                'hi' if True(조건식) else 'bye'
                ```

        - ##### 03-2 for 문
            ```python
            #for item in 반복할 객체(iterable이라고 불린다.):
            #   ...

            ```

            ```python
            range(0,10)
            print(list(range(0,10))) #0부터 9까지

            print(list(range(0,11,2))) #0부터 짝수로

            print(list(range(1,10,2))) #1부터 홀수로

            print(list(range(10,0,-2))) # 10,8,6,4,2

            print(list(range(4,101,4))) # 4부터 4의 배수를 100까지 표현


            res = 0
            for i in range(1,11):
                res += 1 ## 55

            ```

            ```python
            ##list comprehension / 리스트 내포
            [i for i in range(10)]
            ```
        - ##### 03-3 while 문
            ```python
            while 조건문:
                수행할문장1
                수행할문장2
                ...
            ```

    - #### 04 파이썬의 입출력
        - ##### 04-1 함수
            - 함수 만들기
            ```python
            def plus(a,b):
                res = a+b:
                return res
            ```
            - 함수 pass
            ```python
            def funName():
                pass
            ```
            - 함수 기본 인수 지정
            ```python
            def power(a,b=10):
                res = a**b
                return res

            ##def power(a=2,b): 이건 안됨. 기본 인수는 뒤에서부터 지정
            ```

            - 매개 변수의 개수를 모를 때(동적 매개변수)
            ```python
            def plus_many(*items):
                result =0
                for item in items:
                        result += item
                    return result

            plus_many(1,2,3,4)
            plus_many(1,2)
            ```
            - 계산기
            ```python
            def calcurator(mode, *args):
                    if mode == 'a':
                        result = 0
                    for i in args:
                            result += i
                    elif mode == 'n':
                        result = args[0]
                    for i in args[1:]:
                            result -= i
                elif mode == 'm':
                    result = 1
                    for i in args:
                        result *= i
                elif mode == 'd':
                    result = args[0]
                    for i in args[1:]:
                        result /= i
                return result
            ```
            - 키워드 매개 변수(딕셔너리 생성)
            ```python
            def print_kwargs(**items):
                print(items)
            ```

            - return이 여러개인 함수. 튜플로 리턴
            ```python
            def calc2(a,b):
                result1 = a+b
                result2 = a-b
                result3 = a*b
                result4 = a/b

                return result1,result2,result3,result4
            ```
            - 람다(익명 함수)
            ```python
            add = lambda a,b:a+b
            print(add(5,4))
            ```

## 3일차
- ### 파이썬 학습
    - #### 04 파이썬의 입출력
        - ##### 04-2 사용자 입출력
            - input
                - input으로 받는 값은 모두 문자열
                ```python
                num = input('곱할 수나이를 적으세요 > ') # num = int(input('숫자 입력 > '))
                type(print(num))
                num = int(num)
                print(num * 2)
                ```

                - 여러 값을 입력할 때
                ```python
                (a1,a2,a3) = input('세 값을 입력(구분자는 space)').split(' ')
                #튜플 자료형이므로 바로 int로 변경할 수 없다
                # a1,a2,a3 = int(input('세 값을 입력(구분자는 space)').split(' '))
                a1,a2,a3 = int(a1),int(a2),int(a3)
                sum + a1+a2+a3

                #map을 사용할 수도 있다. map(function, iterable)
                (a1,a2,a3) = map(int,input('세 값을 입력(구분자는 space)').split(' '))
                ```

            - print
            ```python
            print()
            ```

        - ##### 04-3 파일 입출력
            - 파일 생성하기
            ```python
            f = open("파일경로/새파일.txt",mode='w',encoding='utf-8')
            f.close()

            #컴퓨터에서 열면 무조건 닫아야하는 것
            #1. 파일 open(),close()
            #2. 네트워크 open(),close()
            #3. DB open or connect(),close()
            ```
            
            - 파일 열기 모드
            ```python
            'r' 읽기 모드
            'w' 쓰기 모드 <- 매번 새로운 파일 생성
            'a' 추가 모드 <- 기존 파일에 내용 추가
            ```

            - 상대 경로 절대 경로
            ```python
            # 상대 경로
            ./day03/sample.txt # .의 의미는 자기 자신 ..은 부모

            # 절대 경로
            G:/Source/java-bigdata-2024/day03/sample.txt
            ```

            - 파일 쓰기
            ```python
            f = open("./sample.txt",mode='w',encoding='utf-8')
            f.write('안녕하세요. 파이썬\n') #줄바꿈 하려면 \n을 작성해줘야 한다
            f.write('가즈아')
            f.close()
            # 쓰기는 출력이다
            ```

            - 파일 읽기
            ```python
            f = open('./sample.txt',mode='r',encoding='utf-8')
            read = f.readline() < - 한줄만 읽기
            read1 = f.readlines() <- 여러줄 읽기 ,리스트로 반환
            read3 = f.read() <- 전체 텍스트를 문자열로 반환, 단 텍스트가 길면 문장이 잘려나온다

            for line in read1:
            print(line.replace('\n',''))

            while True:
                if not read : break
                print(read.replace('\n',''))

            f.close()
            ```
        
        - ##### 04-4 프로그램 입출력
        ```python
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
        ```
    - #### 05 객체지향
        - ##### 05-1 클래스
            - 클래스 생성
            ```python
            class (클래스 이름):
            ```

            - 멤버 변수
            ```python
            __변수이름 = 값 #__는 private를 의미
            ```
            - 메서드
            ```python
            #메서드의 입력값에 반드시 첫번째로 self를 넣어줄 것
            ```

            - 매직 메서드
            ```python
            def __init__(self) -> None:  # 생성자  ->None 리턴 할 게 없음
                실행문
            def __str__(self) -> str# 객체 변수를 print()할 때 출력 커스터마이징 함수
                실행문
                return
            ```

            - 상속
            ```python
            class 자식 클래스(부모 클래스): #상속 부모 클래스를 상속받는 자식 클래스 선언
            ```


## 4일차
- ### 파이썬 학습
    - #### 05 객체지향
        - ##### 05-2,3 모듈, 패키지
            - 모듈
                - 무조건 모듈이 클래스로 만들 필요는 없다.
                - 파이썬에서 모듈은 하나의 .py 파일이다.
                ```python
                import calc(모듈이름) as c(사용할 이름)

                result = c.mul(10,7)

                from calc import mul #mul() 함수명만 쓰면 됨
                result = mul(10,7)
                ```

                - if __name__ = "__main__" 의 의미

                - 다른 파일에서 모듈 불러오기

                - 다른 디렉토리에 있는 모듈 불러오기
                ```python
                from day03.p22_carClass import Car
                ```

            - 패키지
                - 관련 있는 모듈의 집합
                - 디렉토리와 파이썬 모듈로 이루어진다

        - ##### ★★ 05-4 예외 처리 / 디버깅
            - 오류(Error) : 코드상 빨간색(노란줄) 밑줄이 그어지는 것
            - 예외(Exception) : 프로그램 실행 중에 생기는 오류(비정상적 종료)
            - 예외와 오류는 구분해야 한다.
            - 예외 처리 문법
            ```python
            try: #예외 발생 가능한 실행문
                ~~~
            except: # 예외가 발생한다면 실행할 것
                ~~~
            else: # 예외가 발생하지 않는다면 실행할 것
                ~~~
            finally: # 예외 발생 여부에 상관없이 항상 실행할 것
                ~~~
            ```
            - 예외를 일부러 발생시키기
            ```python
            raise NotImplementedError
            ```

            - 디버깅
                - 디버깅 하면서 예외를 찾고 거기에 예외 처리
                - F9 중단점
                - F5 디버깅
                - F10 한줄 씩 실행
        
        - ##### 05-5 내장 함수
            -
            ```python
            이미 있는 것을 다시 만드느라 시간을 낭비하지 말라.
            ```
            - 자주 쓰는 내장 함수
            ```python
            # abs() <- ()안의 수의 절대값(absolute)
            # all(iterable) <- 요소 중 하나라도 거짓이 있으면 False를 리턴 / 모두 참이면 True 리턴
            # chr() 아스키나 유니코드 값을 받아서 글자로 변경
            # ascii() 영문자, 문자를 아스키숫자와 유니코드숫자로 변경
            # dir() 객체가 지닌 변수, 함수를 알려주는 함수
            # divmod() 나누기의 몫, 나머지를 한 번에 구해주는 함수
            # ★ enumerate(iterable) 인덱스 값을 포함하는 enumerate 객체를 리턴. 보통 for 문과 함께 사용한다.
            # eval(expression) 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결과값을 리턴
            # hex() 10진수를 16진수로 문자열 변환하여 리턴
            # ★ map(f, iterable) 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴
            # max(iterable) iterable의 요소 중 최댓값 리턴
            # oct() 정수를 8진수 문자열로 바꾸어 리턴
            # ord() ascii와 동일
            # round(숫자,[ndigits]) 반올림
            # sum(iterator) iterable의 요소를 더한 값을 리턴
            # tuple(iterable) 반복 가능한 데이터를 튜플로 바꾸어 리턴
            # ★ type(object) 입력값의 자료형을 리턴
            # zip(iterable) 동일한 개수로 이루어진 데이터를 묶어서 리턴
            ```

        - ##### 05-6 표준 라이브러리
            - 자주 쓰는 표준 라이브러리
            ```python
            import datetime
            # datetime.date(년,월,일) 연, 월, 일로 날짜를 표현
            # datetime.datetime.now() < - 정말 자주 사용

            import time
            # time.localtime()
            # time.sleep(숫자) 숫자만큼 간격을 두고 루프 실행

            import random
            # random.random() 0에서 1 사이의 실수 중에서 난수 값 리턴
            # random.randint(숫자,숫자) 숫자와 숫자 사이의 정수 중에서 난수 값 리턴

            import urllib
            # 웹사이트 데이터 가져오기
            ```

        - ##### 05-7 외부 라이브러리
            - pip(피아이피)
            - pip install 이름
            - ex) faker, requests, beautifulsoup4
            

## 5일차
- ### 파이썬 학습
    - #### 파이썬 응용
        - ##### OS 내 디렉토리 검색
            - import os #OS에서 필요한 모듈

        - ##### 아스키 및 유니코드
             - 인코딩하기
             ```python
             a = 'Life is too short'
             b = a.encode('utf-8')
             type(b) # <class bytes>
             ```

        - ##### 주소록 앱 만들기

            ```python
            class Contact:
                def __init__(self,name,phoneNumber,eMail,addr): #생성자
                    self.__name = name
                    self.__phoneNumber = phoneNumber
                    self.__eMail = eMail
                    self.__addr = addr

                def __str__(self) -> str: #사용자가 원하는 형태로 출력
                    strRes = (f'이  름 : {self.__name}\n'
                            f'휴대폰 : {self.__phoneNumber}\n'
                            f'이메일 : {self.__eMail}\n'
                            f'주  소 : {self.__addr}')
                    return strRes
                
                def getInfo(self):
                    return self.__name,self.__phoneNumber,self.__eMail,self.__addr
                
                def isNameExist(self,name): # 연락처 여부 확인
                    if self.__name == name:
                        return True
                    else:
                        return False
            ```

            ![주소록앱](https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/bigdata01.gif)

        - ##### 윈도우 앱 만들기(Tkinter, PyQt)
            - PyQt5 -> Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
            - Qt -> C,C++에서 사용할 수 있는 GUI(WinApp) 프레임워크(멀티플랫폼)
                - 설치 pip install PyQt5
                - './day05/p37_qtApp.py' 참조
                ![QtApp](https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/bigdata02.png)

## 6일차
- ### 파이썬 학습
    - #### 파이썬 응용
        - ##### 윈도우 앱 만들기(PyQt)
            - PyQt를 기본적 방법부터 차근차근

                [PyQt 위키독스](https://wikidocs.net/book/2165) 학습

                [QtDesigner 위키독스](https://wikidocs.net/book/2944) 학습

                [PyQt](https://youneedawiki.com/app/page/1jZnNNl4biKk3kjpcR4BfKhTO54BJf8QM) 참조

            - PyQt5 학습 이어서
                - QWidget 자식 클래스 종류 학습

                ![Qlabel](https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/bigdata03.gif)

                - [공공데이터포털](https://www.data.go.kr/)
                
                - [네이버 디벨로퍼](https://developers.naver.com/main/)

                - 네이버 API로 뉴스 검색앱
                ![네이버 API로 뉴스 검색 앱](https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/bigdata04.png)
                

## 7일차
- ### 파이썬 학습
    - #### 파이썬 응용
        - ##### PyQt5 계속
            - Naver 뉴스API 검색 앱 마무리

        - ##### json 학습
            - data로 출력 -> 파이썬 덕셔너리 출력 /json.dumps(data) ->json 형태로 출력


            - json 데이터 접근은 파이썬 딕셔너리, 리스트와 동일하게 사용가능
        - ##### PyQt5
            - 스레드 학습

                ![스레드](https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/bigdataThread.gif)

                ![스레드비교](https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/bigdata05.png)

            - QR코드 생성기

                ![Qr코드](https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/KangJeongTaekPython2024QrCode.png)

            - 번역기 앱

                ![번역기](https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/bigdata07.png)

## 8일차
- ### 파이썬 학습

    - #### 파이썬 응용

        - ##### 파이썬 자동화
            - PyAutoGui 모듈(마웃, 키보드, 화면캡쳐)

            - 슬랙 webhook로 모바일 메시지 전송

                <img src="https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/bigdata08.jpg" width="250" height = "310">

                <!-- html 태그로 이미지를 삽입하면 문제 없음 -->

                <img src="https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/bigdata09.jpg" width ="250" height = "310">


                <!-- ![슬랙webhook](https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/bigdata08.png) -->

                <!-- ![슬랙message](https://github.com/KangJeongTaek/java-bigdata-2024-Python/blob/main/images/bigdata09.png) -->
## 9일차
