import requests
"""
get请求：
    有参数
    无参数
"""
r=requests.get("https://api.github.com/events")
print(r.status_code)

params={
    "shouji":"15911187981",
    "appkey":"0c818521d38759e1"
}
m=requests.get("http://sellshop.5istudy.online/sell/shouji/query",params=params)
print(m.status_code)
print(m.json())


"""
post请求:
    paramas
    json格式
    data格式（form data）
"""
# param={
#     "shouji":"15911187981",
#     "appkey":"0c818521d38759e1"
# }
# r=requests.post("http://sellshop.5istudy.online/sell/shouji/query",params=param)
# print(r.status_code)
#
#
# json_data={
#     "shouji":"15911187981",
#     "appkey":"0c818521d38759e1"
# }
# r=requests.post("http://sellshop.5istudy.online/sell/shouji/query",json=json_data)
# print(r.status_code)
#
# form_data={
#     "text":"hello",
#     "lang":"en",
#     "to":"zn"
# }
# r=requests.post("https://dict.youdao.com/keyword/key",data=form_data)
# print(r.json())
"""
headers
"""
# data={
#     "type":"movie",
#     "tag":"热门",
#     "page_limit":50,
#     "page_start":10
# }
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
# }
# r=requests.get("https://movie.douban.com/j/search_subjects",data=data,headers=headers)
# print(r.status_code)

"""
断言
"""
# def test_one():
#     actual=1
#     expect=2
#     assert actual==expect

"""
pytest+request
"""
def test_mobile():
    params={
            "shouji":"15911187981",
            "appkey":"0c818521d38759e1"
    }
    r=requests.post("http://sellshop.5istudy.online/sell/shouji/query",params=params)
    print(r.status_code)
    print(r.json())
    result=r.json()
    assert r.status_code==200
    assert result["status"]==0
    assert result["msg"]=="ok"
    assert result["result"]["city"]=="北京"


# if __name__ == '__main__':
#     {
#         "code": 0,
#         "data": {
#             "id": "1",
#             "name": "况亲到",
#             "photoUrls": [
#                 "http://dummyimage.com/200x200"
#             ],
#             "category": {
#                 "id": 8440624395335082,
#                 "name": "Dog"
#             },
#             "tags": [
#                 {
#                     "id": 659068040334010,
#                     "name": "dog"
#                 }
#             ],
#             "status": "sold"
#         }
#     }