#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import os

from utx import *



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
    runner.run_test(report_title='接口自动化测试报告')
