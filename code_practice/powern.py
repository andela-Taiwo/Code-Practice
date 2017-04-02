def power(a,b):
  
  if(type(a)==int or type(a)==float and(type(b)==int or type(b)==float)):
    
    result = 1
    
    if(b==0):
      return(1)
    elif(b==1):
      return(a)
    elif(b<0):
      b=-(b)
      for i in range (0,b):
        result=a*power(a,b-1)
        result =float(result)
      print result
      return((1/result))
      
    else:
        result = a*power(a,b-1)
      
        return(result)
  
  
  else:
    raise TypeError("Arguments should be integer or float")
    

print (power(2,3))
