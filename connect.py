import mysql.connector
conn = mysql.connector.connect(host="localhost",username="root",password="root",database="learning")
my_cursor=conn.cursor()
ins = "insert into student (s_id,s_name) values (%s,%s)"
val =(1,"sam")
ins = "insert into student (s_id,s_name) values (%s,%s)"
val =(2,"ram")
my_cursor.execute(ins,val)
conn.commit()
conn.close()
print('connected successfully')
