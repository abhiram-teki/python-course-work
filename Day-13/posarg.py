'''
def disp(name,email,password):
    print('Name: ',name)
    print('Email: ',email)
    print('Password: ',password)

disp('user', 'email@gmail.com', 'pwd123')
disp('email@gmail.com','pwd@123','user2')
'''
'''
def disp(name,email,password):
    print('Name: ',name)
    print('Email: ',email)
    print('Password: ',password)

disp(name='user', email='email@gmail.com', password='pwd123')
disp(email='email@gmail.com',password='pwd@123',name='user2')
'''
def disp(name,email,password,phone=None):
    print('Name: ',name)
    print('Email: ',email)
    print('Password: ',password)
    print('Phone: ', phone)

disp(name='user', email='email@gmail.com', password='pwd123')
disp(email='email@gmail.com',password='pwd@123',name='user2',phone='123456789')
