import pymysql

con=pymysql.connect(host='bordn9sunylocpr1dorc-mysql.services.clever-cloud.com',user='unnjv2kp52dsmz2g',password='iAdIu7xClJRnqBRh39lV',database='bordn9sunylocpr1dorc')
curs=con.cursor()

ra=input('Enter Ram: ')
ro=input('Enter Rom: ')

curs.execute("select * from Mobiles where Ram='%s' and Rom='%s'" %(ra,ro))
data=curs.fetchall()
print(data)



con.close()


