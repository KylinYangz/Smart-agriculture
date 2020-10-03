#coding:utf-8
import json
import os

shijian={}
changyongshijianlist=[]
lujing = os.path.dirname(__file__) #获取当前文件夹的绝对路径
path=lujing+'\\static\\wenjian\\time.txt'
path2=lujing+'\\static\\wenjian\\max.txt'

def duqu():  #获取txt中的数据
	with open(path,'r') as du:
		jsonstr=du.read()
		shijiandic=json.loads(jsonstr)
		shijian=shijiandic
	return shijian

shijian=duqu()  #获取数据赋值给字典


def zuida():  # 找最大的时间
	li=[] # 值的集合
	li=[] # 值的集合
	listshijian=[] # 获取最大时间并返回
	t=""
	for i in shijian.values():
		li.append(int(i))
	da=max(li)
	if da >=10:
		for x,y in shijian.items():
			if y==da:
				num=int(x)
		try:
			shi=num//4
		except Exception as e:
			shi=00
			fen=00
		fen=(num%4)*15
		ss=str(shi).zfill(2)+str(fen).zfill(2)
		with open(path2,'w') as du:
			du.write(ss)
		shii=ss[:2]
		fenn=ss[2:4]
		listshijian.append(shii)
		listshijian.append(fenn)
		return listshijian
	else:
		with open(path2,'w') as du:
			du.write('[25,25]')
		listshijian.append(25)
		listshijian.append(25)
		return listshijian

changyongshijianlist=zuida()  #获得常用时间的字符串	
	
	
def  kaidongshijianchucun(time):   #传入时间处理
	# time= 2017-01-30 14:05:20
	shi=int(time[11:13])
	fen=int(time[14:16])
	if fen>=0 and fen<15:
		fen=0
	elif fen>=15 and fen<30:
		fen=1
	elif fen>=30 and fen<45:
		fen=3
	else:
		fen=4
	num=int(shi)*4+int(fen)
	shijian[str(num).zfill(2)]=shijian[str(num).zfill(2)]+1
	with open(path,'w') as du:
		shijianstr=json.dumps(shijian)
		du.write(shijianstr)
	changyong=zuida()
	return changyong
	
	

def changyongshijianfanhui():
	return changyongshijianlist



































