Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1 = "Hello"
s2="World"
print(s1, s2)
Hello World
sen= s1+""+s2
print(sen)
HelloWorld
sen= s1+" "+s2

print(sen)
Hello World
print("HELLO!" * 3)
HELLO!HELLO!HELLO!
text = "Python"
print(text[0])
P
print(text[-1])
n
print(text[0:3])
Pyt
print(text[2:])
thon
'Pyt' in text
True
'hon' in text
True
'Java' not in text
True
>>> len(s1)
5
>>> sorted("The quick brown fox leaps over the lazy dog")
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', 'a', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'e', 'f', 'g', 'h', 'h', 'i', 'k', 'l', 'l', 'n', 'o', 'o', 'o', 'o', 'p', 'q', 'r', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> tuple(sorted("the quick brown fox leaps over the lazy dog"))
(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'a', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'e', 'f', 'g', 'h', 'h', 'i', 'k', 'l', 'l', 'n', 'o', 'o', 'o', 'o', 'p', 'q', 'r', 'r', 's', 't', 't', 'u', 'v', 'w', 'x', 'y', 'z')
>>> print(set(sorted("the quick brown fox leaps over the lazy dog")))
{'k', 'a', 'c', 'y', 'r', 'z', ' ', 'e', 'd', 'x', 't', 'h', 'n', 'b', 'f', 'q', 'p', 'l', 'u', 'o', 'i', 'w', 's', 'v', 'g'}
>>> upper(text)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    upper(text)
NameError: name 'upper' is not defined. Did you mean: 'super'?
>>> text.upper()
'PYTHON'
>>> text.lower()
'python'
>>> text.title()
'Python'
>>> text.swapcase()
'pYTHON'
>>> text.startswith("Py")
True
>>> text.endswith("on")
True
>>> text.istitle()
True
>>> "".isspace()
False
>>> " ".isspace()
True
>>> text.replace('P','B')
'Bython'
>>> print(text)
Python
>>> "a,b,c".split(',')
['a', 'b', 'c']
>>> "a,b,c".rsplit(',',1)
['a,b', 'c']
>>> "a,b,c".split(',',2)
['a', 'b', 'c']
