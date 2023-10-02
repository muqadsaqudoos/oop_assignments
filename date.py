class Date:
    def __init__(self,date,month,year):
        self.date = date
        self.month = month
        self.year = year

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self,d):
        if d<=31:
            self.__date = d
        return self.__date
    
    @property
    def month(self):
        return self.__month
    @month.setter
    def month(self,d):
        if d<=12:
            self.__month = d
        return self.__month
    
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,d):
        self.__year = d
        return self.__year
    

    def __str__(self):
        return f"{self.date}/{self.month}/{self.year}"
    


def main():
    a = Date(30,9,2023)
    print(a)

main()

         
    
