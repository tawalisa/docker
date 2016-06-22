import mysql.connector

cnx = mysql.connector.connect(user='root', password='secret',
                              host='mysql_pm2',
                              database='pm2')
cursor = cnx.cursor()
add_trace = ("INSERT INTO degrade_tracelog "
               "(phase_id,duration,tracelog) "
               "VALUES (%s, %s, %s)")
data_trace = ('1','123','this test............')
cursor.execute(add_trace, data_trace)
cnx.commit()
cursor.close()
cnx.close()
