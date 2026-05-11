try:
    #n+=10
    a=int(input("Enter number: "))
    #l=[1,2,3,4,5,6]
    #print(l[10])
    #k={1:1,2:4,3:9,4:16}
    #print(k[9])
    #c=12/0
    #m=10+'a'
except (NameError,ValueError,IndexError,KeyError,ZeroDivisionError,TypeError) as e:
    print(f"Error occured: {e}")
else:
    print("No Error")
finally:
    print('End')
