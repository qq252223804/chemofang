# -*- coding: utf-8 -*- 
# @Time : 2018/12/20 18:31 
# @Author : taojian 
# @File : test5_SelfCar_manage.py
import unittest

import yaml
import json

from Common.SQL_execute import MysqlUtil
from Common.variables_func import dealer_Session, cms_cookies
from utx import Log


class Selfcar(unittest.TestCase):
	with open('E:\\chemofang\\Config\\conf.yaml', "r", encoding="utf-8") as r:
		config = yaml.load(r)  # 解析并读写yaml文件
		cms_host = config['cms_host']

	
	@classmethod  # 调用类变量时需加@classmethod
	def setUpClass(cls):
		Log().info("正在执行:登陆测试")
		dealer_Session()  # 登陆写入session
		# token=get_yaml_variable("X-SessionToken-With")
		# print("登陆后的token为：%s"%token)
		cls.cms_host = cls.cms_host
		cls.session = cms_cookies()  # 将获取的cookie设置为session变量全局使用

	def test_UP_Selfcar(self):
		"""
		上架车辆
		:return:
		"""
		lujing = "/cms/dealer/car/add"
		data = {"carBrandId": "5a5ebfb1943d0b515a43b32f",
		        "carSeriesId": "5a5ec006943d0b515a43b333",
		        "carInfoId": "5a5ec113943d0b515a43b33a"}
		res = self.session.post(self.cms_host + lujing, params=data)
		response = json.loads(res.text)
		self.assertTrue(str(response['code']) == '200', msg='状态不对')
		self.assertEqual("success",response['msg'],msg='接口返回错误')
		print(response)

	def test_Down_Selfcar(self):
		"""
		下架车辆
		:return:
		"""
		mysql = MysqlUtil()
		sql = "select * from dealer_car where car_info_id= '5a5ec113943d0b515a43b33a' ORDER BY id DESC"
		
		mysql.mysql_execute(sql, number='one')
		id=mysql.mysql_getrows(sql,number='one')[0]
		# print(id)
		lujing = "/cms/dealer/car/unshelve/"+id
		res = self.session.post(self.cms_host + lujing)
		response = json.loads(res.text)
		self.assertTrue(str(response['code']) == '200', msg='状态不对')
		self.assertEqual("success", response['msg'], msg='接口返回错误')
		print(response)


if __name__ == "__main__":

	unittest.main()