x =['T', 'h', 'i', 's', 'i', 's', 'h', 'o', 'w', 'w', 'e', 'r', 'o', 'c', 'k']
q = ['T', 'h', 'i', 's', 'i', 's', 'h', 'o', 'w', 'w', 'e', 'r', 'o', 'c', 'k','v','i','c','t','i','m']

for i in x:
    if(i==" "):
        x.remove(i)
    
print(x)

y=dict()

for i in x:
    counter =x.count(i)
    y[i] = counter

print(y)

z=set(x)
w = set(q)

print z-w

