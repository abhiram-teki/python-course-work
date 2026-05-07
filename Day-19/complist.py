res=[i for i in range(1,11)]
res2=[i*2 for i in range(1,11)]
res3=[i for i in range(1,101) if i%20==0]
print(res)
print(res2)
print(res3)
res4=[i for i in range(1,101) if i%2==0]
print(res4)
res5=[i for i in range(10,101,10)]
print(res5)
res6=[i for i in range(10,101,10) if i%20==0]
print(res6)
res7=[i if i%2==0 else 0 for i in range(1,11)]
print(res7)
s='I am Abhiram'
res8=[i for i in s]
print(res8)
vol='aeiouAEIOU'
res9=['*' if i in vol else i for i in s]
print(res9)
print(''.join(res9))
d={i for i in range(7,71,7)}
print(d)
d1={i:i*7 for i in range(1,11)}
print(d1)
