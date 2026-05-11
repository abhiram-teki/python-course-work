'''
file = open('names.txt','r')
print(file.read())
file.close()
'''
'''
file = open('names.txt','r')
print(file.readlines())
file.close()
'''
'''
file = open('names.txt','r')
print(file.readline())
file.close()
'''
'''
with open('names.txt','r') as file:
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    print(file.read())
    file.close()
'''

'''
with open('names.txt','w') as file:
    file.write('Barry, Ada, Jill')
'''
'''
with open('names.txt','a') as file:
    file.write('Ada')
'''
'''
with open('names.txt','a+') as file:
    file.write('Jill')
    file.seek(0)
    print(file.read())
'''
try:
    with open('names1.txt','r+') as file:
        file.write('Jill')
        file.seek(0)
        print(file.read())
except Exception as e:
    print(f'Error occured {e}')
    
