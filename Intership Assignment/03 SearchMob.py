import pymysql

con=pymysql.connect(host='bordn9sunylocpr1dorc-mysql.services.clever-cloud.com',user='unnjv2kp52dsmz2g',password='iAdIu7xClJRnqBRh39lV',database='bordn9sunylocpr1dorc')
curs=con.cursor()

nm=input('Enter Modelname: ')
curs.execute("Select* from Mobiles where Modelname='%s'" %nm)
data=curs.fetchone()

if data:
     print(data)
else:
    print('Data not found')
