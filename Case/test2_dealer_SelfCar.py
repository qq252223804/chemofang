'''
此py文件采取yaml写入写出变量
实现流程性api测试
实现流程回归
'''
import unittest,requests,json
from utx import *
from Base.runmethod import RunMethod
from Common.variables_func import dealer_Session,cms_cookies,get_yaml_variable,write_yaml_variable,qiniu_uploadToken1
import yaml



class Dingjia(unittest.TestCase):

	with open('E:\\chemofang\\Config\\conf.yaml', "r", encoding="utf-8") as r:
		config = yaml.load(r)  # 解析并读写yaml文件
		app_host = config['app_host']
		cms_host = config['cms_host']
		app_headers = eval(config['app_headers'])
		


	@classmethod  #调用类变量时需加@classmethod
	def setUpClass(cls):
		Log().info("正在执行:登陆测试")
		dealer_Session()         #登陆写入session
		# token=get_yaml_variable("X-SessionToken-With")
		# print("登陆后的token为：%s"%token)
		
		cls.app_host=cls.app_host
		cls.cms_host=cls.cms_host
		
		cls.Dealer_session={"X-SessionToken-With":get_yaml_variable("X-SessionToken-With")}
		cls.app_headers.update(cls.Dealer_session)

		cls.session=cms_cookies()       #将获取的cookie设置为session变量全局使用
	
		# Log().info("正在执行:定价申请——通过流程")
		# print(cls.host,cls.headers)

	def test_dingjia_shenqing(self):
		'''
		车商定价申请
		:return:sq_id
		'''
		Log().debug("正在执行:定价申请——通过流程")
		# print("头部信息为：%s" % cls.headers)
		datas={"carConfigInstructionImage":[],
		       "carQualifiedImage":"",
		       "invoicePrice":"100008",
		       "price":"388.80","carNameplateImage":"","dealerCarId":"5c1b70d6cec76d6f353db12d"}
		lujing='/carmall/applyDealerCarEnquiry/apply'
		res=RunMethod().run_main('post',self.app_host,lujing,datas,	self.app_headers)
		write_yaml_variable("data", res['data'])
		print( res['data'])
		
		self.assertTrue(str(res['code']) == '200', msg='状态不对')
		self.assertIn('success', res['msg'], msg='a不在b中')
		# print(res)
		# # print(type(res['code']))

	def test_shenqing_details(self):
		'''
		采销后台打开申请详情
		:return:
		'''

		sq_id=get_yaml_variable("data")
		
		lujing='/cms/dealerCarEnquiry/getDetail/'+sq_id
		# print(lujing)
		res=self.session.get(self.cms_host+lujing)
		response=json.loads(res.text)                 #res.text 为str格式 json。loads（）将str-dict
		
		self.assertTrue(str(response['code']) == '200', msg='状态不对')
		self.assertIn('success', response['msg'], msg='a不在b中')
		self.assertIn("'statusName': '待平台定价审核'", str(response['data']), msg='a不在b中')
		print(response['data']['applyNo'])
	
	def test_Dingjia_auditPass(self):
		"""
		定价申请审核通过
		:return:
		"""
		lujing='/cms/dealerCarEnquiry/operateDealerCarEnquiry'
		sq_id=get_yaml_variable("data")

		data={"id":sq_id,"status":"PASSED","remark":"自动化通过"}
		res=self.session.post(self.cms_host+lujing,data)
		response = json.loads(res.text)
		self.assertTrue(str(response['code']) == '200', msg='状态不对')
		self.assertIn('success', response['msg'], msg='a不在b中')
		print(response)

	def test_baodan(self):
		"""
		车商报单申请
		:return:
		"""

		Log().info('车辆报单-通过流程')
	@unittest.skip("跳过失败流程")
	def test_baodan2(self):
		"""
		车商报单申请
		:return:
		"""
		
		Log().warning('车辆报单-失败流程')
	def test_upload_pictures(self):
		"""
		上传图片
		获取时间戳-上传凭证——上传七牛——返回key
		:return:
		"""
		
		Log().info('上传图片-更改头像流程')
		uploadToken=qiniu_uploadToken1()
		# print(upload_voucher)
		#开始上传七牛
		url3='http://upload.qiniup.com/'
		files={'file':('45U58PIC9dF.jpg',open('E:\\chemofang\\Config\\45U58PIC9dF.jpg','rb'),'application/octet-stream')}
		#参数名为fiel 文件路径 +文件类型
		datas={"token":uploadToken}
		res3=requests.post(url3,files=files,data=datas)    #上传文件 用files 参数 data/headers
		write_yaml_variable("key", res3.json()["key"])
		print( res3.json())
		

	def test_change_headshot(self):
		"""
		更改头像
		获取时间戳-上传凭证——上传七牛——返回key——上传服务器
		:return:
		"""
		key=get_yaml_variable("key")
		# print(key)
		url=self.app_host+'/dealer/upInfo'
		image="http:\/test-oss.mofangcar.com\/"+key
		print(image)
		datas={"headImage":image}

		# print(datas)         #此处加了一个变量 自动变为单引号了 但请求必须为双引号的json数据类型啊！！！！
		# data = json.dumps(datas)  #所以必须使用json.dumps 变为 json数据类型 或者下面json=datas也行
		# print(data)
		# print(type(data))
	
		headers=self.app_headers
		res=requests.put(url,json=datas,headers=headers)
		print(res.json())
	



if __name__ == "__main__":

	unittest.main()
	
