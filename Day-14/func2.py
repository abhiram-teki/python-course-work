'''
def display():
    global n
    n+=10
    print('In: ',n)

n=10
display()
print('Out: ',n)
'''
'''
def display(n):
    n+=10
    print('In: ',n)

n=20
display(n)
print('Out: ',n)
'''

def display(course):
    print('Start: ', course)
    def change():
        nonlocal course
        course="JFS"
        print('Course changed: ', course)
    change()
    print('Final: ',course)
course='PFS'
display(course)

'''
s='Python'
print(len(s))
print=23
print(len)
'''
