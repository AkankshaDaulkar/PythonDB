import pymysql

con=pymysql.connect(host='bordn9sunylocpr1dorc-mysql.services.clever-cloud.com',user='unnjv2kp52dsmz2g',password='iAdIu7xClJRnqBRh39lV',database='bordn9sunylocpr1dorc')
curs=con.cursor()

nm=input ('Enter Modelname: ')
curs.execute("select* from Mobiles where Modelname='%s'" %nm)
data=curs.fetchone()
print(data)

if data:
      pur=input('Enter Purpose: ')
      curs.execute("update Mobiles set Purpose='%s' where Modelname='%s'" %(pur,nm))
      con.commit()
      print ('Purpose added Sucessfully')
else:
      print('Mobile not found')

con.close()