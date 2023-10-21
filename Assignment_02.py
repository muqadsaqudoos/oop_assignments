from datetime import datetime
print("MOBILO\nMobile City\nDeals in all kindsof Mobile sets and Accessories\nCell No: 0321-000000\nCASHMENO")
print("================================")


class Address:
    def __init__(self, street, city, state, zipcode):
        self.Street = street
        self.City = city
        self.State = state
        self.Zipcode = zipcode
    @property   
    def Street(self):
        return self.street
    
    @Street.setter
    def Street(self,s):
        self.street = s

    @property
    def City(self):
        return self.city
    @City.setter
    def City(self,c):
        self.city = c
    @property
    def State(self):
        return self.state
    
    @State.setter
    def State(self,s):
        self.state = s

    @property
    def Zipcode(self):
        return self.zipcode
    
    @Zipcode.setter
    def Zipcode(self,z):
        self.zipcode = z

    def __str__(self):
        return f"{self.street},{self.city},{self.state},{self.zipcode}"
class ItemsOnBill:
    def __init__(self,particulars,qty,rate):
        self.Particulars = particulars
        self.Particular_price = rate
        self.Particular_qunatity= qty

    def __str__(self):
        return f"{self.Particulars}\t\t\t{self.Particular_qunatity}\t\t\t{self.Particular_price}\t\t\t{self.Particular_price*self.Particular_qunatity}"
         
    

class Bill:
    def __init__(self,bill_no,date,coust_name,coust_add,items,signature,total=0):
        self.Bill_No = bill_no
        self.Date = date
        self.Coustomer_Name = coust_name
        self.Coustomer_Address = coust_add
        self.Items_On_Bill = items
        self.Signature = signature
        self.Total = total
    def __str__(self):
        b = ""
        b += f"No: {str(self.Bill_No)}\n"
        b += f"Date: {str(self.Date.strftime('%d-%b-%Y'))}\n"
        b += f"Name: {str(self.Coustomer_Name)}\n"
        b += f"Address: {str(self.Coustomer_Address)}\n"
        b += f"Particulars\t\tQTY\t\tRate\t\tAmount\n"

        for obj in self.Items_On_Bill:
            b += f"{obj}\n"
            self.Total+=(obj.Particular_price*obj.Particular_qunatity)

        b += f"Signature: {str(self.Signature)} \t\t"
        b += f"Total: {self.Total}"
        return b

def main():
    b = (Bill(9988, datetime.now(), "Peter zeliski",Address("street 2","lahore","Punjab","5400"),
     [
    ItemsOnBill("Keyboard", 1, 2000),
    ItemsOnBill("Handfree", 2, 700)
    ],"mobilo"))

    print(b)
    print("================================")
    print("Adress: Basement # 2, Allahwala Plaza, Markaz K8, Islamabad")
main()