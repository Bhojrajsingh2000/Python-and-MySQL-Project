import time
import pymysql as sq

mydb = sq.connect(
    host='localhost',
    user='root',
    password='',
    database='atm'
)
mycursor = mydb.cursor()

def greenpin():
    print("=========Create New PIN for your ATM Card=======\n")
    atmCardNo = input("ATM Card Number: ")
    sql = '''SELECT * FROM atmsql WHERE atmCardNo=%s'''
    mycursor.execute(sql, (atmCardNo,))
    result = mycursor.fetchone()
    print("Verifying information, please wait...")
    if result[7]=='':
        if result:
            time.sleep(2)
            print('''
                =============================
                    Your information matched
                =============================
                ''')
            print('Please wait...')
            time.sleep(2)
            while True:
                print("========Create 4 digit PIN number========")
                pin = input("Enter New PIN Number: ")
                pinConfirm = input("Confirm PIN Number: ")
                print("Please Wait...")
                if len(pin) == 4:
                    if pin == pinConfirm:
                        sql = "UPDATE atmsql SET pin=%s WHERE atmCardNo=%s"
                        mycursor.execute(sql, (pin, atmCardNo))
                        mydb.commit()
                        time.sleep(3)
                        print('''
                            ===============================================
                                    Your ATM PIN created successfully
                            ===============================================
                            ''')
                        input("Press Enter to continue...")
                        break
                    else:
                        time.sleep(3)
                        print('''
                            ===============================================================
                                Error: Your ATM PIN & Confirm PIN do not match, try again
                            ===============================================================
                            ''')
                else:
                    time.sleep(3)
                    print('''
                            ===============================================================
                                Error: Your PIN length is not 4, enter only a 4 digit PIN code
                            ===============================================================
                            ''')
        else:
            time.sleep(2)
            print('''
                ===============================================================
                    Error: Your ATM Card Number is not valid, try again
                ===============================================================
                ''')
    else:
            time.sleep(2)
            print('''
                ===============================================================
                    Error: Your ATM Card Pin Already generated
                ===============================================================
                ''')
            input("Press enter to continue...")


