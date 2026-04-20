Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[]
l=list()
type(l)
<class 'list'>
l=[1,'2',3.5,[5],(6),{7},{'eight':8}]
l
[1, '2', 3.5, [5], 6, {7}, {'eight': 8}]
a=[1,2,3]
b=[4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
names=['Mark','Nolan','Oliver','Debbie','Paul','Thragg','Thaedus']
names[0]
'Mark'
names[4]
'Paul'
names[-1]
'Thaedus'
names[1:3]
['Nolan', 'Oliver']
names[::3]
['Mark', 'Debbie', 'Thaedus']
names[::4]
['Mark', 'Paul']
'Kregg' in names
False
'Thragg' not in names
False
'Nolan' in names
True
names[::-1]
['Thaedus', 'Thragg', 'Paul', 'Debbie', 'Oliver', 'Nolan', 'Mark']
names[::-3]
['Thaedus', 'Debbie', 'Mark']
len(names)
7
sorted(names)
['Debbie', 'Mark', 'Nolan', 'Oliver', 'Paul', 'Thaedus', 'Thragg']
names[0]='Conquest'
names
['Conquest', 'Nolan', 'Oliver', 'Debbie', 'Paul', 'Thragg', 'Thaedus']
id(names)
1852804394944
names.append('Anissa')
names
['Conquest', 'Nolan', 'Oliver', 'Debbie', 'Paul', 'Thragg', 'Thaedus', 'Anissa']
names.insert(-2,'Argall')
names
['Conquest', 'Nolan', 'Oliver', 'Debbie', 'Paul', 'Thragg', 'Argall', 'Thaedus', 'Anissa']
names.extend('Thula','Lucan','Robot')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    names.extend('Thula','Lucan','Robot')
TypeError: list.extend() takes exactly one argument (3 given)
names.extend(['Thula','Lucan','Robot'])
names
['Conquest', 'Nolan', 'Oliver', 'Debbie', 'Paul', 'Thragg', 'Argall', 'Thaedus', 'Anissa', 'Thula', 'Lucan', 'Robot']

names.pop()
Traceback (most recent call last):
  File "C:/Users/Abhiram Teki/Desktop/cdg_stuff/test.py", line 2, in <module>
    n= int(input("Enter number of names you would like to enter: "))
ValueError: invalid literal for int() with base 10: 'names.pop()'
names=
['Conquest', 'Nolan', 'Oliver', 'Debbie', 'Paul', 'Thragg', 'Argall', 'Thaedus', 'Anissa', 'Thula', 'Lucan', 'Robot']
SyntaxError: invalid syntax
names = ['Conquest', 'Nolan', 'Oliver', 'Debbie', 'Paul', 'Thragg', 'Argall', 'Thaedus', 'Anissa', 'Thula', 'Lucan', 'Robot']
names.pop()
'Robot'
names.pop(2)
'Oliver'
names.remove('Debbie')
names
['Conquest', 'Nolan', 'Paul', 'Thragg', 'Argall', 'Thaedus', 'Anissa', 'Thula', 'Lucan']
del names[2]
names
['Conquest', 'Nolan', 'Thragg', 'Argall', 'Thaedus', 'Anissa', 'Thula', 'Lucan']
names.clear()
names
[]
names.index('Argall')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    names.index('Argall')
ValueError: list.index(x): x not in list
names=['Conquest', 'Nolan', 'Thragg', 'Argall', 'Thaedus', 'Anissa', 'Thula', 'Lucan']

names.index['Argall']
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    names.index['Argall']
TypeError: 'builtin_function_or_method' object is not subscriptable
names
['Conquest', 'Nolan', 'Thragg', 'Argall', 'Thaedus', 'Anissa', 'Thula', 'Lucan']
names.index['Lucan']
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    names.index['Lucan']
TypeError: 'builtin_function_or_method' object is not subscriptable
names.index[3]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    names.index[3]
TypeError: 'builtin_function_or_method' object is not subscriptable
names2=['abc','def']
names('Lucan')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    names('Lucan')
TypeError: 'list' object is not callable
>>> names.index('Lucan')
7
>>> l=[1,2,3,3,3,3,4,4,4,4,5]
>>> l.count(3)
4
>>> sorted(l)
[1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5]
>>> l.sort()
>>> l
[1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5]
>>> l.sort(reverse=True)
>>> l
[5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 1]
>>> l.reverse()
>>> l
[1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5]
>>> a=[1,2,3,4]
>>> a=b
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a=b
NameError: name 'b' is not defined
>>> b=a
>>> b
[1, 2, 3, 4]
>>> b.append(5)
>>> b
[1, 2, 3, 4, 5]
>>> a
[1, 2, 3, 4, 5]
>>> c=a.copy()
>>> c
[1, 2, 3, 4, 5]
>>> c.append(6)
>>> a
[1, 2, 3, 4, 5]
>>> c
[1, 2, 3, 4, 5, 6]
>>> id(a)
2223923064640
>>> id(c)
2223968117120
