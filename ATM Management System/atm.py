from register import register
from balance import balance
from credit import credit
from greenpin import greenpin
from updatePin import update

def atm():
    while True:
        print('''
            ================= Welcome to ATM ================
            1. Receive ATM Card Number
            2. Create ATM Pin
            3. Balance Enquiry
            4. Cash Withdrawal
            5. Change Pin Number
            6. Exit
            ''')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            register()
        elif choice == 2:
            greenpin()
        elif choice == 3:
            balance()
        elif choice == 4:
            credit()
        elif choice == 5:
            update()
        elif choice == 6:
            print("Exit Successfully")
            print("Thank you")
            break
            
        else:
            print("Invalid Choice")
            atm()
atm()