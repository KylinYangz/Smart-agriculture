# -*- coding:utf-8 -*-


print("******************************************************************")
print('正在启动服务，请稍等....')
from flask import Flask, flash, render_template, request
from shujuku import *

# from shenghuobaobiao import *
print('↓ 服务已启动 20% ...')
from jsonjiexi import *
import json

print('↓ 服务已启动 40% ...')
# from gotodie import *
import urllib

# from gotodie import *
# from ways import *


print('↓ 服务已启动 60% ...')
import base64
import random

# from gps import *
print('↓ 服务已启动 80% ...')
from socketlianjie import *
from json import *

# from PIL import Image
# from oldmanadvice import *
print('√ 服务启动完成！')
print("******************************************************************")
ipList = socket.gethostbyname_ex(socket.gethostname())
print("服务器IP地址：%s" % ipList[2][0])
print("******************************************************************")

app = Flask(__name__)


# 打开登录界面
@app.route('/')
def index():
    return render_template('admin/index.html', text='')


from flask import Flask, flash, render_template, request


# 打开用户管理界面
@app.route('/user', methods=['POST'])
def user():
    uid = request.form['uid']
    pwd = request.form['pwd']
    # 如果登录失败，提示并返回登录界面
    if uid == 'admin' and pwd == '123456':
        return render_template('admin/home.html')
    else:
        # 如果登陆成功，返回管理界面
        return render_template('admin/index.html', text='用户名或密码输入错误！请重新输入。')


# 文章页面
@app.route('/ask')
def ask():
    return render_template('admin/ask.html', text='')


# 页面404
@app.route('/404')
def nopage():
    return render_template('admin/404.html', text='')


# 联系页面
@app.route('/content')
def content():
    return render_template('admin/content.html', text='')


# 主页面
@app.route('/home')
def home():
    return render_template('admin/home.html', text='')


# @app.route('/data')
# def data():
# 	return render_template('admin/data.html',text='')


#
@app.route('/ask2')
def ask2():
    return render_template('admin/ask2.html', text='')


@app.route('/ask3')
def ask3():
    return render_template('admin/ask3.html', text='')


@app.route('/xuanze')
def xuanze():
    return render_template('admin/xuanze.html', text='')


# 查询用户数据信息
@app.route('/chaxun/<name>')
def shujuchaxun(name):
    chaxunlei = shujukuchaxun()
    shujubao = chaxunlei.shujuchaxun(name)
    pppp = random.randint(0, 100)
    return render_template('admin/zhanshi.html', rs=shujubao[0:15], page=1, type=name, p=pppp, tishi=name + '数据如下：')


# 翻页操作
@app.route('/page/<name>/<num>')
def fanye(name, num):
    num = int(num)
    chaxunlei = shujukuchaxun()
    shujubao = chaxunlei.shujuchaxun(name)
    pppp = random.randint(0, 100)
    if num == 0:
        return render_template('admin/zhanshi.html', p=pppp, rs=shujubao[0:15], page=1, type=name, tishi=name + '数据如下：')
    elif num > 0:
        ssssssss = shujubao[(num - 1) * 15:(num - 1) * 15 + 15]
        if ssssssss:
            return render_template('admin/zhanshi.html', p=pppp, rs=ssssssss, page=num, type=name, tishi=name + '数据如下：')
        else:
            return render_template('admin/zhanshi.html', p=pppp, rs=shujubao[(num - 2) * 15:(num - 2) * 15 + 15],
                                   page=num - 1, type=name, tishi=name + '数据如下：')


# 选择功能页面
# 选择功能页面
@app.route('/xuanze/<xuanxiang>')
def xuanzejiemian(xuanxiang):  # 老人定位
    if xuanxiang == 'GPS':
        result = open('jsonshuju.text')
        try:
            all_the_text = result.read()

        finally:
            result.close()
        # print(all_the_text)
        # print(all_the_text)
        return render_template('Gpsdingwei.html', result_json=all_the_text)
    # return render_template('admin/Gpsdingwei.html')
    if xuanxiang == 'shujuchaxun':  # 数据查询页面
        return render_template('admin/zhanshi.html', rs=[], tishi="点击左侧列表，进行历史数据查看！")
    if xuanxiang == 'shujujiankong':  # 数据监控页面
        return render_template('admin/shujujiankong.html')


# 返回及时数据给实时监控页面
@app.route('/shishishuju')
def fanhuijishushuju():
    zidian = fanhuishishishuju()  # 获得返回的数据包
    # print(zidian)
    jsonstr = json.dumps(zidian)  # 将数据包转化为json格式数据
    return jsonstr


# 返回选择界面
@app.route('/fanhui')
def fanhuixuanzejiemian():  # 选择返回选择界面 的路由
    return render_template('admin/xuanze.html')


# 为手机端开辟接
@app.route('/jiekou/sjcx/<name>')
def shoujichaxunjiekou(name):
    a = shujukuchaxun()  # 导入类
    if (name == 'fenxi'):
        fan = return_str()
        return fan
    else:
        chaxunname = shoujifanhui(name)  # 获得要查询的数据名称
        s = a.shujuchaxunshouji(chaxunname)  # 得到数据集
        fan = jsongeshifanhuishouji(s)  # 将数据集转化为json格式数据包
        # print(fan)
        return fan  # 返回给手机端


# 控制灯泡和风扇的路由
@app.route('/kongzhi/<name>')
def yuanchengyaokong(name):
    kongzhi(name)
    return render_template('admin/shujujiankong.html')


# 详细信息查询路由
@app.route('/gotodie/<name>/<p>')
def Iwanttogotodie(name, p):
    a = fuck()
    nums = a.huoyancishu(name)
    shuju = a.huoyanchufacushu(name)
    strs = a.time_num(name)
    return render_template('admin/xiangxi.html', names=name, num=nums, rs=shuju, strr=strs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11111, use_reloader=True)
# debug=True




