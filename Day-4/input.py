Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name= input()
abhi
name
'abhi'
t1=input("Enter first number")
Enter first number5
t1
'5'
t2= int(input("Enter age: "))
Enter age: 22
t2
22
p= float(input("Enter score: "))
Enter score: 7.7
p
7.7
'1 2 3 4'.split()
['1', '2', '3', '4']
lang= input("Enter names: ").split()
Enter names: abhiram mark nolan oliver
lang
['abhiram', 'mark', 'nolan', 'oliver']
numbers = list(map(int,input("Enter numbers: ").split()))
Enter numbers: 1 2 3 4 5 6
numbers
[1, 2, 3, 4, 5, 6]
p= eval(input("Enter the list: "))
Enter the list: [1, 2, 3, 4, 5]
p
[1, 2, 3, 4, 5]
input("Enter something idk: ").split(',')
Enter something idk: 1,2,3,4,5
['1', '2', '3', '4', '5']
q= input("Enter something idk: ").split(',')

Enter something idk: 1,2,3,4,5
q
['1', '2', '3', '4', '5']
r= int(input("Enter something idk: ").split(','))
Enter something idk: 1,3,5,7
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    r= int(input("Enter something idk: ").split(','))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
r= map(int, input("Enter numbers: ").split())
Enter numbers: 1 3 5 7 9
r
<map object at 0x00000260D0A0FBC0>
print(r)
<map object at 0x00000260D0A0FBC0>
r
<map object at 0x00000260D0A0FBC0>
s=map(float, input("Enter the prices: ").split())
Enter the prices: 89.99 29.99 67.67
s
<map object at 0x00000260D0A1AD00>
p,q,r = s=map(float, input("Enter the prices: ").split())

Enter the prices: 12.5 10.5 39.9
p
12.5
q
10.5
r
39.9
p,q,r=map(float, input("Enter the prices: ").split())
Enter the prices: 55.5 22.6 88.99
p
55.5
q
22.6
r
88.99
r= list(map(int, input("Enter numbers: ").split()))
Enter numbers: 1 2 3 4 5 6
r
[1, 2, 3, 4, 5, 6]
brands = input("What brands: ").split()
What brands: Truthear KZ FiiO
brands
['Truthear', 'KZ', 'FiiO']
r= set(map(int, input("Enter numbers: ").split()))
Enter numbers: 2 4 6 8

r
{8, 2, 4, 6}
a=eval(input("What is your name: "))
What is your name: "Abhiram"
a
'Abhiram'
a=eval(input("What is your rank: "))
What is your rank: 2
a
2
d=eval(input("something:" ))
something:{1:1, 2:2}
>>> d
{1: 1, 2: 2}
>>> type(d)
<class 'dict'>
>>> boo = eval(input("Yay or nay: "))
Yay or nay: True
>>> boo
True
>>> a,b,c = 10, 10.3, 'Python'
>>> a
10
>>> b
10.3
>>> c
'Python'
>>> print("a is ",a,"b is ",b,"c is ",c)
a is  10 b is  10.3 c is  Python
>>> print("a is",a,"b is",b,"c is",c)
a is 10 b is 10.3 c is Python
>>> print("a is",a,"b is",b,"c is",c,sep='')
a is10b is10.3c isPython
>>> print("a is",a,"b is",b,"c is",c,sep='@')
a is@10@b is@10.3@c is@Python
>>> print("a is",a,"b is",b,"c is",c,sep='@',end='\n')
a is@10@b is@10.3@c is@Python
>>> print(f'a={a} b={b} c={c}')
a=10 b=10.3 c=Python
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=10.300000 c=Python
>>> print('a={} b={} c={}'format(a,b,c))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('a={} b={} c={}',format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print('a={} b={} c={}',format(a,b,c))
TypeError: format expected at most 2 arguments, got 3
>>> print('a={} b={} c={}'.
...       format(a,b,c))
a=10 b=10.3 c=Python
>>> print(f'I program in c={c}')
I program in c=Python
>>> print(f'I program in {c}')
I program in Python
>>> print(f'This costs {b}')
This costs 10.3
