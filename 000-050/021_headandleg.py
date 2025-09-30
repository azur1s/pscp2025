"""a"""
animal = int(input())
leg = int(input())

bunny = (leg - 2 * animal) // 2
bird = animal - bunny

if bunny < 0 or bird < 0 or (4 * bunny + 2 * bird) != leg:
    print("Impossible")
else:
    print(bunny, bird)
