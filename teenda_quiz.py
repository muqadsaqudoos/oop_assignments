from random import randint


class Teenda:
    def __init__(self,c,d):
        self.Category = c
        self.Data = d
        self.__dead = False

    @property
    def Category(self):
        return self.__category
    
    @Category.setter
    def Category(self,c):
        self.__category = c

    @property
    def Data(self):
        return self.__data
    
    @Data.setter
    def Data(self,d):
        self.__data = [0]*5
        self.__data[0] = d[0]
        self.__data[1] = d[1]
        self.__data[2] = d[2]
        if self.Category == 5:
            self.__data[3] = d[3]
            self.__data[4] = d[4]


    @property
    def Dead(self):
        return self.__dead
    
    def destroy(self):
        self.__dead = True

    def isValid(self):
        valid = False
        if (self.Category == 3 and self.Data[1] == max(self.Data) and self.Data[0]>self.Data[2]):
            valid = True

        elif (self.Category == 5 and self.Data[2] == max(self.Data) and self.Data[1]>self.Data[0] and self.Data[1]>self.Data[3] and self.Data[1]>self.Data[4] and self.Data[0]>self.Data[4]):
            valid = True

        return valid
    def grow(self):
        if self.Category == 3:
            print("growing .... " + str(self))
            self.Category = 5

            self.Data[4] = self.Data[2]
            self.Data[2] = self.Data[1]
            self.Data[1] = (self.Data[0] + self.Data[2]) // 2
            self.Data[3] = (self.Data[2] + self.Data[4]) // 2
            if not self.isValid():
                self.destroy()
        
    def split(self):

        if (self.Category==5):
            print("splitting...."+str(self))
            self.Category = 3

            half = self.Data[2]//2
            t1 = Teenda (3 ,(self.Data[0],self.Data[1],half))
            t2 = Teenda (3 ,(half,self.Data[3],self.Data[4],half))
            if not t1.isValid():
                t1.destroy()
            if not t2.isValid():
                t2.destroy()
            self.destroy()
            return [t1,t2]
       
        
    def mutate(self):
        rn = randint(1094,2088)
        if (rn%20 == 0) and (rn%5 == 0) :
            self.split()

        elif (rn%2 == 0) and (rn%18 == 0) :
            self.grow()

    def __str__(self):
        if self.Category == 3:
            return f"(T3 : {str(self.Data[0])} , {str(self.Data[1])} , {str(self.Data[2])})"
        if self.Category == 5:
            return f"(T5 : {str(self.Data[0])} , {str(self.Data[1])} , {str(self.Data[2])} , {str(self.Data[3])} , {str(self.Data[4])})"


def main():
    teendas = []
    teendas.append(Teenda(3, [4, 7, 2]))
    teendas.append(Teenda(5, [23, 35, 42, 30, 20]))
    teendas.append(Teenda(3, [7, 29, 3]))
    for i in range(50):
        print("Iteration NO",i)
        for j in teendas:
            if j.Dead == False:
                print(j)

        for j in teendas:
            if j.Dead == False:
                newteendas = j.mutate()
                if newteendas:
                    for k in newteendas:
                        teendas.append(k)
main()
  