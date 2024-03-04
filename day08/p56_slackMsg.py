# file : p56.slackMsg.py
# desc : 슬랙으로 스마트폰 메시지 보내기

# 슬랙 URL
'''
1. https://api.slack.com/ 에서 Your apps > Create your first app
2. From Scratch 클릭 - 앱 이름은 영어로만
3. 워크스페이스 선택
4. Incoming Webhooks > On > Add New Webhook to Workspace 클릭 > 채널 선택 > 허용
'''

import requests
import json

slack_url = 'https://****'



headers = {'Content-type':'application/json'}
data = {'text': 'Python에서 보내는 메시지!!'}

res = requests.post(slack_url,headers=headers,data=json.dumps(data))

if res.status_code ==200:
    print('메시지 전송 선공!!')
else:
    print('메시지 전송 실패!!')