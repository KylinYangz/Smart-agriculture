# coding:utf-8
import pymysql
import datetime
import time
import random
from time import time, localtime, strftime


# from PIL import Image
class shujukuchaxun(object):

	# 从数据库查询数据
	def shujuchaxunshouji(self, name):
		try:
			conn = pymysql.connect(user='root', passwd='123456', database='zhinengyanglao', charset='utf8')  # 链接数据库
			cursor = conn.cursor()  # 获得游标
			sql = "select name,timestamp,device_value from xinxin where name='%s' ORDER BY id DESC;" % name  # 查询数据SQL语句
			cursor.execute(sql)  # 执行
			ss = cursor.fetchmany(50)  # 获得返回数据
			cursor.close()  # 关闭游标
			conn.close()  # 关闭数据库链接
			return ss  # 返回查询得到的数据组
		except Exception as e:
			print('数据库链接失败！')

	#  从数据库查询数据
	def shujuchaxun(self, name):
		try:
			conn = pymysql.connect(user='root', passwd='123456', database='zhinengyanglao', charset='utf8')  # 链接数据库
			cursor = conn.cursor()  # 获得游标
			sql = "select * from xinxin where name='%s' ORDER BY id DESC;" % name  # 查询数据SQL语句
			cursor.execute(sql)  # 执行
			ss = cursor.fetchall()  # 获得返回数据
			cursor.close()  # 关闭游标
			conn.close()  # 关闭数据库链接

			return ss  # 返回查询得到的数据组
		except Exception as e:
			print('数据库链接失败！')

	def getfood_s(self):
		try:
			conn = pymysql.connect(user='root', passwd='123456', database='xixi', charset='utf8')
			cursor = conn.cursor()
			random_s = random.randint(715, 727)
			id = random_s
			sql = "select title,content from movie_s where id='%d'" % id
			cursor.execute(sql)
			test = cursor.fetchall()
			cursor.close()
			conn.close()
			return (test)
		except Exception as e:
			print(e)

	def query(self):
		try:
			conn = pymysql.connect(user='root', passwd='123456', database='xixi', charset='utf8')
			cursor = conn.cursor()
			date = strftime("%A", localtime(time()))
			# print(date)
			sql = "select breakfast,lunch,dinner,advice FROM oldmanfood WHERE mame='%s'" % date
			cursor.execute(sql)
			# print(33)
			task = cursor.fetchall()
			# print(44)
			cursor.close()
			conn.close()
			return (task)

		except Exception as e:
			print(e)

	# def query_food_id(self):
	# 	try:
	# 		conn = pymysql.connect(user = 'root',passwd = '123456',database = 'xixi',charset = 'utf8')
	# 		cursor = conn.cursor()
	# 		sql = "select id from foods_s"
	# 		cursor.execute(sql)
	# 		id_s = cursor.fetchall()
	# 		cursor.close()
	# 		conn.close()
	# 		return id_s
	# 		#id_s = list(id_s)
	# 		# for i in id_s:
	# 		# 	i = i[0]
	# 		# 	#i = int(i)
	# 		# 	print(i)
	# 		# 	#return (i)
	# 		# 	#print (type(i))
	# 	except Exception as e:
	# 		print(e)

	def query_food(self):
		try:
			conn = pymysql.connect(user='root', passwd='123456', database='xixi', charset='utf8')
			cursor = conn.cursor()
			# 	a = shujukuchaxun.query_food_id(self)
			# 	a = list(a)
			# 	print(a)
			# 	for i in a:
			# 		i = i[0]
			# 		#print(i)
			# 		mac = str(i)
			# 		mac = list(mac)
			# 		print(max(mac))

			random_s = random.randint(1219, 1223)
			id = random_s
			sql = "select title_s,content_s from foods_s where id='%d'" % id
			cursor.execute(sql)
			test = cursor.fetchall()
			cursor.close()
			conn.close()
			return (test)
		except Exception as e:
			print(e)

	# 向数据库储存数据
	def shujuchucun(self, name, device_id, transfer_type, timestamp, device_value):
		try:
			conn = pymysql.connect(host='localhost', user='root', passwd='123456', database='zhinengyanglao',
								   charset='utf8')  # 链接数据库
			cursor = conn.cursor()  # 获得游标
			# 向数据库添加数据的SQL语句
			# print(5555)
			sql = "insert into xinxin (name,device_id,transfer_type,timestamp,device_value) values ('%s',%s,'%s','%s','%s')" % (
				name, device_id, transfer_type, timestamp, device_value)
			# sql="insert into xinxi (name,device_id,device_type,transfer_type,timestamp,device_value) values ('wkw',12,23,'wer','re','sdf')"
			# print(666)
			cursor.execute(sql)  # 执行

			conn.commit()  # 提交添加数据的命令

			cursor.close()

			conn.close()
		except Exception as e:
			print('数据库链接失败！')


if __name__ == "__main__":
	a = shujukuchaxun()
	a.query()
