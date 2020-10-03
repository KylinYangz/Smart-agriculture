import pymysql
conn = pymysql.connect(port = '3306',user = "root",db = "zhinengyanglao",passwd = "123456")
cur = conn.cursor()
# cur.execute("INSERT INTO device(device_id) VALUES (2)")
sql="INSERT INTO device(device_id)VALUES (5)"

# sql = "insert into device (device_id) values (12)"
cur.execute(sql)
conn.commit()
cur.close()
conn.close()