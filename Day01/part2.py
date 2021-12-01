last_depth = None
increases = 0
with open('input') as file:
    lines = file.readlines()
    for i in range(len(lines) - 2):
        depth = sum(map(int, lines[i:i+3]))
        if last_depth is not None:
            if depth > last_depth:
                increases += 1
        last_depth = depth
print(increases)
