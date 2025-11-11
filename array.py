scores = input("Enter scores separated by spaces: ").split()
scores = [float(s) for s in scores]

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)
