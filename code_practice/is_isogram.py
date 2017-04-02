def is_isogram(word):
  duplicate = []
  result = False
  no_duplicate =[]
  
  
  if(type(word) != str):
    raise TypeError("Argument should be a string")
  elif(word == ""):
    
    return(word, result)
  
  else:
    word = list(word)
    for i in range(0,len(word)):
      if(word[i] not  in duplicate):
        no_duplicate.append(True)
      else:
        no_duplicate.append(False)
        
      duplicate.append(word[i])
      
    if False in no_duplicate:
      return(word,False)
    else:
      return(word,True)
        
  
