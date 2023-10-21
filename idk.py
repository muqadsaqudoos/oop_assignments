from datetime import datetime
print('MOBILO')
print('Mobile City')
print('Deals in all kinds of Mobile sets and Accsessories')
print('Cell No: 0321-0000000')
x = datetime.now()
y = datetime(2020, 5, 17)
z = x.strftime("%d-%b-%Y")
print("====================================")
class name:
    def _init_(self, fn, ln):
        self.__firstname= fn
        self.__lastname=ln
    def _str_(self):
        return f'{self._firstname} { self._lastname}'
class address:
    def _init_(self, hn, block, town, city):
        self.__houseno=hn
        self.__block=block
        self.__town = town
        self.__city= city
    def _str_(self):
        return f'{self._houseno} {self.block} {self.town} {self._city}'
class ItemsOnbill:
    def _init_(self, prt, rte, qty):
        self.__pirticular = prt
        self.__unitprice = rte
        self.__quantity = qty
    def _str_(self):
        return f"{self._pirticular}, {self.unitprice}, {self.quantity}, {self.unitprice * self._quantity}"

class Bill:
    def _init_(self, no, dt, nm, ad, ib):
        self.__billno = no
        self.__billdate = dt
        self.__custname = nm
        self.__custaddr = ad
        self.__items = []
        self.__items.append(ib)

    def _str_(self):
        return f"{self._billno}\n{self.billdate.strftime('%d-%b-%Y')}\n{ self.custname}\n{self.custaddr} \n{self._items}"
def main():
    a=[
    ItemsOnbill('Mouse', 1, 2000),
    ItemsOnbill('Handfree', 2, 700)
    ]
    b = (
    Bill(9988, datetime.now(), name('Peter','zeliski'),address('1010','c2','freaks town','dc'),a
    ))

    print(b)
main()
print('Signature:kaz')
print('Adress: Basement # 2, Allahwala Plaza, Markaz K8, Islamabad')