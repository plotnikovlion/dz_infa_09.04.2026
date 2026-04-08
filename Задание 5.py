from random import randint
a=[0]*5
k=0
for i in range(5):
    a[i]=randint(0,100)
print(a)
for i in range(1,4):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        k+=1
print(k)
