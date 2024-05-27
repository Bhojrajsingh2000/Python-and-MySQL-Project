import time
import pymysql as sq

def connect_to_database():
    try:
        return sq.connect(
            host='localhost',
            user='root',
            password='',
            database='atm'
        )
    except sq.MySQLError as e:
        print("Error connecting to the database: ", e)
        return None

def credit():
    mydb = connect_to_database()
    if mydb is None:
        return

    mycursor = mydb.cursor()

    print('*************  Withdraw Amount  *************\n')
    
    atmCardNo = input("Enter Card Number: ")
    pin = input("Enter PIN Number: ")

    try:
        sql = "SELECT * FROM atmsql WHERE atmCardNo=%s AND pin=%s"
        mycursor.execute(sql, (atmCardNo, pin))
        result = mycursor.fetchone()
        print("\nVerifying Information, please wait...")

        if result:
            time.sleep(2)
            print(f'''
                    =============================
                        Your information matched
                    =============================
                      Name : {result[1]} 
                      Card No : {result[0]}
                      Total Amount : {result[8]}  
                    =============================
                    ''')
            print('Please wait...')
            time.sleep(2)
            
            while True:
                try:
                    amount = int(input("Enter Withdrawal amount: "))
                    if amount <= 0:
                        print("Please enter a positive amount.")
                        continue
                    break
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
            
            if result[8] > amount:
                totalAmount = result[8] - amount
                try:
                    sql = "UPDATE atmsql SET totalAmount=%s WHERE atmCardNo=%s AND pin=%s"
                    mycursor.execute(sql, (totalAmount, atmCardNo, pin))
                    mydb.commit()
                except sq.MySQLError as e:
                    print("Error updating the database: ", e)
                    return

                print("Please Wait...")
                time.sleep(2)
                print(f'''
                    =============================
                        Your Transaction Success
                    
                        Balance : {totalAmount}
                    =============================
                    ''')
                time.sleep(1)
                print("========Thank You! =========")
                input("Press any key to continue...")
            else:
                print(f'''
                    =============================
                        Insufficient funds
                        Balance : {result[8]}
                    =============================
                    ''')
                input("Press any key to continue...")
        else:
            time.sleep(2)
            print("\t\tInvalid Card Number or PIN Number")
            input("Press any key to continue...")
    except sq.MySQLError as e:
        print("Error executing the query: ", e)
    finally:
        mycursor.close()
        mydb.close()


