#coding:utf-8
import socket
import sys
import _thread
import time
import threading
import re
import json
from jsonjiexi import *   # 导入json解析模块



res= r'{[\w:\'\"-\., ]*}'
zhengze=re.compile(res) # 正则表达式
shujujiexi=shujuchuli() # 实例化 数据库处理 类




def jieshou():  # 数据接收方法，接收数据


	while True:
		try:
			msg=s.recv(2048)

			#print(222)
			shujuzu=zhengze.findall(msg.decode('utf-8')) # 正则表达式获得数据组
			# print(shujuzu)
			for shujutiao in shujuzu:
				# print(shujutiao)

				#print(444)
				shujujiexi.jiexi(shujutiao)  # 数据组进行解析
			if zizhuxuexikaideng==1:
				kongzhi('diandengkaiqi')
		except Exception as e:
			print(e)
			return
			
			
class myThread(threading.Thread):   # 多线程类，处理数据接收问题
	
	def run(self):
		#print(1111)
		jieshou()

def kongzhi(num):
	try:
		if num=='diandengkaiqi':
			strr="{\"args\":{\"device_value\":\"true\",\"device_type\":24,\"device_id\":101},\"cmd\":\"set_switch\"}\n"# 电灯
		elif num=='fengshankaiqi':
			strr="{\"cmd\":\"set_switch\",\"args\":{\"device_value\":\"true\",\"device_type\":24,\"device_id\":102}}\n" # 风扇
		elif num=='zhendongkaiqi':
			strr="{\"args\":{\"device_value\":\"true\",\"device_type\":24,\"device_id\":160},\"cmd\":\"set_switch\"}\n" # 震动
		elif num=='diandengguanbi':
			strr="{\"args\":{\"device_value\":\"false\",\"device_type\":24,\"device_id\":101},\"cmd\":\"set_switch\"}\n" # 电灯
		elif num=='fengshanguanbi':
			strr="{\"args\":{\"device_value\":\"false\",\"device_type\":24,\"device_id\":102},\"cmd\":\"set_switch\"}\n" # 风扇
		elif num=='zhendongguanbi':
			strr="{\"args\":{\"device_value\":\"false\",\"device_type\":24,\"device_id\":160},\"cmd\":\"set_switch\"}\n" # 震动
		#jsonstr=json.dumps(strr);
		#jsonstrr=jsonstr+"\n"
		s.send(strr.encode('utf-8'))
	except Exception as e:
		return  e

		
		
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	host=socket.gethostname()
	port=51001
	s.connect(('192.168.1.103',port))   # 开始链接
	print("连接成功！服务器：",host,"，端口号：",port)
	h=myThread()  # 开启 多线程，进行数据接收
	h.start()
except Exception as e:
	print('× 与设备链接失败！')


