import sys


n = int(raw_input().strip())
arr = map(long,raw_input().strip().split(' '))
total = long(0)

try:
    if(len(arr)in range(1,11)):
        for i in arr:
            
            try:
                i = long(i)
                if(i>=-2147483648 and i<2147483647):
                    total += i
            except:
                print("Invalid range")
    print total
except:
    print("Invalid range")


