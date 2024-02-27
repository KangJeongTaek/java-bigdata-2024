# file : p34_osDir.py
# desc : 운영체제 디렉토리 확인하기

import os # 운영체제에서 필요한 모듈

def search(dirName):
    try:
        fileNames = os.listdir(dirName) # 결과는 list[str]
        for fileName in fileNames:
            fullName = os.path.join(dirName,fileName)
            if os.path.isdir(fullName):
                search(fullName) #재귀 호출
            else:
                ext = os.path.splitext(fullName)[-1]
                if ext == '.py': # 확장자가 .py인 것만을 출력해라
                    with open(fullName,mode='r',encoding='utf-8') as fp: # with로 파일을 열면 close()가 필요 없다
                        print(f'파일명: {fullName}, 라인 수: {len(fp.readlines())}줄')
    except PermissionError as e:
        print('접근 권한이 없습니다.', e.args)


if __name__ == '__main__':
    search('G:/Source/java-bigdata-2024')