Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=5
>>> a
5
>>> a=5.5
>>> a
5.5
>>> type(a)
<class 'float'>
>>> str(a)
'5.5'
>>> print(a)
5.5
>>> b=3.2
>>> b
3.2
>>> int(b)
3
>>> l="10"
>>> str(l)
'10'
>>> l
'10'
>>> p="python1"
>>> int(p)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int(p)
ValueError: invalid literal for int() with base 10: 'python1'
>>> s="python"
>>> list(s)
['p', 'y', 't', 'h', 'o', 'n']
>>> tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
>>> set(s)
{'t', 'h', 'y', 'p', 'n', 'o'}
>>> l=[1,2,3]
>>> int(l)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> d={"Name":"Bob", "Age":"32"}
>>> d
{'Name': 'Bob', 'Age': '32'}
str(d)
"{'Name': 'Bob', 'Age': '32'}"
list(d)
['Name', 'Age']

tuple(d)
('Name', 'Age')
set(d)
{'Age', 'Name'}
bool(d)
True
b=True
int(b)
1
float(b)
1.0
complex(b)
(1+0j)
str(b)
'True'
set={1,2,3}
int(set)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(set)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
str(set)
'{1, 2, 3}'
tuple(set)
(1, 2, 3)
bool(set)
True
list(set)
[1, 2, 3]
tu=(1,2,3)
str(tu)
'(1, 2, 3)'
list(tu)
[1, 2, 3]
set(tu)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    set(tu)
TypeError: 'set' object is not callable
set(tu)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    set(tu)
TypeError: 'set' object is not callable
t1=(1,2,3)
set(t1)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    set(t1)
TypeError: 'set' object is not callable
s1="Batman"
int(s1)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    int(s1)
ValueError: invalid literal for int() with base 10: 'Batman'
s2="100"
s3=100
int(s3)
100
str(s3)
'100'
int(s2)
100
s='12','14'
list(s)
['12', '14']
s
('12', '14')
set1={"name":"Rob", "Age":23}
set1
{'name': 'Rob', 'Age': 23}
