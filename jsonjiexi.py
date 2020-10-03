#coding:utf-8
import json
import time
import datetime
from shujuku import shujukuchaxun  # 导入 数据库 模块
from tj import * # 导入 自主学习 模块

shujuchucun=shujukuchaxun()  # 实例化 数据库查询 类
zizhuxuexikaideng=0
fanhui={}  # 返回给实时监控页面的数据-------------------------------？？？？
jiushujuji={'温度':0,'湿度':0,'可燃气体':0,'光照':0,'烟雾浓度':0,'电灯':'0','风扇':'0','人体红外':'0','触摸按键':'0','声音':'0','火焰':'0','磁场':'0','六轴':'0','心率':0,'震动':'0','测试数据':0}



class shujuchuli(object):

	def jiexi(self,ss):   # 将数据包进行json解析
		try:
			s=json.loads(ss) # 将json数据解析成 python 格式数据
			device_id=s['device_id']   # 设备ID
			# device_type=s['device_type']   # 设备类型
			transfer_type=s['transfer_type']   # 传输类型
			device_value=s['device_value']   # 值
			timestamp=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())   # 当前时间
			#print(timestamp)
			#print(timestamp)
			name=namejiexi(device_id,device_value)   # 获得ID对应的设备名称
			# print(name,'数据接收成功！')
			if name=='电灯' and device_value=='true':  # 如果接收灯泡开的命令，就交给自主学习处理
				changyongshijianlist=kaidongshijianchucun(timestamp)  # 调用储时间数据的方法并重新计算常用时间
			xinshuju=fanhui[name]
			jiushuju=jiushujuji[name]
			if name == '人体红外' or name=='火焰' or name == '触摸按键' or name == '声音':
				if(xinshuju!=jiushuju):



					# print("aa")
					shujuchucun.shujuchucun(name,device_id,transfer_type,timestamp,device_value)  # 调用函数，储存处理好的数据
					jiushujuji[name]=xinshuju
			if name=='温度' or name=='湿度':
				if int(xinshuju)-int(jiushuju)>=2 or int(jiushuju)-int(xinshuju)>=2:
					shujuchucun.shujuchucun(name,device_id,transfer_type,timestamp,device_value)  # 调用函数，储存处理好的数据
					jiushujuji[name]=xinshuju
			elif name=='光照' or name=='可燃气体' or name=='烟雾浓度':
				if int(xinshuju)-int(jiushuju)>=20 or int(jiushuju)-int(xinshuju)>=20:
					shujuchucun.shujuchucun(name,device_id,transfer_type,timestamp,device_value)  # 调用函数，储存处理好的数据
					jiushujuji[name]=xinshuju
			elif name=='心率':
				if int(xinshuju)-int(jiushuju)>=5 or int(jiushuju)-int(xinshuju)>=5:
					shujuchucun.shujuchucun(name,device_id,transfer_type,timestamp,device_value)  # 调用函数，储存处理好的数据
					jiushujuji[name]=xinshuju
			# elif name=='六轴':
				# if xinshuju!=jiushuju:
					# shujuchucun.shujuchucun(name,device_id,device_type,transfer_type,timestamp,device_value)  # 调用函数，储存处理好的数据
					# jiushujuji[name]=xinshuju
			# elif name=='磁场':
				# x_new=int(xinshuju[2:4])
				# x_old=int(jiushuju[2:4])
				# if x_new - x_old >=20 or x_old - x_new >=20:
					# shujuchucun.shujuchucun(name,device_id,device_type,transfer_type,timestamp,device_value)  # 调用函数，储存处理好的数据
					# jiushujuji[name]=xinshuju
			elif name=='电灯' or name=='风扇':
				if(xinshuju!=jiushuju):
					shujuchucun.shujuchucun(name,device_id,transfer_type,timestamp,device_value)  # 调用函数，储存处理好的数据
					jiushujuji[name]=xinshuju
			else:
				pass

			shizhong=int(timestamp[11:13])  # 当前时间的时
			fenzhong=int(timestamp[14:16])  # 当前时间的分
			changyongshijianlist=changyongshijianfanhui()

			changshi=int(changyongshijianlist[0]) #自主学习的时

			changfen=int(changyongshijianlist[1]) #自主学习的分
			if name=='电灯' and device_value=='true' and shizhong==changshi and fenzhong>changfen: # 如果时间和自主学习时间差不多，就开启电灯
				zizhuxuexikaideng=1

		except Exception as e:
			return




def namejiexi(id,value):  # 创建方法，用来获得ID对应的设备名称
	if id==1:
		name='温度'
	elif id==2:
		name='湿度'
	elif id==3:
		name='光照'
	elif id==7:
		name='可燃气体'
	elif id==8:
		name='烟雾浓度'
	elif id==101:
		name='电灯'
	elif id==102:
		name='风扇'
	elif id==151:
		name='人体红外'
	elif id==153:
		name='触摸按键'
	elif id==154:
		name='声音'
	elif id==156:
		name='火焰'
	elif id==10:
		name='磁场'
	elif id==4:
		name='六轴'
	elif id==32:
		name='心率'
	elif id==160:
		name='震动'
	else:
		name='测试数据'

	fanhui[name]=value
	return name


def fanhuishishishuju():
	return fanhui


#  解析从手机API接收过来的数据名称
def shoujifanhui(name):
	if name=='wendu':
		newname='温度'
	if name=='shidu':
		newname='湿度'
	if name=='guangzhao':
		newname='光照'
	if name=='keranqiti':
		newname='可燃气体'
	if name=='yanwunongdu':
		newname='烟雾浓度'
	if name=='diandeng':
		newname='电灯'
	if name=='fengshan':
		newname='风扇'
	if name=='rentihongwai':
		newname='人体红外'
	if name=='chumoanjian':
		newname='触摸按键'
	if name=='shengyin':
		newname='声音'
	if name=='huoyan':
		newname='火焰'
	if name=='cichang':
		newname='磁场'
	if name=='liuzhou':
		newname='六轴'
	if name=='xinlv':
		newname='心率'
	if name=='zhendong':
		newname='震动'
	else:
	    pass

	return newname

# 将数据转化为json格式数据包返回给手机API
def jsongeshifanhuishouji(lists):
	jsons=[]
	for l in lists:
		js={}
		js['name']=l[0]
		js['timestamp']=l[1].strftime('%m-%d %H:%M')
		valuestr = fuckpython(l[0],l[2])
		js['device_value']=valuestr
		jsons.append(js)
	jsonstr=json.dumps(jsons)
	return (jsonstr)



def fuckpython(name,neirong):
	str=""
	if name=='温度':
		str=neirong+"℃"
	elif name=='湿度':
		str=neirong+"%"
	elif name=='光照':
		str=neirong+"lux"
	elif name=='可燃气体':
		str=neirong+"PPM "
	elif name=='烟雾浓度':
		str=neirong+"PPM "
	elif name=='电灯' or name=="风扇" or name=="触摸按键":
		if(neirong=="true"):
			str="开启"
		else:
			str="关闭"
	elif name=='火焰' or name=="声音" or name=="人体红外":
		if(neirong=="true"):
			str="危险"
		else:
			str="安全"
	elif name=='心率':
		str=neirong
	else:
	    pass

	return str



#
#
# # cording:utf-8
# import time
# import json
# import datetime
# from shujuku import *
# from tj import *


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		