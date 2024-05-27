import time
import pymysql as sq

mydb = sq.connect(
    host='localhost',
    user='root',
    password='',
    database='atm'
)
mycursor = mydb.cursor()

def balance():
    print('*************  Balance Details *************\n')
    
    atmCardNo = input("Enter Card Number: ")
    pin = input("Enter PIN Number: ")
    sql = "SELECT * FROM atmsql WHERE atmCardNo=%s AND pin=%s"
    mycursor.execute(sql, (atmCardNo, pin))
    result = mycursor.fetchone()
    print("\nSystem Verifying Information, please wait...")
    
    if result:
        time.sleep(2)
        print(f'''
              ***************************************************************
                        Name: {result[1]}
                        Card Number: {result[0]}
                        ______________________________________
                        Balance: {result[8]}
              ****************************************************************
              ''')  
                
        input("Press any key to continue...")
    else:
        time.sleep(2)
        print("\t\tInvalid Card Number or PIN Number")
        input("Press any key to continue...")

