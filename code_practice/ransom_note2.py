def ransom_note(magazine, ransom):
    dico = dict()
    m = set(magazine)
    n = set(ransom)
    print m
    print n
    if(len(m) >=1 and len(n)<=3000):
        for word in m:
            if word.isalpha() and (len(word)in range(1,6)):
                dico[word] = word.lower()
            else:
                raise ValueError("Not a word")
        
        for word in n:
            if(word.lower() not in dico):
                return False
        return True
    else:
        raise ValueError("Out of range")
    
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().lower().strip().split(' ')
ransom = raw_input().lower().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    
