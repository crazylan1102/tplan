from django.shortcuts import render
import codecs,os,time
from django.http import HttpResponse
from django.shortcuts import render_to_response
from huoqi.huoqiCases import *
# Create your views here.


def generate_report(request):
    result_list = []
    print(os.getcwd())
    result_file = codecs.open('result.txt', 'r', encoding='utf-8')
    lines = result_file.readlines()
    success = 0
    fail = 0

    for line in lines:
        li = line.split("|")
        row = {"name": li[0], "method": li[1], "requestUrl": li[2], "description": li[3], "responseMessage": li[4],
               "resultContent": li[5], "requestData": li[6], "responseCode": li[7], "ExceptResCode": li[8],
               "result": li[9]}
        print("haahhahahahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        print(row["result"])
        print("haahhahahahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        if row["result"] == "true":
            print("wwwwwwwwwwwwwwwwwwwwwwwwwww")
            success += 1
        else:
            print("ccccccccccccccccccc")
            fail += 1
        result_list.append(row)
    result_file.close()
    generateTime = time.strftime("%Y-%m-%d %H:%M:%S")
    print(result_list)
    return render_to_response("huoqi_report.html", {'testcases': result_list, 'total': len(lines), "success": success,
                                               'fail': fail, 'generateTime': generateTime})

def RunHuoqiTesting(request):
    huoqiSuite = HuoqiSuite()
    huoqiSuite.add_case(HuoqiCase001())
    # huoqiSuite.add_case(HuoqiCase002())
    huoqiSuite.run()
    return generate_report(request)