def power(a,b):
  result = 1
  
  if((type(a) == int or type(a)==float) and(type(b)==float or type(b)==int)):
    if(a==0):
      return (0)
    elif(b==0):
      return(1)
    
    else:
      result=a*power(a,b-1)
      return result
    
  
  
  else:
    raise TypeError("Argument must be integer of float")


print(power(0,2))
