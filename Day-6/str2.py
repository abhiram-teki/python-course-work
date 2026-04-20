Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="the quick brown fox leaps over the lazy dog"
s
'the quick brown fox leaps over the lazy dog'
sorted(s)
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'a', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'e', 'f', 'g', 'h', 'h', 'i', 'k', 'l', 'l', 'n', 'o', 'o', 'o', 'o', 'p', 'q', 'r', 'r', 's', 't', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(set(s))
{'l', 'c', 'v', 'r', 'a', 'p', 'f', 'i', 'n', 't', 'e', 'w', 'd', 's', 'u', 'o', ' ', 'k', 'y', 'b', 'x', 'q', 'z', 'g', 'h'}
print(sorted(set(s)))
[' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n.startswith(the quick)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
n.startswith('the quick'
             )
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    n.startswith('the quick'
NameError: name 'n' is not defined
s.startswith(the quick)
                 
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.startswith('the quick'
             )
                 
True
s.endswith('lazy dog')
                 
True
isalpha(s)
                 
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    isalpha(s)
NameError: name 'isalpha' is not defined
s.isalpha()
                 
False
num="12345"
                 
num.isalnum()
                 
True
'lol'.islower()
                 
True
'LOL'.isupper()
                 
True
"LOL 123".isupper()
                 
True
'Codegnan'.istitle()
                 
True
s1="bruh'
                 
SyntaxError: unterminated string literal (detected at line 1)
s1="bruh"
                 
'Python Program'.istitle()
...                  
True
>>> 'Python program'.istitle()
...                  
False
>>> '五'.isnumeric()
...                  
True
>>> 'VIII'.isnumeric()
...                  
False
>>> '123'.isnumeric()
...                  
True
>>> '123'.isdigit()
...                  
True
>>> '123'.isdecimal()
...                  
True
>>> '٣'.isnumeric()
...                  
True
>>> '٣'.isdigit()
...                  
True
>>> '٣'.isdecimal()
...                  
True
>>> '1a3'.isnumeric()
...                  
False
>>> '12.3'.isdecimal()
...                  
False
>>> n2= 12.3
...                  
>>> n2.isdecimal()
...                  
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    n2.isdecimal()
AttributeError: 'float' object has no attribute 'isdecimal'
>>> ' '.isspace()
...                  
True
