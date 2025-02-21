probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
high = []
for p in probabilities:
    if float(p) > 0.5:
        high.append(float(p))
print(high)
