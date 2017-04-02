# coding=utf-8


from debt.testSuite import *
import requests


class debtSuite(TestSuite):
    def setup(self):


        super(debtSuite, self).setup()
        self.s = requests.session()
        self.headers = {'content-type': "text/plain",'cache-control': "no-cache",
                        'postman-token': "25778bc8-4eba-135a-8fb0-c26507065e8d"}
        self.s.headers.update(self.headers)
        self.url = "http://core.debt.svc"


class debtCase(TestCase):
    def setup(self):
        super(debtCase, self).setup()
        pass

    def teardown(self):
        super(debtCase, self).teardown()
        pass

