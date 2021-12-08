def count_bits_in_pos(blist, index):
    d = {0: 0, 1: 0}
    for l in blist:
        d[int(l[index])] += 1
    return d

oxygen = 0
with open('input') as file:
    lines = file.read().splitlines()
    i = 0
    while len(lines) > 1:
        c = count_bits_in_pos(lines, i)
        common = None
        if c[0] > c[1]:
            common = 0
        elif c[1] > c[0]:
            common = 1
        else:
            common = 1
        lines = list(filter(lambda line: line[i] == str(common), lines))
        i += 1
    oxygen = int(lines[0], 2)


scrubber = 0
with open('input') as file:
    lines = file.read().splitlines()
    i = 0
    while len(lines) > 1:
        c = count_bits_in_pos(lines, i)
        common = None
        if c[0] < c[1]:
            common = 0
        elif c[1] < c[0]:
            common = 1
        else:
            common = 0
        lines = list(filter(lambda line: line[i] == str(common), lines))
        i += 1
    scrubber = int(lines[0], 2)

print(oxygen * scrubber)
