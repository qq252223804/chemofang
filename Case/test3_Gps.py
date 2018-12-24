# -*- coding: utf-8 -*- 
# @Time : 2018/12/19 10:23 
# @Author : taojian 
# @File : test3_Gps.py

import unittest,yaml,json,requests
from Common.variables_func import write_yaml_variable,get_yaml_variable,cms_cookies,qiniu_uploadToken2
from utx import Log

class gps(unittest.TestCase):
	with open('E:\\chemofang\\Config\\conf.yaml', "r", encoding="utf-8") as r:
		config = yaml.load(r)  # 解析并读写yaml文件
		cms_host = config['cms_host']
	
	@classmethod  # 调用类变量时需加@classmethod
	def setUpClass(cls):
		Log().info("正在执行:GPS管理模块测试")
		cls.cms_host=cls.cms_host
		cls.session = cms_cookies()  # 将获取的cookie设置为session变量全局使用

	
	def test_getJimiGPS(cls):
		"""
		查询记录仪信息
		:return:
		"""
		jim='868120185127088'
		lujing = "/cms/GPS/getJimiGPS/"+jim
		res = cls.session.get(cls.cms_host + lujing)
		response = json.loads(res.text)
		cls.assertIn("'imei': '868120185127088'", str(response['data']), msg='gps查询失败')
		print(response)
	def test_add_gps(cls):
		"""
		添加GPS
		:return:
		"""
		lujing="/cms/GPS/addCarGPS"
		data={"imei":"868120185127088",
"type":"WIRELESS",
"deviceModel":" GT740",
"dateExpired":"2038-05-21 16:29:51",
"dateActivated":"2018-05-21 16:29:51",
"activationFlag":"true",
"status":"0",
"expiryFlag":"true",
"startingState":"NORMAL",
"simNo":"1064730151182"}
		res=cls.session.post(cls.cms_host+lujing,data=data)
		response = json.loads(res.text)
		cls.assertEqual("success", response['msg'], msg='gps添加失败')
		print(response)
#
	def test_getCarInfo_VIM(cls):
		"""
		根据车架号查询已提车信息
		:return:
		"""
		vin = '1545200742441'
		lujing ="/cms/GPS/getCarInfoByCode/"+vin
		res=cls.session.get(cls.cms_host+lujing)
		response = json.loads(res.text)
		cls.assertIn('1545200742441', str(response['data']), msg='gps查询失败')
		print(response)
	# def test_uplod_Gpsimages(cls):
	# 	"""
	# 	上传七牛
	# 	:return:
	# 	"""
	# 	uploadToken=qiniu_uploadToken2()
	# 	url="http://upload.qiniup.com/"
	# 	files1 = {'file': ('45U58PIC9dF.jpg', open('E:\\chemofang\\Config\\45U58PIC9dF.jpg', 'rb'), 'multipart/form-data')}
	# 	files2 = {'file': ('45U58PIC9dF.jpg', open('E:\\chemofang\\Config\\45U58PIC9dF.jpg', 'rb'), 'multipart/form-data; boundary=----WebKitFormBoundaryMEy9M0PXwBREHkYK')}
	# 	# 参数名为fiel 文件路径 +文件类型
	# 	datas = {"token": uploadToken,"name":"o_1cv38i9rbto7b2gis41drp1nfp1n.jpg","key":"o_1cv38i9rbto7b2gis41drp1nfp1n.jpg"}
	# 	res1 =cls.session.post(url, files=files1, data=datas)  # 上传文件 用files 参数 data/headers
	# 	res2=cls.session.post(url, files=files2, data=datas)    #上传2张
	# 	print(res1.json())
	# 	print(res2.json())
		# write_yaml_variable("key1", res1.json()["key"])


		
	def test_bindCarGPS(cls):
		"""
		绑定车辆
		:return:
		"""
		lujing = "/cms/GPS/bindCarGPS"
		# key=get_yaml_variable("key1")
		# picture="http://test-oss.mofangcar.com/"+"o_1cv38i9rbto7b2gis41drp1nfp1n.jpg"
		# pictures=[picture,picture]
		# json.dumps(picture1)

		datas={"imei":"868120185127088",
			"pictures":"[\"http://test-oss.mofangcar.com/o_1cv38i9rbto7b2gis41drp1nfp1n.jpg\", \"http://test-oss.mofangcar.com/o_1cv38i9rbto7b2gis41drp1nfp1n.jpg\"]",
			"carVinNo":"1545200742441"}

		res1=cls.session.post(cls.cms_host+lujing,data=datas)
		response = json.loads(res1.text)
		cls.assertEqual("success", response['msg'], msg='gps绑定失败')

		print(response)
		
	def test_unbindCarGPS(cls):
		"""
		解除绑定车辆
		:return:
		"""
		jim = '868120185127088'
		lujing="/cms/GPS/unbindCarGPS/"+jim
		res = cls.session.post(cls.cms_host + lujing)
		response = json.loads(res.text)
		print(response)
		
	def test_delete_gps(cls):
		"""
		删除gps
		:return:
		"""
		jim = '868120185127088'
		lujing='/cms/GPS/deleteCarGPS/'+jim
		res=cls.session.post(cls.cms_host + lujing)
		response = json.loads(res.text)
		print(response)

	



		
		
		
if '__name__'=='__main__':
	unittest.main()
	
	


