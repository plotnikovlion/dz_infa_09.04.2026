from random import randint
a=[0]*5
b=[0]*7
for i in range(5):
    a[i]=randint(0,100)
for i in range(7):
    b[i]=randint(0,100)
print("Первый массив:",a)
print(int(sum(a)/len(a)),sum(a))
print("Второй массив:",b)
print(int(sum(b)/len(b)),sum(b))
