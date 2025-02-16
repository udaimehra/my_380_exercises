text = 'python is a popular programming language.'
n = int(0)
new_text = ''
for i in text:
    if n == 0:
        i = i.upper()
        new_text = new_text + i
    else:
        new_text = new_text + i
    n = n + 1
print(new_text)
