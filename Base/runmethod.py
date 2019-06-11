#coding=utf-8
"""接口模块/流程性封装的请求方法"""
import requests
import json

from utx import Log


class RunMethod:

	def post_main(self,host,lujing,data,headers=None):      #host 为基础url ，lujing为路径
		try:
			# print(type(data))
			if type(data)==dict:          #判断是否为dict 类型
				# print("ok")
				data=data
			else:
				# print("nooo")
				data=eval(data)        #如果data 不是dict 类型 就必须先是str 然后转成dict
				
			url=host+lujing
			# print(url)
			if headers != None:
				if type(headers)==dict:
					headers=headers
				else:
					headers=eval(headers)        #如果data 不是dict 类型 就必须先是str 然后转成dict
		
				res=requests.post(url=url,json=data,headers=headers,verify=False)
			else:
				res=requests.post(url=url,json=data,verify=False)
		
			response =res.json()   #  将返回的数据转换为json格式的 字典
			# print(type(response))
			# print(response['code'])
			if 	response['code'] != 200:      #当返回的不为200时记录到log中
				Log().info(res.json())
			return   response
	
		except Exception as e:
				Log().debug('post 请求错误 错误原因为%s'%e)
				return('post 请求错误 错误原因为%s'%e)

			
		
	def get_main(self,host,lujing,data=None,headers=None):
		try:
			url = host + lujing

			if headers != None:
				# print("ok")
				if type(headers) == dict:
					headers = headers
				else:
					headers = eval(str(headers))  # 如果data 不是dict 类型 就必须先是str 然后转成dict
				res=requests.get(url=url,data=data,headers=headers,verify=False)
				# print(res)
			else:
				res=requests.get(url=url,data=data,verify=False)
				
			response = res.json()        #res.text 为str格式 json。loads（）将str-dict、
			if response['code'] != 200:  # 当返回的不为200时记录到log中
				print("oK")
				Log().info(res.json())
			return response
		except Exception as e:
				Log().debug('get 请求错误 错误原因为%s'%e)
				return('get 请求错误 错误原因为%s'%e)
	def run_main(self,method,host,lujing,data=None,headers=None):
		if method=='post':
			res=self.post_main(host,lujing,data,headers)
			return res
		if method=='get':
			res=self.get_main(host,lujing,data,headers)
			return res


if __name__ == '__main__':
	run = RunMethod()  # 实例化
	host='http://192.168.31.172:8080'
	lujing='/dealer/login'
	datas={"mobile":"18657738815","password":"dc483e80a7a0bd9ef71d8cf973673924"}

	headers={"version":"2.0.0","Connection":"keep-alive","Content-Type":"application/json; charset=utf-8"}
	res=run.run_main('post',host,lujing,datas,headers)
	print(res)
	print(type(res))
