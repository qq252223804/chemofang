# -*- coding: utf-8 -*- 
# @Time : 2018/12/24 14:29 
# @Author : taojian 
# @File : run_excel.py

import unittest
import time
from Common import HTMLTestRunner_api
import os

from Common.Email import send_email

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report_excel")
if not os.path.exists(report_path): os.mkdir(report_path)
#执行用例路径
case_path = os.path.join(curpath, "Case_excel")


def add_case(casepath=case_path, rule="test*_*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                  pattern=rule,)

    return discover

def run_case(all_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    htmlreport = reportpath+r"\result.html"
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner_api.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="测试报告",
                                               description="用例执行情况")
    #发送报告的路径
    file_path=htmlreport
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()
    send_email(file_path)
    

if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
    print('ok')

