# -*- coding: utf-8 -*- 
# @Time : 2018/12/13 10:21 
# @Author : taojian 
# @File : test3_excel_apis.py
#  此py文件用于处理excel管理接口数据 unittest+ddt+excel
# 对于没有关联的单个接口请求是可以批量执行的，需要登录的话写到setUpclass里的session里保持cookies
# token关联的不能实现

import ddt,unittest

from Base.api_method import send_requests, write_result
from Common import *
from Common.Operate_Excel import UtilExcel
from Common.variables_func import cms_cookies


#设置全局变量 方便ddt.data 读取
excelPath = "E:\chemofang\Config\cms_api.xlsx"
sheet_id = 0
read_data = UtilExcel(excelPath,sheet_id).dict_data()         #一次性读取所有数据
# print(read_data[0])
@ddt.ddt
class A(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.session=cms_cookies() #  一次性登陆

	# @ddt.data(*read_data)  #ddt 用法
	# def test_url(self,data):
	# 	print(data['url'])
	#
	@ddt.data(*read_data)
	def test_api(self,data):

		Response = send_requests(self.session, data)  # 返回数据 (以ddt格式 批量读取)
		# print(A)
		write_result(Response, write_excelPath=excelPath,sheet_id=sheet_id)   #写入数据
		# 检查点 checkpoint
		check = data["CheckPoint"]
		print("检查点->：%s" % check)
		print("返回实际结果->：%s" % Response)
		# 断言
		self.assertIn(check, str(Response), msg='a不在b中')
if __name__ == "__main__":
	unittest.main()


