Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

s='python'
for i in s
SyntaxError: expected ':'
for i in s:
    print(i)

   
p
y
t
h
o
n
l=[1,2,3,4,5,6]
for i in l:
    print(i)

    
1
2
3
4
5
6
t=(1,2,3,4,5)
for i in t:
    print(i)

    
1
2
3
4
5
s={1,2,3,4}
for i in s:
    print(o)

    
Traceback (most recent call last):
  File "<pyshell#17>", line 2, in <module>
    print(o)
NameError: name 'o' is not defined
for i in s:
    print(i)

    
1
2
3
4
d={1:'one',2:'two',3:'three'}
d
{1: 'one', 2: 'two', 3: 'three'}
for i in d:
    print(i)

    
1
2
3
for i in d:
    print(i,d[i])

    
1 one
2 two
3 three
for i in d:
    print(f'{i}is the key and {d[i]} is the value')

    
1is the key and one is the value
2is the key and two is the value
3is the key and three is the value
for i in range(0,10,1):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
for i in range(2,11,2)
SyntaxError: expected ':'
for i in range(2,11,2):
    print(i)

    
2
4
6
8
10
for i in range(5,51,5):
    print(i)

    
5
10
15
20
25
30
35
40
45
50
for i in range(10,0,-1):
    print(i)

    
10
9
8
7
6
5
4
3
2
1
for i in range(30,19,-1)
SyntaxError: expected ':'
for i in range(30,19,-2):
    print(i)

    
30
28
26
24
22
20
for i in range(1,11,3):
    print(i)

    
1
4
7
10
for i in range(0,11,3):
    print(i)

    
0
3
6
9
nums=[1,2,3,3,4,5,5]
set(nums)
{1, 2, 3, 4, 5}
s='python'
s[0]
'p'
for i in s:
    print(s[i])

    
Traceback (most recent call last):
  File "<pyshell#59>", line 2, in <module>
    print(s[i])
TypeError: string indices must be integers, not 'str'
for i in s:
    print(i)

    
p
y
t
h
o
n
enumerate(s)
<enumerate object at 0x0000017E14D01A30>
for i in enumerate(s):
    print(i)

    
(0, 'p')
(1, 'y')
(2, 't')
(3, 'h')
(4, 'o')
(5, 'n')
for i in range(len(s)):
    print(s[i])

    
p
y
t
h
o
n
for i in range(len(s)):
    enumerate(i)
    print(i)

    
Traceback (most recent call last):
  File "<pyshell#73>", line 2, in <module>
    enumerate(i)
TypeError: 'int' object is not iterable
for i in range(len(s)):
    print(i,s[i])

    
0 p
1 y
2 t
3 h
4 o
5 n
names=['mark', 'nolan', 'oliver', 'thaedus']
for i in enumerate(names)
SyntaxError: expected ':'
for i in enumerate(names):
    print(i[0], i[1])

    
0 mark
1 nolan
2 oliver
3 thaedus
for i in range(len(names)):
    print(f'{s[i]}')

    
p
y
t
h
for i in range(len(names)):
    print(i,names[i])

    
0 mark
1 nolan
2 oliver
3 thaedus
set={1,2,3,4}
for i in range(len(set))
SyntaxError: expected ':'
for i in range(len(set)):
    print(set[i])

    
Traceback (most recent call last):
  File "<pyshell#92>", line 2, in <module>
    print(set[i])
TypeError: 'set' object is not subscriptable
for i in enumerate(set):
    print(i[0],i[1])

    
0 1
1 2
2 3
3 4
for i in enumerate(set):
    print(i[0],i[1],d[i[1]])

    
0 1 one
1 2 two
2 3 three
Traceback (most recent call last):
  File "<pyshell#98>", line 2, in <module>
    print(i[0],i[1],d[i[1]])
KeyError: 4
for i in enumerate(set):
    print(i[0],i[1],set[i[1]])

    
Traceback (most recent call last):
  File "<pyshell#100>", line 2, in <module>
    print(i[0],i[1],set[i[1]])
TypeError: 'set' object is not subscriptable
>>> p=set()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    p=set()
TypeError: 'set' object is not callable
>>> p={1,2,3,4,5}
>>> p
{1, 2, 3, 4, 5}
>>> for i in enumerate(p):
...     print(i[0],i[1],p[i[1]])
... 
...     
Traceback (most recent call last):
  File "<pyshell#105>", line 2, in <module>
    print(i[0],i[1],p[i[1]])
TypeError: 'set' object is not subscriptable
>>> 
>>> p={1:1,2:4,3:9}
>>> for i in enumerate(p):
...     print(i[0],i[1],p[i[1]])
... 
0 1 1
1 2 4
2 3 9
>>> for i in range(10):
...     print(i)
...         break
...     
SyntaxError: unexpected indent
>>> for i in range(10):
...     if i==5:
...         break
...     print(i)
... 
...     
0
1
2
3
4
>>> for i in range(10):
...     pass
... 
