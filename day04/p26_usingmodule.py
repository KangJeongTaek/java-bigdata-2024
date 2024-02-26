# file : p26_usingmodule.py
# desc : 모듈 사용

import calc as c# 나는 calc.py를 사용할 것입니다.
from calc import mul as multy
import Math

#from Math import Math from Math는 모듈 import Math는 클래스 이름

if __name__ == '__main__': ##java의 public static void main(String[] args) 과 동일

    result = c.add(4,10)
    print(result)

    result = multy(19,4)
    print(result)
    print(c.__name__)


    print(__name__) # __main__ = 나는 main 엔트리

    myMath = Math.Math()
    print(myMath.solv(10))
