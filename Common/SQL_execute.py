# -*- coding: utf-8 -*- 
# @Time : 2018/12/19 17:32 
# @Author : taojian 
# @File : SQL_execute.py
# 封装mysql  mysql_info 连接池配置信息
import pymysql

from utx import Log

mysql_info = {"host": "192.168.31.173",
              "user": "mfcar",
              "password": "12345678",
              "db": 'mfcar_test',
              "port": 3306,
              "charset": "utf8"}


class MysqlUtil():
	'''
	mysql 数据库相关操作
	连接数据库信息：mysql_info
	创建游标：mysql_execute
	查询某个字段对应的字符串：mysql_getstring
	查询一组数据：mysql_getrows
	关闭 mysql 连接：mysql_close
	'''
	
	def __init__(self):
		self.db_info = mysql_info
		u'''连接池方式'''
		self.conn = MysqlUtil.__getConnect(self.db_info)
	
	@staticmethod
	def __getConnect(db_info):
		# 静态方法：@staticmethod
		# 不能访问实例属性！！！   参数不能传入self！！！
		# 与类相关但是不依赖类与实例的方法！！
		'''静态方法，从连接池中取出连接'''
		try:

			conn = pymysql.connect(host=db_info['host'],
			                       port=db_info['port'],
			                       user=db_info['user'],
			                       passwd=db_info['password'],
			                       db=db_info['db'],
			                       charset=db_info['charset'])
			return conn  # 打开数据库操作
		except Exception  as a:
			Log().debug("数据库连接异常：%s" % a)
	
	# print("数据库连接异常：%s"%a)
	def mysql_execute(self,sql,number=None):
		'''执行 单表sql 语句'''
		cur = self.conn.cursor()
		try:
			if number=='one':
				cur.execute(sql)
			elif number=='more':
				cur.executemany(sql)
			else:
				pass
		except Exception as a:
			self.conn.rollback()  # sql 执行异常后回滚
			Log().debug("执行 SQL 语句出现异常：%s" % a)
		# print("执行 SQL 语句出现异常：%s"%a)
		else:
			cur.close()
			self.conn.commit()  # sql 无异常时提交
			
	
	def mysql_getrows(self, sql,number=None):
		''' 返回查询结果'''
		cur = self.conn.cursor()
		try:
			cur.execute(sql)
		except Exception as a:
			Log().debug("查询结果错误：%s" % a)
		# print("查询结果错误：%s" % a)
		if number=='one':
			row = cur.fetchone()
			return row
		elif number == 'more':
			rows = cur.fetchall()
			cur.close()
			return rows
		else:
			pass
		cur.close()
	
	
	def mysql_getstring(self, sql):
		'''查询一行的所有值'''
		rows = self.mysql_getrows(sql,'one')
		if rows != None:
			for row in rows:
				print(row)
	
				# for i in row:
				# 	print(i)
	
	def mysql_close(self):
		''' 关闭 close mysql'''
		
		try:
			self.conn.close()
		except Exception as a:
			Log().debug("数据库关闭异常：%s" % a)
	# print("数据库关闭时异常：%s" % a)


if __name__ == "__main__":
	mysql = MysqlUtil()
	# sql = "SELECT * FROM test_hsry_data WHERE `code`  between '4260000' and '4260010'"
	sql1 = "select * from order_info where order_no='20201812191425320005'"
	sqls="UPDATE order_pledge SET status = 'CLOSED_DEALER' where user_id= '5b42f9b7cec76d75f185d4ec'"
	sql2="select * from dealer_car where car_info_id= '5a5ec113943d0b515a43b33a' ORDER BY id DESC "
	mysql.mysql_execute(sql1,number='one')
	mysql.mysql_execute(sqls,number='one')
	mysql.mysql_execute(sql2,number='one')
	# print(mysql.mysql_getrows(sql1,'one'))
	# print(mysql.mysql_getrows(sqls,'one'))
	print(mysql.mysql_getrows(sql2,number='one'))

	print(mysql.mysql_getstring(sql2))
	mysql.mysql_close()