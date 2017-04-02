# coding=utf-8

from huoqi.huoqiSuite import *
import requests
import string
import random
import json


def after_execute(name, requestUrl, method, description, responseMessage, resultContent, responseCode, ExceptResCode, requestData, responseBody,ExceptErrorMessage):
    # json_result = result.json()
    with open('result.txt', 'a') as rs:
        # 将期望Code与返回code写入result.txt文件中
        rs.write(name+'#')
        rs.write(method + '#')
        rs.write(requestUrl + '#')
        rs.write(description + '#')
        rs.write(json.dumps(requestData)+ '#')

        rs.write(str(ExceptResCode))
        rs.write('#')
        rs.write(ExceptErrorMessage+'#')

        rs.write(str(responseCode))
        rs.write('#')

        rs.write(responseBody)
        rs.write('#')

        # 并判断测试是否通过，并把结果写入result.txt文件(Code一致，则成功)
        if ExceptResCode == responseCode:
            rs.write("true")
            rs.write('#')
        else:
            rs.write("false")
            rs.write('#')

        rs.write('\n')
        rs.close()

        # 将返回message写入result.txt文件(无返回message则置空)
        # if rs.write(responseMessage + '|') == '':
        #     rs.write('\n')
        #     return
        # else:
        #     rs.write(responseMessage + '|')
        #     rs.write('\n')


# class CreateCurrent(HuoqiCase):
#     def create_new(self, id, maxInvestAmount, minInvestAmount, name, rate, title):
#         requestUrl = "http://core.current.svc/api/currents"
#         r = self.suite.s.post(requestUrl, data=json.dumps({"id": id, "maxInvestAmount": maxInvestAmount,
#                                                        "minInvestAmount": minInvestAmount, "name": name,
#                                                        "rate": rate, "title": title}))
#         print(title)
#         self.suite.globals["current_id1"] = r.json()['id']  # 保存产品ID
#         return self.suite.globals["current_id1"]

# 创建活期产品
class CreatCurrentPro(HuoqiCase):
    def setup(self):
        self.name = "创建活期产品"
        self.description = self.name
        self.requestData = json.dumps({
            "id": "string",
            "maxInvestAmount": 200,
            "minInvestAmount": 200,
            "name": "Tplan1",
            "rate": 6.33,
            "title": "Tplan1"
        })
        self.method = "post"
        self.requestUrl = self.suite.url+"/api/currents"
        self.ExceptResCode = 200

    def run(self):
        r = self.suite.s.post(self.requestUrl, data=self.requestData)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = ""
        self.responseBody = r.text
        self.ExceptErrorMessage = "无"

        self.suite.globals["last_response"] = r
        self.suite.globals["current_id1"] = r.json()['id']  # 保存产品ID

        # after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
        #               self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)


# HuoqiCase001：创建活期账户
class HuoqiCase001(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase001：创建活期账户"
        self.description = self.name
        self.requestData = "--"
        self.method = "post"
        account_uid = '1'.join(random.sample(string.ascii_letters + string.digits, 8))

        self.requestUrl = self.suite.url+"/api/accounts/" + account_uid + "/currents/" + self.suite.globals["current_id1"]
        self.ExceptResCode = 200

    def run(self):
        r = self.suite.s.post(self.requestUrl, data=self.requestData)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = "--"
        self.responseBody = r.text
        self.ExceptErrorMessage = "无"

        self.suite.globals["last_response"] = r
        self.suite.globals["account_uid"] = r.json()['uid']  # 保存账户ID

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)


# HuoqiCase002：创建活期账户——账户已存在
class HuoqiCase002(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase002：创建活期账户——账户已存在"
        self.description = self.name
        self.requestData = "--"
        self.method = "post"
        self.requestUrl = self.suite.url+"/api/accounts/" + self.suite.globals["account_uid"] + "/currents/" + self.suite.globals["current_id1"]
        self.ExceptResCode = 400

    def run(self):
        r = self.suite.s.post(self.requestUrl, data=self.requestData)

        self.responseCode = r.status_code
        self.result = r.text
        self.ExceptErrorMessage = "创建活期账户失败"
        self.responseMessage = r.json()["message"]
        self.responseBody = r.text

        self.suite.globals["last_response"] = r

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody, self.ExceptErrorMessage)


