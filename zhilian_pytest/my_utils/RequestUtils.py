import requests
from my_utils.LogUtils import  my_log


# def requests_get(url, paramas=None):
#     r = requests.get(url, params=paramas)
#     dic = {}
#     dic["status_code"] = r.status_code
#     try:
#         dic["body"] = r.json()
#     except Exception as e:
#         dic["body"] = r.text
#     return dic


# def requests_post(url, json=None):
#     r = requests.post(url, json=json)
#     dic = {}
#     dic["status_code"] = r.status_code
#     try:
#         dic["body"] = r.json()
#     except Exception as e:
#         dic["body"] = r.text
#     return dic


class MyRequest:
    def __init__(self):
        self.log=my_log()
        # self.log=my_log("Request")
    def requests_api(self, url, params=None,data=None, json=None, headers=None, cookies=None, method="get"):
        if method == "get":
            self.log.debug("发送get请求")
            r = requests.get(url,params=params,data=data,json=json, headers=headers, cookies=cookies)
        elif method == "post":
            self.log.debug("发送post请求")
            r = requests.post(url, data=data,json=json, headers=headers, cookies=cookies)
        code=r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res=dict()
        res["code"]=code
        res["body"]=body
        return r.text

    def get(self,url,**kwargs):
        return self.requests_api(url,method="get", **kwargs)

    def post(self,url,**kwargs):
        return self.requests_api(url, method="post", **kwargs)


if __name__ == '__main__':
    # m = Requests()
    # r = m.requests_api("https://www.baidu.com", method="post")
    # print(r)
    url = "https://api.weixin.qq.com/cgi-bin/token"
    data = {"grant_type": "client_credential", "appid": "wx02374310523f1868",
            "secret": "ceeaeaed3ab07365f5b08e7e72c03f95"}
    request = MyRequest()
    r = request.get(url, params=data)
    print(r)