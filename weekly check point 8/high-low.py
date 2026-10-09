def main():
    def highest(a,b):
            if a > b:
                highest_num = a
            else:
                highest_num = b
            print(f"The highest number entered is {highest_num}")

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    highest(num1, num2)

    def lowest(a,b,c):
            if a < b and a < c:
                lowest_num = a
            elif b < a and b < c:
                lowest_num = b
            else:
                lowest_num = c
            print(f"The lowest number entered is {lowest_num}")

    num3 = float(input("Enter first number: "))
    num4 = float(input("Enter second number: "))
    num5 = float(input("Enter third number: "))

    lowest(num3, num4, num5)

if __name__=="__main__":
    main()
