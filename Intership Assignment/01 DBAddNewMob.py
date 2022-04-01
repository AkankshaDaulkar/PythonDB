import pymysql
try:
    no=int(input ('Enter Prodid: '))
    nm=input('Enter Modelname: ')
    com=input('Enter Company:  ')
    conn= input ('Enter Connectivity: ')
    ram=input('Enter Ram: ')
    rom=input('Enter Rom: ')
    col=input('Enter Color: ')
    sc=input('Enter Screen: ')
    bat=input('Enter Battery: ')
    pro=input('Enter Processor: ')
    pri=float(input('Enter Price: '))
    rat=float(input('Enter Rating: '))
    pur=input('Enter Purpose: ')

    con=pymysql.connect(host='bordn9sunylocpr1dorc-mysql.services.clever-cloud.com',user='unnjv2kp52dsmz2g',password='iAdIu7xClJRnqBRh39lV',database='bordn9sunylocpr1dorc')
    curs=con.cursor()
    curs.execute("insert into Mobiles values(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s',%.2f,%.2f,'%s')"%(no,nm,com,conn,ram,rom,col,sc,bat,pro,pri,rat,pur))
    con.commit()
    print ('New mobile data stored in the DB table')
    
except:
    print('Error in data....cant insert')

con.close()
