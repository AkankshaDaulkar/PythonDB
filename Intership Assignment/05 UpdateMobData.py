import pymysql


con=pymysql.connect(host='bordn9sunylocpr1dorc-mysql.services.clever-cloud.com',user='unnjv2kp52dsmz2g',password='iAdIu7xClJRnqBRh39lV',database='bordn9sunylocpr1dorc')
curs=con.cursor()

no=int(input('Enter Prodid= '))
curs.execute("select * from Mobiles where Prodid=%d" %no)
data=curs.fetchone()

if data:
    pri=float(input('Enter Price= '))
    curs.execute("update Mobiles set Price=%.2f where Prodid=%d" %(pri,no))
    con.commit()
    print("Mobile data updated")

else:
    print("Mobile does not found")

con.close()