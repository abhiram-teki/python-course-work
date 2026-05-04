data={12345:{'pin':1234,'balance':5000,'history':[]},
      23456:{'pin':1234,'balance':5000,'history':[]},
      34567:{'pin':1234,'balance':5000,'history':[]},
      45678:{'pin':1234,'balance':5000,'history':[]}
    }
def login(e_num,e_pin):
    if e_num in data and data[e_num]['pin']==e_pin:
        global acc_num
        acc_num=e_num
        print("Login Succesful")
        return True
    else:
        print('Login Unsuccesful')
        return False
    
def check_balance():
    print("Current balance is: ",data[acc_num]['balance'])
    
def deposit():
    amt=int(input("Enter deposit amount: "))
    data[acc_num]['balance']+=amt
    data[acc_num]['history'].append(f'+ {amt} was deposited.')
    print(f'{amt} was deposited.')

def withdraw():
    amt=int(input("Enter deposit amount: "))
    if amt<=data[acc_num]['balance']:
        data[acc_num]['balance']-=amt
        data[acc_num]['history'].append(f'- {amt} was withdrawn.')
        print(f'{amt} was withdrawn.')

    else:
        print('Insufficient Balance')
        
def viewtransaction():
    if data[acc_num]['history']:
        print('++++++++Transaction History++++++++')
        for i in data[acc_num]['history']:
                print(i)
        print("+++++++++++++++++++++++++++++++++++")
    else:
        print("No transactions.")
    
