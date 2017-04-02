from django.shortcuts import render
import codecs,os,time
from django.http import HttpResponse
from django.shortcuts import render_to_response
from huoqi.huoqiCases import *
# Create your views here.


def generate_report(request):
    result_list = []
    result_file = codecs.open('result.txt', 'r')
    lines = result_file.readlines()
    success = 0
    fail = 0
    for line in lines:
        li = line.split("#")
        row = {"name": li[0], "method": li[1], "requestUrl": li[2], "description": li[3], "requestData": li[4],
                 "ExceptResCode": li[5],"ExceptErrorMessage": li[6], "responseCode":li[7],"responseBody": li[8],
               "result": li[9]}
        print(row["result"])
        if row["result"] == "true":
            success += 1
        else:
            fail += 1
        result_list.append(row)
    result_file.close()
    generateTime = time.strftime("%Y-%m-%d %H:%M:%S")
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(os.getcwd())
    os.remove(os.getcwd()+"\\result.txt")
    return render_to_response("huoqi_report.html", {'testcases': result_list, 'total': len(lines), "success": success,
                                               'fail': fail, 'generateTime': generateTime})

def RunHuoqiTesting(request):
    huoqiSuite = HuoqiSuite()
    huoqiSuite.add_case(CreatCurrentPro())
    huoqiSuite.add_case(HuoqiCase001())
    huoqiSuite.add_case(HuoqiCase002())
    huoqiSuite.add_case(HuoqiCase003())
    huoqiSuite.add_case(CreatCurrentPro1())
    huoqiSuite.add_case(HuoqiCase004())
    huoqiSuite.add_case(HuoqiCase005())
    huoqiSuite.add_case(HuoqiCase006())
    huoqiSuite.add_case(HuoqiCase007())
    huoqiSuite.add_case(HuoqiCase008())
    huoqiSuite.add_case(HuoqiCase009())
    huoqiSuite.add_case(CreateAccount())
    huoqiSuite.add_case(HuoqiCase010())
    huoqiSuite.add_case(HuoqiCase011())
    huoqiSuite.add_case(HuoqiCase012())
    huoqiSuite.run()
    return generate_report(request)