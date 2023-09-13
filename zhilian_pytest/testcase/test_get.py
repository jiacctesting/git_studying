import json

import requests
import pytest
from my_utils.RequestUtils import requests_get
#login_1	登录获取token	登录成功
# https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx02374310523f1868&secret=ceeaeaed3ab07365f5b08e7e72c03f95
# get	json		{"access_token":"72_8QhttGu5YjxZiabZN3BbDomfIRHxRfF7f83pTqY-OtzgpZgtALhKF-O78GD1jYDOt02TQgxlyOmdG4Wd4Mkbd8lw4RrWZcgMEPJKsn3eR3VJIUzE-itreJAO3TUEGPdAAAWYH","expires_in":7200}


def test_login():
    url="https://api.weixin.qq.com/cgi-bin/token"
    data= {"grant_type":"client_credential","appid":"wx02374310523f1868","secret":"ceeaeaed3ab07365f5b08e7e72c03f95"}
    r=requests.get(url,params=data)

    print(r.text)
    print(r.url)


def test_add_tags():
    url="https://api.weixin.qq.com/cgi-bin/tags/create?access_token=72_SdgVX2dfLfw3hJx-1iTU_UyxzDr0M3SVoRa9hp9nHy3ZpZICzXprICXFN9ThTbdg-LR20W7J6C4uzxgNu8Iq0SEBOjlJ1sReUc7JbOCpFH3-w1JDZGBgyFpOWBcIRMgAIAYHC"
    data={
            "tag": {
                "name": "test1221"
            }
        }
    r=requests.post(url,data=json.dumps(data))
    print(r.json())
    print(r.url)

def test_show_tags():
    url="https://api.weixin.qq.com/cgi-bin/tags/get?access_token=72_SdgVX2dfLfw3hJx-1iTU_UyxzDr0M3SVoRa9hp9nHy3ZpZICzXprICXFN9ThTbdg-LR20W7J6C4uzxgNu8Iq0SEBOjlJ1sReUc7JbOCpFH3-w1JDZGBgyFpOWBcIRMgAIAYHC"
    r=requests.get(url)
    print(r.json())

def test_modify_tag():
    url="https://api.weixin.qq.com/cgi-bin/tags/update?access_token=72_SdgVX2dfLfw3hJx-1iTU_UyxzDr0M3SVoRa9hp9nHy3ZpZICzXprICXFN9ThTbdg-LR20W7J6C4uzxgNu8Iq0SEBOjlJ1sReUc7JbOCpFH3-w1JDZGBgyFpOWBcIRMgAIAYHC"
    data={
            "tag": {
                "id": "100",
                "name": "测试999"
            }
        }
    # r=requests.post(url,data=json.dumps(data))
    r=requests.post(url,json=data)
    print(r.json())

def test_delete_tag():
    url="https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=72_SdgVX2dfLfw3hJx-1iTU_UyxzDr0M3SVoRa9hp9nHy3ZpZICzXprICXFN9ThTbdg-LR20W7J6C4uzxgNu8Iq0SEBOjlJ1sReUc7JbOCpFH3-w1JDZGBgyFpOWBcIRMgAIAYHC"
    data={
            "tag": {
                "id": "171"
            }
        }
    # r=requests.post(url,data=json.dumps(data))
    r=requests.post(url,json=data)
    print(r.json())

if __name__ == '__main__':
    pytest.main(["-vs"])