pin=12345
for i in range(5):
    epin=int(input("Enter: "))
    if pin==epin:
        print("Cool")
        break
    else:
        print("Wrong")
else:
    print("Try again later")
