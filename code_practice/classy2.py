def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         self.num1 = top
         self.den1 = bottom

     def __str__(self):
         return str(self.num1)+"/"+str(self.den1)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num1*otherfraction.den1 + \
                      self.den1*otherfraction.num1
         newden = self.den1 * otherfraction.den1
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
         firstnum = self.num1 * other.den1
         secondnum = other.num1 * self.den1

         return firstnum == secondnum
    

x = Fraction(1,2)
y = Fraction(2,3)
print(x)
print(y)
print(x+y)
print(x == y)
