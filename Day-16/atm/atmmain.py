from atmlogic import *

e_num=int(input("Enter your account number: "))
e_pin=int(input("Enter pin: "))

if login(e_num,e_pin):
    print("Welcome to the ATM")

    while True:
        print("[C]heck balance")
        print("[D]eposit")
        print("[W]ithdraw")
        print("[V]iew Transactions")
        print("[E]xit")
        ch = input("Enter choice: ").upper()
        if ch=='C':
            check_balance()
        elif ch=='D':
            deposit()
        elif ch=='W':
            withdraw()
        elif ch=='V':
            viewtransaction()
        elif ch=='E':
            print("Thanks")
            break
        else:
            print("Enter valid input")
            
