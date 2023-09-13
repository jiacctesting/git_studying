import json

import requests
import pytest
from my_utils.RequestUtils import requests_get,requests_post,MyRequest
from configs.conf import MyConfigYaml
# @pytest.mark.skip
def test_login():
    # url="https://api.weixin.qq.com/cgi-bin/token"
    url_path=MyConfigYaml().get_conf_url()
    url=url_path+"/token"
    data= {"grant_type":"client_credential","appid":"wx02374310523f1868","secret":"ceeaeaed3ab07365f5b08e7e72c03f95"}
    request=MyRequest()
    r=request.get(url,params=data)
    print(r)

# @pytest.mark.skip
def test_add_tags():
    url_path = MyConfigYaml().get_conf_url()
    url = url_path +"/tags/create?access_token=72_jvnA-WUls6l9DhrYXclVLCtKk41CmAPSpvS7Xit5Ug-7Gd6qRxQN55co3dZUxuDp5aalwZ5AcRygAngShWiDVLTWTBQ-r0oYs8qNkNt7CW5P3ws5Kd-fcj8JjM0CYKfAJAQMY"
    data={
            "tag": {
                "name": "test81"
            }
        }
    # r=requests_post(url,data)
    request=MyRequest()
    r=request.post(url,json=data)
    print(r)
# @pytest.mark.skip
def test_show_tags():
    url_path = MyConfigYaml().get_conf_url()
    url = url_path +"/tags/get?access_token=72_jvnA-WUls6l9DhrYXclVLCtKk41CmAPSpvS7Xit5Ug-7Gd6qRxQN55co3dZUxuDp5aalwZ5AcRygAngShWiDVLTWTBQ-r0oYs8qNkNt7CW5P3ws5Kd-fcj8JjM0CYKfAJAQMY"
    # r=requests_get(url)
    request=MyRequest()
    r=request.post(url)
    print(r)
# @pytest.mark.skip
def test_modify_tag():
    url_path = MyConfigYaml().get_conf_url()
    url = url_path +"/tags/update?access_token=72_jvnA-WUls6l9DhrYXclVLCtKk41CmAPSpvS7Xit5Ug-7Gd6qRxQN55co3dZUxuDp5aalwZ5AcRygAngShWiDVLTWTBQ-r0oYs8qNkNt7CW5P3ws5Kd-fcj8JjM0CYKfAJAQMY"
    data={
            "tag": {
                "id": "100",
                "name": "测试950"
            }
        }
    request=MyRequest()
    r=request.post(url,json=data)
    print(r)
# @pytest.mark.skip
def test_delete_tag():
    url_path = MyConfigYaml().get_conf_url()
    url = url_path +"/tags/delete?access_token=72_jvnA-WUls6l9DhrYXclVLCtKk41CmAPSpvS7Xit5Ug-7Gd6qRxQN55co3dZUxuDp5aalwZ5AcRygAngShWiDVLTWTBQ-r0oYs8qNkNt7CW5P3ws5Kd-fcj8JjM0CYKfAJAQMY"
    data={
            "tag": {
                "id": "108"
            }
        }
    request = MyRequest()
    r = request.post(url, json=data)
    print(r)

if __name__ == '__main__':
    pytest.main(["-vs"],"test_recon.py")