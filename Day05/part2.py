plane = {}


def add_to_plane(x, y):
    if not x in plane:
        plane[x] = {}
    if not y in plane[x]:
        plane[x][y] = 1
    else:
        plane[x][y] += 1


def count_overlaps(plane):
    overlaps = 0
    for x, val in plane.items():
        for y, overlap in val.items():
            if overlap > 1:
                overlaps += 1
    return overlaps


with open('input') as f:
    for line in f:
        start, end = tuple(line.split(' -> '))
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+ 1):
                add_to_plane(x1, y)
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                add_to_plane(x, y1)
        else:
            xd = 1
            yd = 1

            if x2 < x1:
                xd = -1
            if y2 < y1:
                yd = -1

            for d in range(max(x1, x2) - min(x1, x2) + 1):
                add_to_plane(x1 + d * xd, y1 + d * yd)


print(count_overlaps(plane))
