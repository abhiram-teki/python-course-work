Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> for i in range(3):
...     print('*')
... 
...     
*
*
*
>>> for i in range(3):
...     print('*', end=' ')
... 
...     
* * * 
>>> for j in range(5):
...     print(end=' ')
...     for i in range(3):
...         print('*')
... 
...         
 *
*
*
 *
*
*
 *
*
*
 *
*
*
 *
*
*
>>> for j in range(5):
...     for i in range(3):
...         print('*')
