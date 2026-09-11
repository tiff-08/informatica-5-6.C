def main():
#blue
    #sort
    numbers = [1, 4, 5, 7, 9, 3]
    numbers.sort()
    print(numbers)

    items = ["Lettuce", "Tomato", "Bread", "Jam", "Mayonaise"]
    items.sort()
    print(items)

    numbers1 = [1, 4, 5, 7, 9, 3]
    numbers1.sort(reverse=True)
    print(numbers1)
#green
    # len()
    mylist = ["pensil","computer","shirt","phone","paper"]
    print(len(mylist))
#yellow
    #.append()
    fruits = ["apple","orange","grapes"]
    fruits.append("Banana")
    print(fruits)

    #insert()
    fruits1 = ["apple","orange","grapes"]
    fruits1.insert(2, "banana")
    print(fruits1)
#orange
    # max
    numbers2 = [1,2,3,4,5,6,7,8,9,10,11]
    resultm = max(numbers2)
    print(resultm)

    #min
    resultsmin = min(numbers2)
    print(resultsmin)

    #sum
    results = sum(numbers2)
    print(results)
#red
    #.pop .remove
    lista = ["Rojo","Amarillo","Verde","Naranja","Azul"]
    print("lista:", lista)

    lista.pop(1)
    print("con pop(1):", lista)

    lista.remove("Rojo")
    print("con remove(´Rojo´):", lista)








if __name__ == "__main__":
    main()
