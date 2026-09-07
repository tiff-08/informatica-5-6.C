import time
def main():
    print("Remember drink your daily water")
    input("do you consider yourself a sendentary person, Moderate activity person or a sportman? ")
    reminder = 5

    while reminder >0:
          print("drink water")
          time.sleep(10)
          reminder = reminder - 1


if __name__ == "__main__":
        main()
