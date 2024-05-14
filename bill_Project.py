import pandas as pd
import pymysql as mq
mydb = mq.connect(
    host='localhost',
    user='root',
    password='',
    database='bill'
)
mycursor=mydb.cursor()

def item_billing():
    print('************* Enter Item Billing Details*************')
    
    try:
        l=[]
        item_name = input("Enter item Name : ")
        l.append(item_name)
        price=int(input("Enter Price/item: "))
        l.append(price)
        quantity=int(input("Enter Quantity : "))
        l.append(quantity)
        total_price=price*quantity
        l.append(total_price)
        cust=(l)
        sql ='''
                insert into item (item_name, price, quantity, total_price) values(%s, %s, %s, %s)
        '''
    
        mycursor.execute(sql,cust)
        mydb.commit()
        print('********************************')
        print('Total Amount: ' ,total_price)
        print('********************************')
        print('\n********Invoice Created Successfully*********\n')
        input('Press Enter to continue...')
    except ValueError:
        print('****************************************************************')
        print('\n\t>>>Error : You are enter  Worng Value so comes valuerror\n\n')
        print('****************************************************************') 
        input('Press Enter to continue...')

def view_invoice():
    try:
        l=[]
        print('********************************')
        serial_no=int(input("Enter invoice Serial Number : "))
        print('********************************')
        l.append(serial_no)
        cust=(l)
        sql='''
            select * from item where serial_no=%s
        '''
        mycursor.execute(sql,cust)
        result=mycursor.fetchall()
        k=pd.DataFrame(result,columns=['Serial Number','Item Name','Price','Quantity','Total Amount'])
        print(k)
        input('\n\nPress Enter to continue...')
    except ValueError:
        print('****************************************************************')
        print('\n\t>>>Error : You are enter  Worng Value so comes valuerror\n\n')
        print('****************************************************************') 
        input('Press Enter to continue...')

def update_invoice():
    try:
        while True:
            print('''
                ========== Update Invoice =================
                1. Update All Item Data")
                2. Exit''')
            print('********************************')
            choice = int(input("Enter your choice: "))
            print('********************************')
            if choice == 1:
                serial_no = int(input('Enter Serial Number: '))
                item_name = input('Update Item Name: ')
                price = int(input('Update Item Price: '))
                quantity = int(input('Update Item Quantity: '))
                total_price = price * quantity

                # Update item in database
                sql = '''
                    UPDATE item
                    SET item_name = %s, price = %s, quantity = %s, total_price = %s
                    WHERE serial_no = %s
                '''
                val = (item_name, price, quantity, total_price, serial_no)

                mycursor.execute(sql, val)
                mydb.commit()
                
                print('\nInvoice Updated Successfully\n')
                input('Press Enter to continue...')
            elif choice == 2:
                print('\nExit Successfully\n')
                break
            else:
                print('\nEnter valid choice...\n')
    except ValueError:
        print('****************************************************************')
        print('\n\t>>>Error : You are enter  Worng Value so comes valuerror\n\n')
        print('****************************************************************') 
        input('Press Enter to continue...')
def customer_billing():
    while True:
        print ('''
            =============== Billing Invoice ============
            1. Create Invoice : 
            2. View Invoice :
            3. Update Invoice :
            4. Exit
            ''')
        print('********************************')
        ch=int(input('Enter Your Choice : '))
       
        if ch==1:
            item_billing()
        elif ch==2:
            view_invoice()
            
        elif ch==3:
            update_invoice()
            
        elif ch==4:
            print('\nExit Successfully\n')
            break
        else:
            print('\nEnter valid choice...\n')
customer_billing()