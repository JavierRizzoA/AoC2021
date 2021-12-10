def parse(lines):
    numbers = list(map(int, lines[0].split(',')))
    boards = []
    for line in lines[1:]:
        if line == '':
            boards.append([])
        else:
            boards[len(boards) - 1].append(list(map(int, line.split())))

    return (numbers, boards)


def mark_boards(n, boards):
    for b in range(len(boards)):
        for r in range(len(boards[b])):
            for c in range(len(boards[b][r])):
                if boards[b][r][c] == n:
                    boards[b][r][c] = 'x'


def check_win_vertical(board):
    for c in range(len(board[0])):
        if len(list(filter(lambda r: not r[c] == 'x', board))) == 0:
            return True
    return False


def check_win_horizontal(board):
    for line in board:
        if len(list(filter(lambda c: not c == 'x', line))) == 0:
            return True
    return False


def check_win(boards):
    for b in boards:
        if check_win_vertical(b) or check_win_horizontal(b):
            return b
    return None


def get_points(n, board):
    s = 0
    for row in board:
        for col in row:
            if not col == 'x':
                s += col
    return s * n


lines = None
with open('input') as file:
    lines = file.read().splitlines()

numbers, boards = parse(lines)
found = False

for n in numbers:
    if found:
        break
    mark_boards(n, boards)
    b = check_win(boards)
    while b:
        if len(boards) == 1:
            print(get_points(n, b))
            found = True
            break
        else:
            boards.remove(b)
        b = check_win(boards)

