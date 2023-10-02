class Fraction:
    def __init__(self,num,den):
        self.num = num
        self.den = den
        
    def show(self):
        print(f"{self.num}/{self.den}")
        
    def multiply(self,other):

        num = self.num*other.num
        den = self.den*other.den
        return f"{num}/{den}"
    
    def real_number(self):
        return (self.num)/(self.den)
    

def main():
    a = Fraction(3,4)
    a.show()
    b= Fraction(9,10) 
    f = a.multiply(b)
    print(f)
    
    print(b.real_number())

main()

