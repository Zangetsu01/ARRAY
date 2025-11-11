scores = input("Enter scores separated by spaces: ").split()
scores = [float(s) for s in scores]

total = sum(scores)
average = total / len(scores)

print("Sum =", total)
print("Average =", average)
