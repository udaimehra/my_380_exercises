text = "Python is powerful... and fast plays well with others runs everywhere is friendly & easy to learn is Open These are some of the reasons people who use Python would rather not use anything else"
text.lower()
new_arr = []
arr=text.split(' ')
for i in arr:
    x=i.replace('.', '')
    if len(i) >6:
        new_arr.append(x)
print(new_arr)
