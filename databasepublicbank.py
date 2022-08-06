from ast import main
from ssl import OP_ENABLE_MIDDLEBOX_COMPAT
import pymysql
import string
import random

con = None
cur = None

def dbconnect():
    global con,cur
    try:
        con = pymysql.connect(host='localhost',
                        database='bank1',
                        user='root',
                        password='')
        cur = con.cursor()
    except Exception as e:
        print(e)
#    cur = con.cursor()

def dbdisconnect():
    con.close()

number = string.digits
num = list(number)
random.shuffle(num)

def OpenAc():
    dbconnect()
    n = input ('Enter your Name : ')
#    ac = int(input('Enter your Account Number : '))
    ac = "".join(num)
    dob = input('Enter your D.O.B in (DD-MM-YYYY) : ')
    addr = input('Enter your Address :')
    mob = int(input('Enter your Mobile Number : '))
    opbal = int(input('Enter Opening Balance : '))
    data1 = (n,ac,dob,addr,mob,opbal)
    data2 = (n,ac,opbal)
    sql1 = "insert into account values(%s,%s,%s,%s,%s,%s)"
    sql2 = "insert into amount values(%s,%s,%s)"
    cur = con.cursor()
    cur.execute(sql1,data1)
    cur.execute(sql2,data2)
    con.commit()
    print ("Account opened Successfully")
    dbdisconnect()

def DepoAmt():
    dbconnect()
    amt = int(input('Enter Deposit Amount : '))
    ac = int(input('Enter your Account Number : '))
    a1 = "select balance from amount where Acno = %s"
    data = (ac,)
    cur = con.cursor()
    cur.execute(a1,data)
    myresult = cur.fetchone()
    tamt = myresult[0]+amt
    sql1 = "update amount set balance = %s where Acno = %s"
    d = (tamt,ac)
    cur.execute(sql1,d)
    con.commit()
    print ("Amount Deposited Successfully")
    dbdisconnect()

def WithAmt():
    dbconnect()
    amt = int(input('Enter Withdrawal Amount : '))
    ac = int(input('Enter your Account Number : '))
    a = "select balance from amount where Acno = %s"
    data = (ac,)
    cur = con.cursor()
    cur.execute(a,data)
    myresult = cur.fetchone()
    n=0
    while(n<=0):

        if (myresult[0] - amt)>=5000:
            sql = "update amount set balance = %s where Acno = %s"
            tamt = myresult[0]-amt
            d = (tamt,ac)
            cur.execute(sql,d)
            con.commit()
            print ("Amount Withdrawn Successfully")
        else:
            print ('INSUFFICIENT BALANCE')
            break
        n+=1
    dbdisconnect()

def BalEnq():
    dbconnect()
    ac = int(input('Enter your Account Number : '))
    a = "select balance from amount where Acno = %s"
    data = (ac,)
    cur = con.cursor()
    cur.execute(a,data)
    myresult = cur.fetchone()
    print ("Balance for Account No.",ac,"is : ",myresult[0],"Rupees only")
    dbdisconnect()

def DispAc():
    dbconnect()
    ac = int(input('Enter your Account Number : '))
    a = "select * from account where Acno = %s"
    data = (ac,)
    cur = con.cursor()
    cur.execute(a,data)
    myresult = cur.fetchone()
    for i in myresult:
        print (i)
    dbdisconnect()

def CloseAc():
    dbconnect() 
    ac = int(input('Enter your Account Number : '))
    sql1 = "delete from account where Acno = %s"
    sql2 = "delete from amount where Acno = %s"
    data = (ac,)
    cur = con.cursor()
    cur.execute(sql1,data)
    cur.execute(sql2,data)
    con.commit()
    print ("Account number",ac,"is closed permanently")
    dbdisconnect()