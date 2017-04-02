# -*- coding: utf-8 -*-
def solution(A):

    sum1 = 0
    sum2 = 0
    equi =[]

    if((len(A) in range (0,100000))):
        for i,value in enumerate(A):
            if((i >= -2147483648) and(i<2147483647)):
                
                sum1 = sum(A[0:i])

                sum2 = sum(A[i+1:])
                
                if(sum1 == sum2):
                    return(i)

                
            else:
                raise ValueError("Integer out of the range")
            
        if((len(equi)==0)or len(A)==0):
            return(-1)

    else:
        raise ValueError("Out of the range")
            

  
        
    




print solution([-1])

            

    
