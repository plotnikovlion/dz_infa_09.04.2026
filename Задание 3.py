from random import randint
a=[0]*5
s=0
for i in range(5):
    a[i]=randint(0,100)
    if i%2==1:
        s+=a[i]
print(a,s)
