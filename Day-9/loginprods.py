prod={1:{'name':'bread','stock':10},
      2:{'name':'sugar','stock':0},
      3:{'name':'jam','stock':5},
      4:{'name':'butter','stock':0}}
login_status=True
print(prod)
index=int(input("Enter index: "))
if login_status:
    if prod[index]['stock']:
        print(f'{prod[index]['name']} is ordered.')
    else:
        print(f'{prod[index]['name']} is out of stock.')
else:
    print('Please login.')
