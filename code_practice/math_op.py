def gcd(a,b):
    
    while(a%b != 0):
        initial_a =a
        initial_b = b
        a=initial_b
        
        b=initial_a % initial_b
    return b

class Fraction(object):
    

    def __init__(self,top,bottom):

        try:
            if(type(top)==int or type(top)==long) and (type(bottom)==int or type(bottom)==long):
                self.num = top
                self.den = bottom
        except:
            print("Bad value")
            
    def __str__(self):

        return (str(self.num) + "/" + str(self.den))

    def __add__(self, otherfraction):
        try:
            if(type(top)==int or type(top)==long) and (type(bottom)==int or type(bottom)==long) and(bottom>0):
                new_num = self.num*otherfraction.den + self.den*otherfraction.num
                new_den = self.den * otherfraction.den
                common_factor = gcd(new_num,new_den)
                return(Fraction(new_num//common_factor,new_den//common_factor))
        except:
            print("Invalid value, integer expected")
        

    
    def __mul__(self,otherfraction):
        try:
            if(type(top)==int or type(top)==long) and (type(bottom)==int or type(bottom)==long) and(bottom>0):    
                new_num = self.num*otherfraction.num
                new_den = self.den* otherfraction.den
                common = gcd(new_num,new_den)
                return(Fraction(new_num//common,new_den//common))
        except:
            print("Invalid value, integer expected")
    
    def __sub__(self,otherfraction):
        try:
            if(type(top)==int or type(top)==long) and (type(bottom)==int or type(bottom)==long) and(bottom>0):    
                new_num = self.num*otherfraction.den - self.den*otherfraction.num
                new_den = self.den * otherfraction.den
                common_factor = gcd(new_num,new_den)
                return(Fraction(new_num//common_factor,new_den//common_factor))
        except:
            print("Invalid value, integer expected")


x = Fraction(2,0)
y = Fraction(1,5)
print (x+y)
print(x*y)
print(x-y)

        
