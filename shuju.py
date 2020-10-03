import pymysql

db = pymysql.connect(host='localhost', user="root", passwd="123456", db="zhinengyanglao",charset='utf8')
cursor = db.cursor()
# sql = "insert into  xinxi (device_id) values ('78')"
# sql = "insert into  qqq (saas,s,tt) values ('78','ss','d')"

name=1
device_id=6
device_type=6
transfer_type=6
timestamp=5
device_value=5

sql="insert into xinxi (id,name,device_id,device_type,transfer_type,timestamp,device_value) values  (%s,'%s',%s,%s,'%s','%s','%s')" %(3,'wkw',12,23,'wer','2018-10-11 14:42:44','sdf')
# sql="insert into  xinxi (name,device_id,device_type,transfer_type,timestamp,device_value) values ('wkw',12,23,'wer','2018-10-11 14:42:44','sdf')"
# sql = "insert into  abc (name,device_id,device_type,transfer_type,timestamp,device_value) values ('22',6,'dd','wer','2018-10-11 14:42:44','ddd')"
try:
    cursor.execute(sql)
    db.commit()
except:

   db.rollback()
db.close()
cursor.close()
