import sys

scores = [float(x) for x in sys.argv[1:]]

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)
