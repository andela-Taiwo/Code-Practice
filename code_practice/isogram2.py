def is_isogram(word):

  
  if(type(word) != str):
    raise TypeError("Argument should be a string")
  elif(word == "" or word==" "):
    return(word,False)
    
  else:
    
    if(word.isalpha()):
      temp = word.lower()
      
      for i in range(0,len(temp)):
        for x in range(i+1,len(word)):
          if(temp[i] == temp[x]):
            return((word),False)


      return(word, True)




print is_isogram(2)
