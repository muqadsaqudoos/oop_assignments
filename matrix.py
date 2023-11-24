class Matrix:
    def __init__(self,row,col):
       self.row = row
       self.col = col
       self.data = [[0 for _ in range(col)]for _ in range(row)]

    def __str__(self):
       return '\n'.join([' '.join(map(str,row))for row in self.data])
    
    def __add__(self,other):
        if self.row!=self.row and self.col!=self.row:
            return None
        
        result = Matrix(self.row,other.col)
        result.data = [[self.data[i][j]+other.data[i][j] for j in range(other.col)]for i in range(self.row)]
        return result
    def __sub__(self,other):
        if self.row!=other.row and self.col!=other.col:
            return None
        
        result = Matrix(self.row,other.col)
        result.data = [[self.data[i][j]-other.data[i][j] for j in range(other.col)]for i in range(self.row)]
        return result
    
    def transpose(self):
        result = Matrix(self.row,self.col)
        result.data = [[self.data[j][i] for j in range(self.row)]for i in range(self.col)]
        return result
    
    def scalar_multiply(self,scalar):
        result = Matrix(self.row,self.col)
        result.data = [[self.data[i][j]*scalar for j in range(self.col)]for i in range(self.row)]
        return result
    
    def matrix_multiply(self,other):
        if self.col!=other.row:
            return None
        result = Matrix(self.row,other.col)
        result.data = [[sum(self.data[i][k]*other.data[k][j]for k in range(self.col)) for j in range(other.col)]for i in range(self.row)]
        return result
    


def main():
# Example Usage
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(3, 2)
    matrix2.data = [[7, 8], [9, 10], [11, 12]]

    print("Matrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    print("\nMatrix 1 + Matrix 2:")
    result_addition = matrix1 + matrix2
    if result_addition:
        print(result_addition)
    else:
        print("Matrix addition is not possible.")

    print("\nTranspose of Matrix 1:")
    print(matrix1.transpose())

    print("\nScalar Multiplication of Matrix 1:")
    print(matrix1.scalar_multiply(2))

    print("\nMatrix Multiplication of Matrix 1 and Matrix 2:")
    result_multiplication = matrix1.matrix_multiply(matrix2)
    if result_multiplication:
        print(result_multiplication)
    else:
        print("Matrix multiplication is not possible.")
main()