# HuoqiCase003：创建活期账户——currentId不存在
class HuoqiCase003(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase003：创建活期账户——currentId不存在"
        self.description = self.name
        self.requestData = "--"
        self.method = "post"
        currentID_no_exit1 = '2'.join(random.sample(string.ascii_letters + string.digits, 8))
        self.requestUrl = self.suite.url+"/api/accounts/" + self.suite.globals["account_uid"] + "/currents/" + currentID_no_exit1
        self.ExceptResCode = 400

    def run(self):
        r = self.suite.s.post(self.requestUrl, data=self.requestData)

        self.responseCode = r.status_code
        self.result = r.text
        self.ExceptErrorMessage = "创建活期账户失败"
        self.responseMessage = r.json()["message"]
        self.responseBody = r.text

        self.suite.globals["last_response"] = r

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody, self.ExceptErrorMessage)


# 创建活期产品
class CreatCurrentPro1(HuoqiCase):
    def setup(self):
        self.name = "创建活期产品"
        self.description = self.name
        self.requestData = json.dumps({
            "id": "string",
            "maxInvestAmount": 200,
            "minInvestAmount": 200,
            "name": "Tplan2",
            "rate": 6.33,
            "title": "Tplan2"
        })
        self.method = "post"
        self.requestUrl = self.suite.url+"/api/currents"
        self.ExceptResCode = 200

    def run(self):
        r = self.suite.s.post(self.requestUrl, data=self.requestData)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = ""
        self.responseBody = r.text
        self.ExceptErrorMessage = "无"

        self.suite.globals["last_response"] = r
        self.suite.globals["current_id2"] = r.json()['id']  # 保存产品ID

        # after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
        #               self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)


# HuoqiCase004：创建活期账户—同一uid创建不同产品的账户
class HuoqiCase004(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase004：创建活期账户—同一uid创建不同产品的账户"
        self.description = self.name
        self.requestData = "--"
        self.method = "post"

        self.requestUrl = self.suite.url+"/api/accounts/" + self.suite.globals["account_uid"] + "/currents/" + self.suite.globals["current_id2"]
        self.ExceptResCode = 200

    def run(self):
        r = self.suite.s.post(self.requestUrl, data=self.requestData)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = "--"
        self.responseBody = r.text
        self.ExceptErrorMessage = "无"

        self.suite.globals["last_response"] = r
        self.suite.globals["account_uid"] = r.json()['uid']  # 保存账户ID

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)


# HuoqiCase005：查询活期账户—账户不存在（用户名不存在）
class HuoqiCase005(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase005：查询活期账户—账户不存在（用户名不存在）"
        self.description = self.name
        self.requestData = "--"
        self.method = "get"
        currentid_no_exit1 = '3'.join(random.sample(string.ascii_letters + string.digits, 8))
        self.requestUrl = self.suite.url+"/api/accounts/" + currentid_no_exit1 + "/currents/" + self.suite.globals["current_id1"]
        self.ExceptResCode = 404

    def run(self):
        r = self.suite.s.get(self.requestUrl)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = "--"
        self.responseBody = r.text
        self.ExceptErrorMessage = "账户不存在"

        self.suite.globals["last_response"] = r

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)


# HuoqiCase006：查询活期账户—账户不存在（currentId不存在）
class HuoqiCase006(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase006：查询活期账户—账户不存在（currentId不存在）"
        self.description = self.name
        self.requestData = "--"
        self.method = "get"
        currentId_no_exit2 = '4'.join(random.sample(string.ascii_letters + string.digits, 8))
        self.requestUrl = self.suite.url+"/api/accounts/" + self.suite.globals["account_uid"] + "/currents/" + currentId_no_exit2
        self.ExceptResCode = 404

    def run(self):
        r = self.suite.s.get(self.requestUrl)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = "--"
        self.responseBody = r.text
        self.ExceptErrorMessage = "账户不存在"

        self.suite.globals["last_response"] = r

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)


# HuoqiCase007：查询活期账户—用户名为空
class HuoqiCase007(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase007：查询活期账户—用户名为空"
        self.description = self.name
        self.requestData = "--"
        self.method = "get"
        self.requestUrl = self.suite.url+"/api/accounts/" + "" + "/currents/" + self.suite.globals["current_id1"]
        self.ExceptResCode = 404

    def run(self):
        r = self.suite.s.get(self.requestUrl)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = "--"
        self.responseBody = r.text
        self.ExceptErrorMessage = "账户不存在"

        self.suite.globals["last_response"] = r

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)


