# coding=utf-8

from debt.debtSuite import *
import requests
import string
import random


def after_execute(name, requestUrl, method, description, responseMessage, resultContent, responseCode, ExceptResCode, requestData):
    # json_result = result.json()
    with open('result.txt', 'a') as rs:
        # 将期望Code与返回code写入result.txt文件中
        rs.write(name+'|')
        rs.write(method + '|')
        rs.write(requestUrl + '|')
        rs.write(description + '|')
        rs.write("sdfsd" + '|')
        rs.write(resultContent + '|')
        rs.write(requestData+'|')
        rs.write(str(responseCode))
        rs.write('|')
        rs.write(str(ExceptResCode))
        rs.write('|')

        print(responseCode)
        print(ExceptResCode)

        # 并判断测试是否通过，并把结果写入result.txt文件(Code一致，则成功)
        if ExceptResCode == responseCode:
            rs.write("true")
            rs.write('|')
        else:
            rs.write("false")
            rs.write('|')
        rs.write('\n')
        rs.close()



        # 将返回message写入result.txt文件(无返回message则置空)
        # if rs.write(responseMessage + '|') == '':
        #     rs.write('\n')
        #     return
        # else:
        #     rs.write(responseMessage + '|')
        #     rs.write('\n')


class DebtCase001(debtCase):
    def setup(self):
        # self.name = "创建借款人账户"
        self.name = "createaccount"
        super(DebtCase001, self).setup()

    def run(self):
        self.requestUrl = self.suite.url+"/api/borrower_accounts/"
        self.method = "post"
        self.description = self.name
        self.ExceptResCode = 201
        self.requestData = 'l'.join(random.sample(string.ascii_letters + string.digits, 8))

        super(DebtCase001, self).run()
        r = self.suite.s.post(self.requestUrl, data=self.requestData)
        self.responseCode = r.status_code
        self.result = r.text
        self.responseMessage = ""

        self.suite.globals["last_response"] = r
        self.suite.globals["debt_b_uid1"] = self.requestData

        print(self.name)
        print(self.requestUrl)
        print(self.method)
        print(self.description)
        print(self.responseMessage)
        print(self.result)
        print(self.responseCode)
        print(self.ExceptResCode)
        print(self.requestData)
        after_execute(self.name, self.requestUrl, self.method, self.description, self.responseMessage,
                      self.result, self.responseCode, self.ExceptResCode, self.requestData)


class DebtCase002(debtCase):
    def run(self):
        super(DebtCase002, self).run()

        r = self.suite.s.post(self.suite.url+"/api/borrower_accounts/", self.suite.globals["debt_b_uid1"])
        self.suite.globals["last_response"] = r
        print(r.text)







