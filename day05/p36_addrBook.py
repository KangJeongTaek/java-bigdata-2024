# file : p36_addrBook.py
# desc : 콘솔 주소록 프로그램

class Contact:
    def __init__(self,name,phoneNumber,eMail,addr): #생성자
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail
        self.__addr = addr

    def __str__(self) -> str: #사용가아 원하는 형태로 출력
        strRes = (f'이  름 : {self.__name}\n'
                  f'휴대폰 : {self.__phoneNumber}\n'
                  f'이메일 : {self.__eMail}\n'
                  f'주  소 : {self.__addr}')
        return strRes
    

def run():
    first = Contact('홍길동','010-1234-5678','honggildong@google.com','대한민국 함경북도')
    print(first)

def set_contact():
    name,phoneNumber,eMail,addr = input('정보 입력(이름, 휴대폰, 이메일, 주소[구분자/]) : ').split('/')
    print(name,phoneNumber,eMail,addr)
    first = Contact(name,phoneNumber,eMail,addr)
    print(first)

if __name__ == '__main__': # 메인엔트리
    print('프로그램 시작')
    set_contact()
    



print('프로그램 종료')