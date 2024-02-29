# file : p42_jsonHandle.py
# desc : json 읽고/쓰기

import json

with open('./day07/p42_testData.json',mode='r',encoding='utf-8') as fp:
    print(fp.readlines())