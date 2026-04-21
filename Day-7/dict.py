Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d=dict()
type(d)
<class 'dict'>
d={'Name':'Abhiram','Course':'PFS','Batch':52,'Skills':['Python','HTML','CSS']}
d
{'Name': 'Abhiram', 'Course': 'PFS', 'Batch': 52, 'Skills': ['Python', 'HTML', 'CSS']}
d['C_Type']= 'Offline'
d
{'Name': 'Abhiram', 'Course': 'PFS', 'Batch': 52, 'Skills': ['Python', 'HTML', 'CSS'], 'C_Type': 'Offline'}
s=dict()
s['1']:'one'
s
{}
s[1]='one'
s
{1: 'one'}
s[2.5]='two'
s
{1: 'one', 2.5: 'two'}
s[(3,4,5)]:'three'
s
{1: 'one', 2.5: 'two'}
s[(3,4,5)]='three'
s
{1: 'one', 2.5: 'two', (3, 4, 5): 'three'}
s[True]='four'
s
{1: 'four', 2.5: 'two', (3, 4, 5): 'three'}
s[True]='one'
s
{1: 'one', 2.5: 'two', (3, 4, 5): 'three'}
s[False]='four'
s
{1: 'one', 2.5: 'two', (3, 4, 5): 'three', False: 'four'}
s[6+7j]='five'
s
{1: 'one', 2.5: 'two', (3, 4, 5): 'three', False: 'four', (6+7j): 'five'}
'Name' in d
True
'Skills' in d
True
d['Skills']
['Python', 'HTML', 'CSS']
d.get('age')
d.get('Batch')
52
d.get('age','age is not in')
'age is not in'
d['Time Start']=200
d
{'Name': 'Abhiram', 'Course': 'PFS', 'Batch': 52, 'Skills': ['Python', 'HTML', 'CSS'], 'C_Type': 'Offline', 'Time Start': 200}
d['Time Start']=900
d.update(['Time End': 1800,'Travel':1])
SyntaxError: invalid syntax
d.update('Time End':1800,'Travel':1)
SyntaxError: invalid syntax
d.update(['Time End':1800,'Travel':1])
SyntaxError: invalid syntax
d.update({'Time End':1800,'Travel':1})
d
{'Name': 'Abhiram', 'Course': 'PFS', 'Batch': 52, 'Skills': ['Python', 'HTML', 'CSS'], 'C_Type': 'Offline', 'Time Start': 900, 'Time End': 1800, 'Travel': 1}
d.popitem()
('Travel', 1)
d
{'Name': 'Abhiram', 'Course': 'PFS', 'Batch': 52, 'Skills': ['Python', 'HTML', 'CSS'], 'C_Type': 'Offline', 'Time Start': 900, 'Time End': 1800}
>>> d.pop(C_Type)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    d.pop(C_Type)
NameError: name 'C_Type' is not defined
>>> d.pop('C_Type')
'Offline'
>>> d
{'Name': 'Abhiram', 'Course': 'PFS', 'Batch': 52, 'Skills': ['Python', 'HTML', 'CSS'], 'Time Start': 900, 'Time End': 1800}
>>> d.clear()
>>> d
{}
>>> d={'Name': 'Abhiram', 'Course': 'PFS', 'Batch': 52, 'Skills': ['Python', 'HTML', 'CSS'], 'C_Type': 'Offline', 'Time Start': 900, 'Time End': 1800, 'Travel': 1}
>>> d
{'Name': 'Abhiram', 'Course': 'PFS', 'Batch': 52, 'Skills': ['Python', 'HTML', 'CSS'], 'C_Type': 'Offline', 'Time Start': 900, 'Time End': 1800, 'Travel': 1}
>>> d.keys()
dict_keys(['Name', 'Course', 'Batch', 'Skills', 'C_Type', 'Time Start', 'Time End', 'Travel'])
>>> d.values()
dict_values(['Abhiram', 'PFS', 52, ['Python', 'HTML', 'CSS'], 'Offline', 900, 1800, 1])
>>> d.items()
dict_items([('Name', 'Abhiram'), ('Course', 'PFS'), ('Batch', 52), ('Skills', ['Python', 'HTML', 'CSS']), ('C_Type', 'Offline'), ('Time Start', 900), ('Time End', 1800), ('Travel', 1)])
>>> sorted(d)
['Batch', 'C_Type', 'Course', 'Name', 'Skills', 'Time End', 'Time Start', 'Travel']
>>> len(d)
8
>>> max(d)
'Travel'
>>> min(d)
'Batch'
>>> d.setdefault('Age')
>>> d
{'Name': 'Abhiram', 'Course': 'PFS', 'Batch': 52, 'Skills': ['Python', 'HTML', 'CSS'], 'C_Type': 'Offline', 'Time Start': 900, 'Time End': 1800, 'Travel': 1, 'Age': None}
>>> d.setdefault('Gender','Male')
'Male'
>>> d
{'Name': 'Abhiram', 'Course': 'PFS', 'Batch': 52, 'Skills': ['Python', 'HTML', 'CSS'], 'C_Type': 'Offline', 'Time Start': 900, 'Time End': 1800, 'Travel': 1, 'Age': None, 'Gender': 'Male'}
