def map_signals(signals):
    m = {}
    for s in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        appearances = list(filter(lambda x: s in x, signals))
        if len(appearances) == 6:
            m[s] = 'b'
            continue
        elif len(appearances) == 4:
            m[s] = 'e'
            continue
        elif len(appearances) == 9:
            m[s] = 'f'
            continue
        else:
            appearances_length = list(map(lambda x: len(x), appearances))
            appearances_length.sort()
            if appearances_length == [3, 5, 5, 5, 6, 6, 6, 7]:
                m[s] = 'a'
                continue
            elif appearances_length == [2, 3, 4, 5, 5, 6, 6, 7]:
                m[s] = 'c'
                continue
            elif appearances_length == [4, 5, 5, 5, 6, 6, 7]:
                m[s] = 'd'
                continue
            elif appearances_length == [5, 5, 5, 6, 6, 6, 7]:
                m[s] = 'g'
                continue
    return m


def apply_mapping(mapping, display):
    mapped = list(map(lambda c: mapping[c], display))
    mapped.sort()
    return "".join(mapped)


def decode_display(display):
    if display == 'cf':
        return 1
    elif display == 'acdeg':
        return 2
    elif display == 'acdfg':
        return 3
    elif display == 'bcdf':
        return 4
    elif display == 'abdfg':
        return 5
    elif display == 'abdefg':
        return 6
    elif display == 'acf':
        return 7
    elif display == 'abcdefg':
        return 8
    elif display == 'abcdfg':
        return 9
    elif display == 'abcefg':
        return 0


s = 0

with open('input') as f:
    for line in f:
        signals, output = tuple(map(lambda x: x.split(), line.split('|')))
        mapping = map_signals(signals)
        mapped_output = list(map(lambda x: apply_mapping(mapping, x), output))
        decoded_output = list(map(lambda x: decode_display(x), mapped_output))
        i = 0
        for d in decoded_output[::-1]:
            s += d * pow(10, i)
            i += 1

print(s)
