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
    def __str__(self):
        pstr = ""
        a = self.list_of_coffients
        a.reverse()
        for i in range(self.degree,-1,-1):
            if i != 0:

                pstr += f"({str(a[i])}{str(self.var)}^{str(i)})+"
        pstr += f"({str(a[0])})"


        return pstr
    
def main():
    a = Polynomial("y",3,[1,2,-1,4])
    print(a)

main()