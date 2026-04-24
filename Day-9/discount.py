prod={1:{'name':'bread','discount':10},
      2:{'name':'sugar','discount':0},
      3:{'name':'jam','discount':5},
      4:{'name':'butter','discount':0}}
print(prod)
index=int(input("Enter index: "))
if prod[index]['discount']:
    print(f'{prod[index]["name"]} has a discount.')
