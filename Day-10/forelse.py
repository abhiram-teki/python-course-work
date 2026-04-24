prod=['a','b','c','d']
a=input("what prod?")
for i in prod:
    if i==a:
        print(i)
        break
else:
    print('Prod not found')
