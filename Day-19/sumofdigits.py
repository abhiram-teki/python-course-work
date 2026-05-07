def sod(s):
    if s==0:
        return 0
    return s%10+sod(s//10)

s=int(input('Enter num: '))
print(sod(s))
