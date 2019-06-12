''''
目前实现登陆单接口
# 后期此py 可完善登陆模块/类似模块接口测试
采取ddt+自动读取
@data 传入数据 将接口结果写入到excel
'''
import unittest,requests,json
from utx import *
# from ddt import ddt,data,unpack
from Base.runmethod import RunMethod



# @unittest.skip("跳过测试登陆")

class login(unittest.TestCase):
	
	def setUp(self):
		self.run=RunMethod()
	
		# pass
	def tearDown(self):
		pass
	@data({"mobile": "18657738815", "password": "dc483e80a7a0bd9ef71d8cf973673924"},
	      {"mobile": "13071863055", "password": "dc483e80a7a0bd9ef71d8cf973673924"},unpack=False)
	def test_dealer_login(self,data):
		'''
		车商登陆:密码
		:return:session

		'''

		host = 'http://192.168.31.172:8080'
		lujing='/dealer/login'
		# datas = {"mobile": "18657738815", "password": "dc483e80a7a0bd9ef71d8cf973673924"}
		headers = {"version": "2.0.0", "Connection": "keep-alive", "Content-Type": "application/json; charset=utf-8"}

		res =self.run.run_main('post',host,lujing,data=data,headers=headers)
		self.assertTrue(str(res['code']) == '200', msg='状态不对')
		self.assertIn('success', res['msg'], msg='a不在b中')
		print(res)
	@data(18657738815, 15805811478, 13071863055)
	def test_cms_login(self,user):
		"""后台登陆:密码

		:return:cookie
		"""

		url='http://192.168.31.172:8082/cms/login'
		datas={"username":user,"password":111111}
		res=requests.post(url,datas)
		response =res.json()
		self.assertTrue(str(response['code']) == '200', msg='状态不对')
		self.assertIn('success', response['msg'], msg='a不在b中')
		print(response)

	@data(["gold", 100], ["diamond", 500])
	def test_bless(self, bless_type, award):
		'''
		领取宝箱
		:param bless_type:
		:param award:
		:return:
		'''
		print(bless_type)
		print(award)
	#
	# @data(*testdata)
	# def test_file(self,file):
	#
	# 	print(file)



if __name__ == "__main__":
	unittest.main()