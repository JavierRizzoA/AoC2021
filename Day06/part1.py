fish = []

def simulate_day(fish):
    fish_to_add = 0
    for i in range(len(fish)):
        fish[i] -= 1
        if fish[i] < 0:
            fish[i] = 6
            fish_to_add += 1

    for i in range(fish_to_add):
        fish.append(8)


with open('input') as f:
    fish = list(map(int, f.read().split(',')))


for i in range(80):
    simulate_day(fish)

print(len(fish))
