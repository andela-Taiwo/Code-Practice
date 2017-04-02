def ransom_note(magazine, ransom):
    dico = dict()
    m = len(set(magazine))
    n = len(set(ransom))
    if(m >=1 and n<=3000):
        for word in magazine:
            if word.isalpha() and (len(word)in range(1,6)):
                dico[word] = word.lower()
            else:
                raise ValueError("Not a word")
        
        for word in ransom:
            if(word.lower() not in dico):
                return False
    return True
        
    
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    
