def main():
    doctrine = ["faith","repentance","baptism","confirmation","endure to the end"]

    for principle in doctrine:
        print(principle)
    for i in range(len(doctrine)):
        print(f"{i+1}. {doctrine[i]}")
if __name__=="__main__":
    main()
