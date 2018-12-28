# -*- coding: utf-8 -*- 
# @Time : 2018/12/28 14:04 
# @Author : taojian 
# @File : test6_mock_api.py
import json
import unittest

from Common.mock_demo import mock_test

class Mock(unittest.TestCase):
	def test_04(self):
		"""
		模拟接口测试
		"""
		url = 'http://coding.imooc.com/api/cate'
		data = {
			'timestamp': '1507034803124',
			'uid': '5249191',
			'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
			'secrect': '078474b41dd37ddd5efeb04aa591ec12',
			'token': '7d6f14f21ec96d755de41e6c076758dd',
			'cid': '0',
			'errorCode': 1003
		}
		'''1'''
		# mock_data=mock.Mock(return_value=data)  #面向对象-对象
		# self.run.method_main=mock_data    #  模拟返回数据 返回上面的data 数据 新增了errCOde
		'''2'''
		# self.run.method_main=mock.Mock(return_value=data)  # 实例化 run.method_main这样mock数据就等于response
		# respose = self.run.method_main(url, 'POST', data)
		'''3'''
		response = mock_test(url, 'POST', data, data)  # mock 的封装使用
		print(json.dumps(response, indent=2, sort_keys=True))
		self.assertEqual(response["errorCode"], 1003, '测试失败')
	
if __name__ == "__main__":

	unittest.main()
