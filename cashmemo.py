from datetime import datetime

x = datetime.now()
print(x)
y = datetime(2020, 5, 17)
print(y)
z = x.strftime("%d-%b-%Y")
print(z)
print("====================================")
# https://www.w3schools.com/python/python_datetime.asp

class Address:
    # You have to code this
    
    def __str__(self):
        return "0300 the dummy address"
        
class ItemsOnbill:
    def __init__(self, prt, rte, qty):
        self.__pirticular = prt
        self.__unitprice = rte
        self.__quantity = qty

    def __str__(self):
        return f"{self.__pirticular},  {self.__unitprice},   {self.__quantity},   {self.__unitprice*self.__quantity}"

class Bill:
    def __init__(self, no, dt, nm, ad, ib):
        self.__billno = no
        self.__billdate = dt
        self.__custname = nm
        self.__custaddr = ad
        self.__items = []
        self.__items.append(ib)

    def __str__(self):
        return f"{self.__billno},  {self.__billdate.strftime('%d-%b-%Y')}, \n   {self.__items}"

def main():
    b = (
    Bill(9988, datetime.now(), "Peter zeliski","The address",
    [
    ItemsOnbill("Mouse", 1, 2000),
    ItemsOnbill("Handfree", 2, 700)
    ]
    ))

    print(b)

main()    