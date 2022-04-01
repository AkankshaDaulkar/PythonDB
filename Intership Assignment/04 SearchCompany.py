import pymysql

con=pymysql.connect(host='bordn9sunylocpr1dorc-mysql.services.clever-cloud.com',user='unnjv2kp52dsmz2g',password='iAdIu7xClJRnqBRh39lV',database='bordn9sunylocpr1dorc')
curs=con.cursor()

nm=input ('Enter Company: ')
curs.execute("Select * from Mobiles where Company='%s' order by Price" %nm)
data=curs.fetchall()
#print (data)

for rec in data:
       print(rec)
       
con.close()