# HuoqiCase008：查询活期账户—账户不存在（currentId为空）
class HuoqiCase008(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase008：查询活期账户—账户不存在（currentId为空）"
        self.description = self.name
        self.requestData = "--"
        self.method = "get"
        self.requestUrl = self.suite.url+"/api/accounts/" + self.suite.globals["account_uid"] + "/currents/" + ""
        self.ExceptResCode = 404

    def run(self):
        r = self.suite.s.get(self.requestUrl)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = "--"
        self.responseBody = r.text
        self.ExceptErrorMessage = "账户不存在"

        self.suite.globals["last_response"] = r

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)


# HuoqiCase009：查询活期账户
class HuoqiCase009(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase009：查询活期账户"
        self.description = self.name
        self.requestData = "--"
        self.method = "get"
        self.requestUrl = self.suite.url+"/api/accounts/" + self.suite.globals["account_uid"] + "/currents/" + self.suite.globals["current_id1"]
        self.ExceptResCode = 200

    def run(self):
        r = self.suite.s.get(self.requestUrl)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = "--"
        self.responseBody = r.text
        self.ExceptErrorMessage = "--"

        self.suite.globals["last_response"] = r

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)

# 创建活期账户
class CreateAccount(HuoqiCase):
    def setup(self):
        self.name = "创建活期账户"
        self.description = self.name
        self.requestData = "--"
        self.method = "post"
        account_uid = '1'.join(random.sample(string.ascii_letters + string.digits, 8))

        self.requestUrl = self.suite.url+"/api/accounts/" + account_uid + "/currents/" + self.suite.globals["current_id1"]
        self.ExceptResCode = 200

    def run(self):
        r = self.suite.s.post(self.requestUrl, data=self.requestData)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = "--"
        self.responseBody = r.text
        self.ExceptErrorMessage = "无"

        self.suite.globals["last_response"] = r
        self.suite.globals["account_uid2"] = r.json()['uid']  # 保存账户ID

        # after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
        #               self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)


# HuoqiCase010：查询活期账户—用户名和currentid不对应
class HuoqiCase010(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase010：查询活期账户—用户名和currentid不对应"
        self.description = self.name
        self.requestData = "--"
        self.method = "get"
        self.requestUrl = self.suite.url+"/api/accounts/" + self.suite.globals["account_uid2"] + "/currents/" + self.suite.globals["current_id2"]
        self.ExceptResCode = 404

    def run(self):
        r = self.suite.s.get(self.requestUrl)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = "--"
        self.responseBody = r.text
        self.ExceptErrorMessage = "账户不存在"

        self.suite.globals["last_response"] = r

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)


# HuoqiCase011：禁用活期账户1
class HuoqiCase011(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase011：禁用活期账户1"
        self.description = self.name
        self.requestData = "--"
        self.method = "put"
        self.requestUrl = self.suite.url+"/api/accounts/" + self.suite.globals["account_uid"] + "/currents/" + self.suite.globals["current_id1"] + "/disable"
        self.ExceptResCode = 200

    def run(self):
        r = self.suite.s.put(self.requestUrl, data=self.requestData)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = "--"
        self.responseBody = r.text
        self.ExceptErrorMessage = "无"

        self.suite.globals["last_response"] = r

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)


# HuoqiCase012：开启活期账户1
class HuoqiCase012(HuoqiCase):
    def setup(self):
        self.name = "HuoqiCase012：开启活期账户1"
        self.description = self.name
        self.requestData = "--"
        self.method = "put"
        self.requestUrl = self.suite.url+"/api/accounts/" + self.suite.globals["account_uid"] + "/currents/" + self.suite.globals["current_id1"] + "/enable"
        self.ExceptResCode = 200

    def run(self):
        r = self.suite.s.put(self.requestUrl, data=self.requestData)

        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = "--"
        self.responseBody = r.text
        self.ExceptErrorMessage = "无"

        self.suite.globals["last_response"] = r

        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData, self.responseBody,self.ExceptErrorMessage)

