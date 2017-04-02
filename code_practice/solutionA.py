def solution(A):
    temp = ""
    # write your code in Python 2.7
    sum_total = long(0)
    if(len(A) in range(0,100000)):
        for i in A:
            if ((i >= -2147483648)and(i < 2147483647)):
                temp = str(i)
               
                if(len(temp) == 2):
                    sum_total += i
                elif(len(temp)==3) and (temp[0] == "-"):
                    sum_total += i
                else:
                    sum_total =sum_total
                    
            else:
                return(-1)
                
        return sum_total
    else:
        return(-1)
        
    


print solution([47,1900,1,90,45])
