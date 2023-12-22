import math
class Vector:
    def __init__(self, *vector):
        self.vector = vector

    def magnitudeOfVector(self):
        sum = 0
        for i in range(len(self.vector)):
            sum = sum + ((self.vector[i])**2)
        return f"{math.sqrt(sum):.4f}"
    
    def dotProduct(self,other):
        sum = 0
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must have the same dimension for dot vector")

        for i in range(len(self.vector)):
            sum = sum + (self.vector[i]*other.vector[i])
        return sum
    
    def __add__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must have the same dimension for addition")
        
        v = (self.vector[i]+other.vector[i] for i in range(len(self.vector)))
        return Vector(*v)
    
    def __sub__(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must have the same dimension for Subtraction")
        
        v = (self.vector[i]-other.vector[i] for i in range(len(self.vector)))
        return Vector(*v)
    
    def scalarProduct(self, a):
        v = (a*self.vector[i] for i in range(len(self.vector)))
        return Vector(*v)
    
    def __str__(self):
        vstr = "<"
        a = len(self.vector) - 1
        for i in range(len(self.vector)):
            vstr += str(self.vector[i])
            if i < a:
                vstr += ","

        vstr += ">"
        return vstr
    
    def listAllElements(self):
        a = []
        for i in range(len(self.vector)):
            a.append(self.vector[i])
        return a

    def isEmpty(self):
        if len(self.vector) == 0:
            return f"vector has no components"   
        else:
            return f"Vector has components"
        
    def isnullVector(self):
        a = 0
        for i in range(len(self.vector)):
            if self.vector[i] == 0:
                a += 1

        if a == len(self.vector):
            return f" it is a null vector"
        else:
            return f"it is not a null vector"
        
    def addAllElements(self):
        sum = 0
        for i in range(len(self.vector)):
            sum += self.vector[i]
        return sum
    
    def dimentionOfVector(self):
        a = len(self.vector)
        return f"It is a {a} dimensional vector"
    
def main():
    #2 dimension vector
    v1 = Vector(1,3)
    v2 = Vector(4,5)
    print(v1,v2)

    #3 dimension Vector
    v3 = Vector(1,2,0)
    v4 = Vector(3,6,2)
    print(v3)
    print(v4)
    print(f"Vector Addition : {v3+v4}")
    print(f"Vector Subtraction : {v3-v4}")
    print(f"Magnitude of Vector: {v3.magnitudeOfVector()}")
    print(f"Dimension of vector: {v4.dimentionOfVector()}")

    #4 dimension vector
    v5 = Vector(3,5,2,8)
    v6 = Vector(-2,4,-8,0)
    print(v5)
    print(v6)
    print(f"Dot product of Vector: {v5.dotProduct(v6)}")
    print(f"Scalar product of Vector : {v5.scalarProduct(4)}")
    print(f"List all elements of vector: {v5.listAllElements()}")
    print(f"Dimension of vector: {v6.dimentionOfVector()}")
    
    #5 dimension vector
    v5 = Vector(2,4,5,2,12)
    v6 = Vector()
    v7 = Vector(0,0,0,0,0)
    print(v5)
    print(f"Add all elements of Vector: {v5.addAllElements()}")
    print(f"Empty vector: {v6.isEmpty()}")
    print(f"Null vector: {v7.isnullVector()}")

main()

    

            


    

    

            