
# -*- coding:utf8 -*-
# create by pengcheng
import json,requests
from conf import ApiSetting


class BaseApi(object):
    url = ""
    base_url= ApiSetting.API_TEST_BASE_URL

    def __init__(self,url_params=None):
        if not url_params:
            url_params = []
        self.url_params = url_params
        self.response = None
        self.base_url = self.base_url

    # 拼接url
    def api_url(self):
        if not self.url:
            raise RuntimeError("no url been set")
        return self._get_url()

    def _get_url(self):
        format_url = self.url.format(self.url_params)
        return "{0}{1}".format(self.base_url, format_url)

    # 封装POST请求类型
    def post(self, data=None):
        if not data:
            data = {}
        base_param = self.build_base_param()
        custom_param = self.build_custom_param(data)
        data.update(base_param)
        data.update(custom_param)
        self.response = requests.post(url=self.api_url(), data=data, headers=ApiSetting.HEADERS)
        return self.response

    # 封装GET请求类型
    def get(self,data=None):
        if not data:
            data={}
        base_param = self.build_base_param()
        custom_param = self.build_custom_param(data)
        data.update(base_param)
        data.update(custom_param)
        response = requests.get(url=self.api_url(),params=data)
        return self.response

    # 获取回参中状态码
    def get_code(self):
        if self.response:
            return json.loads(self.response.text)['code']

    # 获取HTTP状态码
    def get_status_code(self):
        if self.response:
            return self.response.status_code

    # 获取回参中message
    def get_response_message(self):
        if self.response:
            return json.loads(self.response.text)['message']

    # 所有接口共有的入参，比如：app_version、token等
    def build_base_param(self):
        return {
                "app_version": ApiSetting.APP_VERSION,
                "token":""
        }

    # 被测接口除公共参数外所需的其余参数
    def build_custom_param(self, data):
        return {}