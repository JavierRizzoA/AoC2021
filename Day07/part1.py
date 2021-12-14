import statistics

crabs = None

with open('input') as f:
    crabs = list(map(int, f.read().split(',')))

median = int(statistics.median(crabs))

fuel = 0
for c in crabs:
    fuel += abs(c - median)

print(fuel)
