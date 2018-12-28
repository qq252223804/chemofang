#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import time

from utx import *
from Common.Email import send_email

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report\\")

times=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
# print(times)
# 发送文件路径
file_path =report_path+times+r"-ztest.html"
# print(file_path)
if __name__ == '__main__':
    setting.check_case_doc = False  # 关闭检测是否编写了测试用例描述
    setting.full_case_name = True
    setting.max_case_name_len = 80  # 测试报告内，显示用例名字的最大程度
    setting.show_error_traceback = True  # 执行用例的时候，显示报错信息
    setting.sort_case = True  # 是否按照编写顺序，对用例进行排序
    setting.create_bstest_style_report = False # 生成bstest风格的报告
    setting.create_ztest_style_report = True  # 生成ztest风格的报告



    runner = TestRunner()
    runner.add_case_dir(r"Case")
    runner.run_test(report_title='车魔方接口自动化测试报告')

    send_email(file_path)

