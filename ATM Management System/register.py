import random 
import time
import pymysql as sq
mydb=sq.connect(
    host='localhost',
    user='root',
    password='',
    database='atm'
)
mycusor=mydb.cursor()
def register():
    print(" Plz Enter correct information...")
    l=[]
    atmCardNo=str(random.randint(100000000000,999999999999))
    l.append(atmCardNo)
    name = input("Enter your name: ")
    l.append(name)
    dob = input("Enter your DOB: ")
    l.append(dob)
    fatherName = input("Enter your Father's Name: ")
    l.append(fatherName)
    address = input("Enter your address: ")
    l.append(address)
    mobile = input("Enter your mobile number: ")
    l.append(mobile)
    adharNo = input("Enter your adhar number: ")
    l.append(adharNo)
    totalAmount=5000
    l.append(totalAmount)
    cust=(l)
    sql='''
    insert into atmsql(atmCardNo, name,dob,fatherName,address,mobile,adharNo,totalAmount ) values(%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    mycusor.execute(sql,cust)
    mydb.commit()
    print("\nPlease wait .....")
    time.sleep(4)
    atmNo=" ".join([atmCardNo[i:i+4] for i in range(0,len(atmCardNo),4)])
    print(f'''
          ************* Note Your ATM Card Number *******************
                   Holder Name: {name}
                   ATM Card Number :  {atmNo}
         
         **********************************************************
         ''')
    input("Press enter to return main menu")

