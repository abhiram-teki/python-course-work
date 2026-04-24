status=input("Enter status: ")
if status=='face':
    print('Unlock phone')
else:
    print("Unable to unlock, use password.")
    if status=='password':
        print("Phone unlocked.")
    else:
        print("Incorrect password, try again.")
    
