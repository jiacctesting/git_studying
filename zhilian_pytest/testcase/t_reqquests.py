import pytest
import requests,time

class TestApi:
    access_token=""
    sess=requests.session()

    def test_1(self):
        r=requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx02374310523f1868&secret=ceeaeaed3ab07365f5b08e7e72c03f95")
        # print(r.json())
        print(r)
        print(r.text)
        TestApi.access_token=r.json()["access_token"]

        print(TestApi.access_token)

    def test_2(self):
        url="https://api.weixin.qq.com/cgi-bin/tags/create?access_token="+TestApi.access_token
        json={
              "tag": {
                "name": "hello "+str(time.time())
                    }
              }
        r=requests.post(url,json=json)
        print(r.json())

    def test_3(self):
        url="https://api.weixin.qq.com/cgi-bin/tags/create?access_token="+TestApi.access_token
        # url="https://api.weixin.qq.com/cgi-bin/tags/create?access_token="
        json={
              "tag": {
                "name": "hello "+str(time.time())
                    }
              }
        r=TestApi.sess.post(url,json=json)
        print(r.json())

if __name__ == '__main__':
    pytest.main()
