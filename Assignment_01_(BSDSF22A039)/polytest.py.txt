from polynomial import Polynomial
def main():
    a = Polynomial("y",3,[1,2,-1,4])
    b = Polynomial("y",3,[2,3,-1,8])
    c = Polynomial("y",3,[1,2,-1,4])
    print("a: " + str(a))
    print("b: " + str(b))
    print("a+b: " + str(a + b))
    print("b-a: " + str(b - a))
    print(a==c)
    


if __name__ == "__main__":
    main()