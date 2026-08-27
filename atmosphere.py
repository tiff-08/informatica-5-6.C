def main():
    layer1 = input("Descent atmosphere layer: ")

    if layer1 == "Exosphere":
        print("Your altitude layer would be between 700 and 10,000 km")
    elif layer1 == "Thermosphere":
        print("Your altitude layer would be between 85 and 700 km")
    elif layer1 == "Mesosphere":
        print("Your altitude layer would be between 50 and 85 km")
    elif layer1 == "Stratosphere":
        print("Your altitude layer would be between 12 and 50 km")
    elif layer1 == "Troposphere":
         print("Your altitude layer would be between 0 and 12 km")
    else:
         print("Not valid option")

    print("Enter exact altitud: ")





if __name__ == "__main__":
        main()
