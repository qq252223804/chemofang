#coding:utf-8
import os

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "Report_html")
if not os.path.exists(report_path): os.mkdir(report_path)


import unittest
from BeautifulReport import BeautifulReport




if __name__=='__main__':
	suit=unittest.defaultTestLoader.discover('Case',pattern='test*_*.py')
	report=BeautifulReport(suit)
	report.report(filename='测试报告',description='测试车魔方流程接口报告',log_path='Report_html')


