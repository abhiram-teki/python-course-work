products={
    1:{'name':'Rice','price':60},
    2:{'name':'Wheat Flour','price':50},
    3:{'name':'Sugar','price':50},
    4:{'name':'Milk','price':30},
    5:{'name':'Eggs','price':80},
    6:{'name':'Cooking Oil','price':160},
    7:{'name':'Tea Powder','price':90},
    8:{'name':'Salt','price':20},
    9:{'name':'Bread','price':40},
    10:{'name':'Soap','price':25},
}

print('------ Welcome to Grocery Store ------')
print('Here are the available products:')

print('Index'.ljust(5,' '),'Product'.ljust(20,' '),'Price (Rs.)')

for i in products:
    print(str(i).ljust(5,' '),products[i]['name'].ljust(20,' '),products[i]['price'])

print('Enter the product indexes you want to buy (you can repeat indexes)')
selected = list(map(int,input('Enter indexes (e.g. 1 2 2 5): ').split()))

total=0
s=set()
print('Product'.ljust(20,' '),'Qty'.ljust(5,' '),'Price'.ljust(5,' '),'Total')

for i in selected:
    if i not in s:
        print(products[i]['name'].ljust(20,' '),str(selected.count(i)).ljust(5,' '),str(products[i]['price']).ljust(5,' '),selected.count(i)*products[i]['price'])
        total+=products[i]['price']*selected.count(i)
        s.add(i)

print('Total Amount to Pay:',total)
print('Thank you for shopping with us!')
