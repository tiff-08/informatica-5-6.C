def main():
    #print("Times Table Generator")
    #times_table = int(input("Enter a number between 1 and 10: "))

    print("Welcome to the times table quiz")
    while True:
        try:
            max_value = int(input("Enter a times table that you would like to be tested on (1-10): "))
            for x in range(1, max_value + 1):
                tables = int(input(f"{x} times {max_value} is "))
                if tables == (x * max_value):
                    print("Correct!")
        except ValueError:
            print("Invalid. Enter a number")

    #         if 1 <= times_table <= 10:

    #             print(f"Here is the {times_table} times table")

    #             for x in range(1, 11):
    #             answer = x * times_table
    #             print(f"{x} times {times_table} is {answer}")
    # else:
    #     print("Invalid command.")
if __name__=="__main__":
    main()
