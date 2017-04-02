
import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
total = None 
sum1 = long(0)
sum2 =long(0)
x = 0
for k in range (0,n):
    if(k == 0) :
        
        for j in range(0,n):
            sum1 += a[j][j]
   
    elif( k==n-1):
        for l in range(n-1,-1,-1):
            sum2 += a[x][l]
            x +=1
    else:
        sum1 +=0
       
print abs(sum1 - sum2)
