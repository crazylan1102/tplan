# coding=utf-8


class TestSuite(object):
    def __init__(self):
        self.cases = []
        self.globals = {}

    def setup(self):
        print("run testSuite======================")
        pass



    def run(self):
        self.setup()

        for case in self.cases:
            case.setup()
            case.run()
            case.teardown()
        self.teardown()

    def teardown(self):
        print("end testSuite======================")
        pass

    def add_case(self, testcase):
        testcase.set_suite(self)
        self.cases.append(testcase)



class TestCase(object):
    def __init__(self):
        self.name = ""
        self.requestUrl = ""
        self.method = ""
        self.description = ""
        self.responseMessage = ""
        self.result = ""
        self.responseCode = 200
        self.ExceptResCode = 200
        self.requestData = ""
        self.responseBody = ""
        self.ExceptErrorMessage = ""
        self.ResponseMessage = ""

    def set_suite(self, suite):
        self.suite = suite

    def setup(self):
        print("start:"+self.name+"-------------")
        pass

    def run(self):
        pass

    def teardown(self):
        print("end:"+self.name+"-------------"+"\n")
        pass











