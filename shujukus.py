import pymysql
class shujukuchaxun(object):
	def shujuchucun(self):
		try:
			conn = pymysql.connect(host='localhost', user='root', passwd='123456', database='zhinengyanglao',
								   charset='utf8')  # 链接数据库
			cursor = conn.cursor()  # 获得游标

			sql = "insert into xinxi (id,name,device_id,device_type,transfer_type,timestamp,device_value) values  (%s,'%s',%s,%s,'%s','%s','%s')" % (7, 'wkw', 12, 23, 'wer', '2018-10-11 14:42:44', 'sdf')

			# sql="insert into xinxi (name,device_id,device_type,transfer_type,timestamp,device_value) values ('wkw',12,23,'wer','re','sdf')"

			cursor.execute(sql)  # 执行

			conn.commit()  # 提交添加数据的命令

			cursor.close()
			conn.close()
			print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
		except Exception as e:
			print('数据库链接失败！')
