def my_sort(listings):
  odd_number =[]
  even_number = []
  for item in listings:
    if(item>0 and type(item)==int):
      if(item %2 ==0):
        even_number.append(item)
      
      elif(item % 2 ==1):
        odd_number.append(item)
    else:
      raise TypeError("Invalid output")
        
  
  odd_number = sorted(odd_number)
  even_number = sorted(even_number)
  
  return(odd_number+even_number)    
    

print my_sort([90, 45, 66])
