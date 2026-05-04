def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
           return False
    return True

num=int(input('Enter number: '))
print('Prime' if isPrime(num) else 'Composite')
