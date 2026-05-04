'''
def iseven(n):
    if n%2==0:
        print('Even')
    else:
        print('Odd')

iseven(12)
iseven(13)
'''
def iseven(n):
    if n%2==0:
        return 'Even'
    else:
        return 'Odd'
    
print(iseven(6))
