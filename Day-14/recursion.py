'''
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)

display(1)
'''
'''
def display(n):
    if n>10:
        return
    
    display(n+1)
    print(n)

display(1)
'''
'''
def display(n,sum):
    if n>10:
        return sum
    return sum+display(n+1,sum+n)
print(display(1,0))
'''
'''
def display(n,prod):
    if n>10:
        return prod
    return prod+display(n+1,prod*n)
print(display(1,1))
'''
'''
def display(i,s):
    if i==len(s):
        return
    print(s[i])
    display(i+1,s)
    
s='Python Program'
display(0,s)
'''
'''
def display(i,s):
    if i==len(s):
        return
    
    display(i+1,s)
    print(s[:i+1])
    
    
s='Python Program'
display(0,s)
'''
'''
def display(i):
    if i==len(s):
        return
    
    print(s[i:i+4])
    display(i+1)
      
s='Python Program'
display(0)
'''

def display(i):
    if i==1:
         return 1
    return i*display(i-1)
print(display(4))

