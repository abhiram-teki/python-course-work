Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=set()
s={1,2,3,4,5}
s
{1, 2, 3, 4, 5}
s.add(6)
s
{1, 2, 3, 4, 5, 6}
s.add(7)
s
{1, 2, 3, 4, 5, 6, 7}
s.add(10)
s.add(8)
s
{1, 2, 3, 4, 5, 6, 7, 8, 10}
b={1,3,5,7}
a.union(b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.union(b)
NameError: name 'a' is not defined
s.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 10}
s.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
s.isdisjoint(b)
False
c={11,12}
a.isdisjoint(c)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.isdisjoint(c)
NameError: name 'a' is not defined
s.isdisjoint(c)
True
c.add('this is a set')
c
{11, 12, 'this is a set'}
c.add(6.7)
c
{11, 12, 'this is a set', 6.7}
11 in c
True
13 in c
False
>>> for i in c:
...     print(i)
... 
11
12
this is a set
6.7
>>> s.intersection(b)
{1, 3, 5, 7}
>>> s&b
{1, 3, 5, 7}
>>> s-b
{2, 4, 6, 8, 10}
>>> {1}<a
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    {1}<a
NameError: name 'a' is not defined
>>> {1}<s
True
>>> {9,10}<s
False
>>> {8,10}<s
True
>>> a>{1,2,4}
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a>{1,2,4}
NameError: name 'a' is not defined
>>> s>{1,2,4}
True
>>> b>{11,6.7}
False
>>> c>{11,6.7}
True
>>> a.update({11,12,13})
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.update({11,12,13})
NameError: name 'a' is not defined
>>> s.update({11,12,13})
>>> s
{1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13}
>>> s.add(9)
>>> s
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
