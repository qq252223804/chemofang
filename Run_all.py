#coding:utf-8
import os

from Common.Email import send_email

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "Report_html")
if not os.path.exists(report_path): os.mkdir(report_path)


import unittest
from BeautifulReport import BeautifulReport



# 发送文件路径
file_path =report_path+r"\测试报告.html"
print(file_path)
if __name__=='__main__':
	suit=unittest.defaultTestLoader.discover('Case',pattern='test*_*.py')
	report=BeautifulReport(suit)
	report.report(filename='测试报告',description='测试车魔方流程接口报告',log_path='Report_html')
	send_email(file_path)


