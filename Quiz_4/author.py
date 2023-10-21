class Author:
    def __init__(self,name,email,gender):
        self.name = name
        self.email = email
        self.gender = gender

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,d):
        self.__name = d

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,d):
        self.__email = d

    @property 
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self,d):
        self.__gender = d

    def __str__(self):
        return f"{self.name} ({self.gender}) @ {self.email}"
class Book:
    def __init__(self,name,author,price,qtyInStock=0):
        self.name = name 
        self.author = author
        self.price = price
        self.qtyInStock = qtyInStock

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,b):
        self.__name = b

    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self,a):
        self.__author = a

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,p):
        if p>0:
            self.__price = p

    @property
    def qtyInStock(self):
        return self.__qtyInStock
    
    @qtyInStock.setter
    def qtyInStock(self,q):
        if q>=0:
            self.__qtyInStock = q

    def printInfo(self):
        print(f"{self.name} by {str(self.author)}")

    def getAuthorName(self):  
        return self.author.name
    
def main():
    author1 = Author("John", "abc@gmail.com","M")
    print(author1)
    book1 = Book("PythonOOP", author1, 40, 100)
    book1.printInfo()
    author1.name = "Peter"
    book1.name = "PythonPF"
    book1.author = Author("Jane Doe", "abc.de@gmail.com","")
    book1.price = 90
    book1.qtyInStock = 50
    print("Book Name:", book1.name)
    print("author of the book:", book1.getAuthorName())
    print("Price of the book:", book1.price)
    print("Quantity in stock:", book1.qtyInStock)



main()
