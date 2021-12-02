x = 0
y = 0
aim = 0
with open('input') as f:
    for line in f:
        direction = line.split()[0]
        magnitude = int(line.split()[1])
        if direction == 'forward':
            x += magnitude
            y += aim * magnitude
        elif direction == 'down':
            aim += magnitude
        elif direction == 'up':
            aim -= magnitude
print(str(x * y))
