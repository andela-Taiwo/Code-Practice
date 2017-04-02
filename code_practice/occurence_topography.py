

from collections import Counter

def outputString(text):
    output1 = dict()
    output2 = []
    counter_store=[]
    
    text_lst = list(text)
    if(len(text) in range(3,10000)) and(text.isalpha()):
        text = text.lower()
        for x in text_lst:
            counter = text_lst.count(x)
            
            output1[x] = counter
        output2 = sorted(output1.items())
        print output2
        output2 =  sorted(output2, key=lambda x: x[1], reverse=True)

        for i in range(0,3):
            print(output2[i][0]),
            print (output2[i][1])          
       
    else:
       return(-1)


def occurence(text):
    c = Counter(text)
    print c
    c = sorted(c.items())
    print c
    c = sorted(c, key=lambda x: x[1], reverse=True)
    for i in range(3):
        print (c[i][0], c[i][1])
    




outputString("aabbbccde")
occurence("aabbbccde")
