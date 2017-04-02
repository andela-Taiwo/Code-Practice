def hailStone(n):
    if(n>1 and n%2 ==0):
        print n
        n = n/2
        hailStone(n)
    elif(n>1 and n%2!=0):
        print n
        n=3*n+1
        hailStone(n)
    else:
        return n


hailStone(5)

