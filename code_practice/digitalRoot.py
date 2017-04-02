def digitalRoot(n):
    if n<10:
        return n
    else:
        total= 0
        n = str(n)
        
        listings=list(n)
         
        for i in range(0,len(listings)):
            total =total + int(listings[i])
        return digitalRoot(total)


print digitalRoot(5015)
