output = 0

with open('input') as f:
    for line in f:
        output += len(list(filter(lambda n: n in [2, 4, 3, 7],
            map(lambda s: len(s), line.split('|')[1].split()))))

print(output)
