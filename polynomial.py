class Polynomial:
    def __init__(self,var,degree,list_of_coffients):
        self.var = var
        self.degree = degree
        self.list_of_coffients = list_of_coffients

    @property
    def var(self):
        return self.__var
    @var.setter
    def var(self,d):
        self.__var = d
        return self.__var
    
    @property
    def degree(self):
        return self.__degree
    @degree.setter
    def degree(self,d):
        self.__degree = d
        return self.__degree
    @property
    def list_of_coffients(self):
        return self.__list_of_coffients
    @list_of_coffients.setter
    def list_of_coffients(self,d):
        self.__list_of_coffients = d
        return self.__list_of_coffients
    
    
    def __add__(self, other):
        result_degree = self.degree
        result_coefficients = [0]*(result_degree+1)
        for i in range(self.degree,-1,-1):
            result_coefficients[i] = (self.list_of_coffients[i]+other.list_of_coffients[i])
        return Polynomial(self.var, result_degree, result_coefficients)
    def __sub__(self, other):
        result_degree = self.degree
        result_coefficients = [0]*(result_degree+1)
        for i in range(self.degree,-1,-1):
            result_coefficients[i] = (self.list_of_coffients[i]-other.list_of_coffients[i])
        return Polynomial(self.var, result_degree, result_coefficients)
    def __eq__(self,other):
        if self.degree == other.degree and self.list_of_coffients == other.list_of_coffients:
            return f"Polynomial  {self} and Polynomial {other} are equal"
        else:
            return f"Polynomial  {self} and Polynomial {other} are not equal"
    def __str__(self):
        pstr = ""
        a = self.list_of_coffients
        c = self.degree
        for i in range(len(a)-1):

            pstr += f"({str(a[i])}{str(self.var)}^{c})+"
            c-=1
        pstr += f"{a[-1]}"


        return pstr
    
