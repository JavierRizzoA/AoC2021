import statistics

crabs = None

with open('input') as f:
    crabs = list(map(int, f.read().split(',')))

avg = int(statistics.mean(crabs))

fuel = 0
for c in crabs:
    for i in range(abs(c - avg)):
        fuel += i + 1

print(fuel)
