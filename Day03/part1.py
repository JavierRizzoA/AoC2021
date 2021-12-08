positions = []

with open('input') as file:
    lines = file.readlines()
    for i in range(len(lines[0].strip())):
        positions.append({0: 0, 1: 0})
    for line in lines:
        i = 0
        for c in line.strip():
            positions[i][int(c)] += 1
            i += 1

gamma = 0
epsilon = 0
i = 0
for p in positions[::-1]:
    gamma += pow(2, i) * max(p, key=p.get)
    epsilon += pow(2, i) * min(p, key=p.get)
    i += 1

print(gamma * epsilon)
