Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=()
type(t)
<class 'tuple'>
t=tuple()
type(t)
<class 'tuple'>
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=(1,2,3.5,'str',[1,2,3], {1,2,3}, (1,2,3), {"four":4},False)
t
(1, 2, 3.5, 'str', [1, 2, 3], {1, 2, 3}, (1, 2, 3), {'four': 4}, False)
a=(1,2,3)
b=(4,5,6)
a+b
(1, 2, 3, 4, 5, 6)
t[2]
3.5
t[:4]
(1, 2, 3.5, 'str')
t[::-3]
(False, {1, 2, 3}, 3.5)
t[-1]
False
t[-3::]
((1, 2, 3), {'four': 4}, False)
'str' in t
True
len(t)
9
t2=(1,2,3,4,5,6,7,8)
max(t2)
8
min(t2)
1
>>> sorted(t2)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> tuple(sorted(t2))
(1, 2, 3, 4, 5, 6, 7, 8)
>>> count(t2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    count(t2)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> t2.count()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    t2.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> t2.count(2)
1
>>> a,b,c,d,e,f,g,h=t2
>>> a
1
>>> b
2
>>> c
3
>>> d
4
>>> t2.index(5)
4
>>> t3=(1,2,3,[5,6])
>>> t3
(1, 2, 3, [5, 6])
>>> t3.append(7)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t3.append(7)
AttributeError: 'tuple' object has no attribute 'append'
>>> t3[3].append(7)
>>> t3
(1, 2, 3, [5, 6, 7])
>>> t3[3][0].append(4)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    t3[3][0].append(4)
AttributeError: 'int' object has no attribute 'append'
>>> t3[3].insert(0,4)
>>> t3
(1, 2, 3, [4, 5, 6, 7])
