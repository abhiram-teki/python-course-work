import collections as co

'''
s='Python program'
text='Python is an essential part of various industries'
l=[1,2,4,5,6,7,4,5,7,1,3,9,9,9,4,1,3,8,4,3,1,9,5]
print(co.Counter(s))
print(co.Counter(text.split()))
print(co.Counter(l))

d=co.defaultdict(int)
for i in s:
    d[i]+=1
    
print(d)
'''
'''
q=co.deque([])
q.append(10)
q.append(20)
q.append(30)
q.append(40)
q.popleft()
q.popleft()
q.append(50)
q.append(60)
q.popleft()
q.popleft()
q.popleft()
q.append(70)
q.append(80)
print(q)
'''

q=co.deque([])
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)
q.pop()
q.pop()
q.appendleft(50)
q.appendleft(60)
q.pop()
q.pop()
q.pop()
q.appendleft(70)
q.appendleft(80)
print(q)
