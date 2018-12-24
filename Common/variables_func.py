#coding:utf-8
"""读取变量封装的方法"""
import yaml
import json
import requests, hashlib
from Base.runmethod import RunMethod

def write_yaml_variable(key=None,value=None):
	"""
	把返回的变量值写入到yaml文件-yaml中已存在key
	:return:
	"""
	# a 追加写入，w,覆盖写入
	with open('E:\\chemofang\\Config\\varibales.yaml',"w", encoding="utf-8") as f:
		#装载数据
		yaml.dump({key: value},f)
		f.close()

def get_yaml_variable(key=None):
	"""
	提取写入yaml的变量值
	:return:
	"""
	#r读取数据，获取文件
	with open('E:\\chemofang\\Config\\varibales.yaml',"r", encoding="utf-8") as f:
		# 加载数据
		s=yaml.load(f)
		# print(s[key])

		return s[key]
		
	

def dealer_Session():
	"""
	返回车商登陆session
	并写入yaml
	:return:
	"""
	with open('E:\\chemofang\\Config\\conf.yaml', "r", encoding="utf-8") as r:
		config = yaml.load(r)  # 解析并读写yaml文件
		lujing = '/dealer/login'
		host =config['app_host']
		datas =config['delear_info']   #将取出来的str格式转变为dict eval()也可以
		headers =config['app_headers']      #将取出来的str格式转变为dict
		res =RunMethod().run_main('post', host, lujing,datas,headers)
		# print(res)
		write_yaml_variable("X-SessionToken-With",res['data']['token'])
def user_Session():
	with open('E:\\chemofang\\Config\\conf.yaml', "r", encoding="utf-8") as r:
		config = yaml.load(r)  # 解析并读写yaml文件
		lujing = '/users/loginByPwd'
		host =config['app_host']
		datas =config['user_info']
		headers =config['app_headers']
		res =RunMethod().run_main("post",host,lujing,datas,headers)
		# print(res)
	
		write_yaml_variable("X-SessionToken-With", res['data'])


def cms_cookies():
	"""
	返回cmscookies
	:return:
	"""
	with open('E:\\chemofang\\Config\\conf.yaml', "r", encoding="utf-8") as r:
		config = yaml.load(r)  # 解析并读写yaml文件
		s=requests.session()    #session()保留登陆的cookies 返回作为后面请求使用
		datas =eval(config['cms_info'])
		host= config['cms_host']
		url= host+'/cms/login'
		res=s.post(url,datas)
		# print(json.loads(res.text))
		# print(res.cookies.values())
		# return(res.cookies)            # 也可以返回cookies  后面请求加入 cookies=self.cookies

		return s
def qiniu_uploadToken1():
	"""
	返回七牛上传凭证-app
	:return:
	"""
	# print(res1.json()['data'])    #时间戳
	# # print(round((time.time()*1000)))  # 毫秒级时间戳*1000，去掉小数点round()
	# times=round((time.time()*1000))
	with open('E:\\chemofang\\Config\\conf.yaml', "r", encoding="utf-8") as r:
		config = yaml.load(r)  # 解析并读写yaml文件
		
	url1 =config['app_host'] + '/timestamp'
	res1 = requests.get(url1)
	times = res1.json()['data']  # 时间戳
	url2 = config['app_host'] + '/fileToken?timestamp=' + str(times)
	pp = str(times // 8)  # 地板除法 消除小数点
	md5 = hashlib.md5(pp.encode('utf-8')).hexdigest()  # 转换16进制
	upper = md5.upper()  # 转换成大写
	# print(upper,md5)
	header1 = {"X-Signature-With": upper}
	# print(header1)
	res2 = requests.get(url2, headers=header1)
	# print(res2.json())
	uploadToken = res2.json()['data']
	# print(uploadToken)
	return uploadToken
def qiniu_uploadToken2():
	"""
	返回七牛上传凭证-cms
	:return:
	"""
	session=cms_cookies()
	with open('E:\\chemofang\\Config\\conf.yaml', "r", encoding="utf-8") as r:
		config = yaml.load(r)  # 解析并读写yaml文件
	url = config['cms_host'] + '/cms/fileToken'
	# print(url)
	res = session.get(url)
	uploadToken = res.json()['uptoken']
	# print(uploadToken)
	return  uploadToken

		
if __name__ == "__main__":
	# write_yaml_variable("X-SessionToken-With",34434)
	# print(get_yaml_variable("X-SessionToken-With"))
	# write_yaml_variable("BBB",2442)
	# print(get_yaml_variable("BBB"))


	# print(get_yaml_variable("X-SessionToken-With"))
	# cms_cookies()
	# qiniu_uploadToken1()
	# qiniu_uploadToken2()
	dealer_Session()
	# user_Session()
