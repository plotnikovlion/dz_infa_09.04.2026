from random import randint
a=[0]*5
b=[0]*5
c=[0]*5
d=[0]*3
for i in range(5):
    a[i]=randint(0,100)
    b[i]=randint(0,100)
    c[i]=randint(0,100)
d[0]=max(a)
d[1]=max(b)
d[2]=max(c)
print(a,b,c)
print(d)
