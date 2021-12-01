last_depth = None
increases = 0
with open('input') as file:
    for line in file:
        depth = int(line)
        if last_depth is not None:
            if depth > last_depth:
                increases += 1
        last_depth = depth
print(increases)
