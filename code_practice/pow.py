"""
This function calculate the exponential value of number
"""

def power(a,b):
    result =1
    if(type(a) == int or type(a)==float and(type(b)==int or type(b)==float)):
        if(b==0):
            return(1)
        elif(b==1):
            return(a)
        else:
            for i in range(0,b):
                result = a*power(a,b-1)
                
            return(result)
    else:
        raise TypeError("Argument should be integer or float")
    
    
    
print(power(2,3))
