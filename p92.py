probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
cls = []
for p in probabilities:
    if float(p) > 0.5:
        cls.append(1)
    else:
        cls.append(0)
print(cls)
