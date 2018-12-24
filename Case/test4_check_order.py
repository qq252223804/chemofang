# -*- coding: utf-8 -*- 
# @Time : 2018/12/19 18:29 
# @Author : taojian 
# @File : test4_check_order.py
import unittest

import requests
import yaml,json

from Base.runmethod import RunMethod
from Common.variables_func import user_Session, get_yaml_variable
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

		# token=get_yaml_variable("X-SessionToken-With")
		# print("登陆后的token为：%s"%token)
		user_Session()
		cls.app_host = cls.app_host
		cls.User_session = {"X-SessionToken-With": get_yaml_variable("X-SessionToken-With")}
		
		cls.app_headers.update(cls.User_session)
		print(cls.app_headers)
	def test_check_order(self):
		"""
		检查订单状态
		:return:
		"""
		Log().debug("正在执行:检查订单状态")
		lujing="/loan/order/check/"
		headers=self.app_headers
		res=RunMethod().run_main("get",self.app_host,lujing,headers=headers)
		self.assertEqual(res["code"],200)
		print(res)

		
		

if __name__ == "__main__":

	unittest.main()