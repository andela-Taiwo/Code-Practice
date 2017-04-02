"""
def solution(N):
    # write your code in Python 2.7
    message = {3:"Fizz",5:"Buzz",7:"Woof"}
    if(N in range(1,1000)):
        for i in range(1,N+1):
            for k,v in message.items():
                k = long(k)
                if(i % k ==0):
                    i = v
            print i
    else:
        raise valueError("Out of range")

"""



def solution(N):
    # write your code in Python 2.7
    message = ["Fizz","Buzz","Woof"]
    N =long(N)
    i = long(1)
    if(N in range(1,1000)):
        for i in range(1,N+1):
            if(i%3==0 and i%5 ==0 and i%7 == 0):
                i= message[0]+message[1]+message[2]
            elif(i%3==0 and i%5 ==0):
                i = message[0]+message[1]
            elif(i%7 == 0 and i%3 ==0):
                i= message[0]+message[2]
            elif(i%3==0):
                i = message[0]
            elif(i%5 ==0 ):
                i = message[1]
            elif(i % 7 ==0):
                i =message[2]
            else:
                i = i
            print i

            
    else:
        raise valueError("Out of range")

solution(24)
