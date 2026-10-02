def main():
    print("Welcome to the times table quiz")
    while True:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))

            while True:
                try:
                    max_value = int(input("Enter the maximum value for your times table: "))


                    if 1 <= times_table <= 10:

                        print(f"Here is the {times_table} times table")

                        for x in range(1, max_value + 1):
                            answer = x * times_table


                            try:
                                user_answer = int(input(f"{x} times {times_table} is "))

                                if user_answer == answer:
                                    print("Correct answer!")
                                else:
                                    print("Incorrect")
                            except ValueError:
                                print("Enter a number for your answer")
                    else:
                        print("Invalid command.")
                except ValueError:
                    print("Enter a number")
        except ValueError:
            print("Enter a number")
if __name__=="__main__":
    main()
