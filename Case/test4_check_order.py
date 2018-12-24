# -*- coding: utf-8 -*- 
# @Time : 2018/12/19 18:29 
# @Author : taojian 
# @File : test4_check_order.py
import unittest

import requests
import yaml,json

from Base.runmethod import RunMethod
from Common.variables_func import dealer_Session, get_yaml_variable
from utx import Log


class order(unittest.TestCase):
	with open('E:\\chemofang\\Config\\conf.yaml', "r", encoding="utf-8") as r:
		config = yaml.load(r)  # 解析并读写yaml文件
		app_host = config['app_host']
		cms_host = config['cms_host']
		app_headers = eval(config['app_headers'])
	
	@classmethod  # 调用类变量时需加@classmethod
	def setUpClass(cls):
		Log().info("正在执行:登陆测试")
		dealer_Session()  # 登陆写入session
		# token=get_yaml_variable("X-SessionToken-With")
		# print("登陆后的token为：%s"%token)
		
		cls.app_host = cls.app_host
		cls.cms_host = cls.cms_host
		
		cls.Dealer_session = {"X-SessionToken-With": get_yaml_variable("X-SessionToken-With")}
		cls.app_headers.update(cls.Dealer_session)
		
	def test_check_order(cls):
		"""
		检查订单状态
		:return:
		"""
		Log().debug("正在执行:检查订单状态")
		lujing="/loan/order/check"
		# print(cls.app_host+lujing)
		# print(cls.app_headers)
		res=RunMethod.run_main('get',cls.app_host,lujing,cls.app_headers)
		print(res)
		
		

if __name__ == "__main__":

	unittest.main()