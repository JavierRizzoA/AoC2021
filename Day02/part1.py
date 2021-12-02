x = 0
y = 0
with open('input') as f:
    for line in f:
        direction = line.split()[0]
        magnitude = int(line.split()[1])
        if direction == 'forward':
            x += magnitude
        elif direction == 'down':
            y += magnitude
        elif direction == 'up':
            y -= magnitude
print(str(x * y))
