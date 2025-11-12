import sys

scores = [float(x) for x in sys.argv[1:]]

total = sum(scores)
average = total / len(scores)

print("Sum =", total)
print("Average =", average)
