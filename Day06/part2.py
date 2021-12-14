fish = {}

for i in range(9):
    fish[i] = 0

with open('input') as file:
    for f in list(map(int, file.read().split(','))):
        fish[f] += 1

for d in range(256):
    new_fish = fish[0]
    fish = {(k - 1): v for k, v in fish.items()}
    fish[6] += fish[-1]
    fish.pop(-1)
    fish[8] = new_fish

total_fish = 0
for f in fish.values():
    total_fish += f

print(total_fish)
