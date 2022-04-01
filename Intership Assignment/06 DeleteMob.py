import pymysql

con=pymysql.connect(host='bordn9sunylocpr1dorc-mysql.services.clever-cloud.com',user='unnjv2kp52dsmz2g',password='iAdIu7xClJRnqBRh39lV',database='bordn9sunylocpr1dorc')
curs=con.cursor()

no=int(input('Enter Prodid: '))
curs.execute("select * from Mobiles where Prodid=%d" %no)
data=curs.fetchone()
print (data)

if data:
    ask=input('Do you want to delete? yes or no: ')

    if ask=='yes':
        curs.execute("delete from Mobiles where Prodid=%d" %no)
        con.commit()
        print('Mobile data deleted sucessfully')
        
    elif ask=='no':
        print ('Mobile data remain same')

else:
    print('Mobile does not exit')

con.commit()
