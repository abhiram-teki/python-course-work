'''
n=int(input("Enter n: "))
for row in range(n):
    for col in range(row+1):
        print('*',end=' ')
    print()
'''
'''
n=int(input("Enter n: "))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()
'''

'''
n=int(input('Enter n: '))
m=n//2
for row in range(n):
    if row<=m:
        for col in range(row+1):
            print('*',end=' ')
    else:
        for col in range(n-row):
            print('*', end=' ')
    print()
'''
'''
n=int(input("Enter n: "))
for row in range(n):
    for spc in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print('*', end=' ')
    print()
'''
'''
n=int(input("Enter n: "))
for row in range(n):
    for spc in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*', end=' ')
    print()
'''
'''
n=int(input('Enter n: '))
m=n//2
for row in range(n):
    if row<=m:
        for spc in range(m-row):
            print(' ',end=' ')
        for col in range(row+1):
            print('*',end=' ')
    else:
        for spc in range(row-m):
            print(' ',end=' ')
        for col in range(n-row):
            print('*', end=' ')
    print()
'''
'''
n=int(input('Enter n: '))
m=n//2
for row in range(n):
    if row<=m:
        print(' '*(m-row)+'*'*(row+1),end=' ')
    else:
        print(' '*(row-m)+'*'*(n-row),end=' ')
    print()
'''
'''
n=int(input("Enter n: "))
for row in range(n):
    for col in range(n):
        print(int((row+col)%2==0),end=' ')
    print()
'''
'''
n=int(input("Enter n: "))
for row in range(n):
    for col in range(n):
        print(int(col%2==0),end=' ')
    print()
'''
'''
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if j==0 or j==(n-1) or i==0 or i==(n-1):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==(n-1) or i+j==(n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==j or i+j==(n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==(n-1) or j==0 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i==n-1 and j<=(n//2)) or(j==n//2 and i>=n//2)or(i==n//2 and j>=n//2)or(j==n-1 and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

        
