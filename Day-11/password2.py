p=input("Enter password: ")

if len(p)>=8:
    status=set()
    for i in p:
        if i.isupper():
            status.add('u')
        elif i.islower():
            status.add('l')
        elif i.isdigit():
            status.add('d')
        else:
            status.add('s')
    if len(status)==4:
        print("Strong Password.")
    else:
        print("Weak Password.")
else:
    print("Needs to be more than eight characters.")
