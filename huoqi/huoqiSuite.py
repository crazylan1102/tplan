# coding=utf-8


from huoqi.testSuite import *
import requests


class HuoqiSuite(TestSuite):
    def setup(self):


        super(HuoqiSuite, self).setup()
        self.s = requests.session()
        self.headers = {'content-type': "application/json", 'cache-control': "no-cache",
                        'postman-token': "6a7d1156-d5ab-73b2-9c19-ce63d4763b2f"}
        self.s.headers.update(self.headers)
        self.url = "http://core.current.svc"


class HuoqiCase(TestCase):
    def setup(self):
        super(HuoqiCase, self).setup()
        pass

    def teardown(self):
        super(HuoqiCase, self).teardown()
        pass

