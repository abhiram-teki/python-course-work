def fib(n):
    if n<1:
        return
    elif n==1:
        print(0)
    elif n>=2:
        a,b=0,1
        print(a,b,end=' ')
        for i in range(n-2):
            c=a+b
            print(c,end=' ')
            a,b=b,c

n=int(input("Enter number: "))
fib(n)        
