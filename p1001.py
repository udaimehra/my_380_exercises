def capital_indexes(str):
    pos = []
    for i in str:
        if i.isupper():
            pos.append((str.index(i)))
    print(pos)
str=input("Enter a String with upper and lower letters: ")
capital_indexes(str)
