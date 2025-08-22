"""a"""
planets = input()
# planets = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Sun"
# planets = "Sun Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune"
# planets = "Mercury Venus Earth Mars Sun Jupiter Saturn Uranus Neptune"
planets = planets.split()

# find Sun
suni = planets.index("Sun")


if len(planets) == 1:
    print("Hot:")
    print("Cool:")
else:
    hots = []
    cools = []
    if not suni:
        hots.append(planets[1])
        cools.append(planets[-1])
    elif suni == len(planets) - 1:
        hots.append(planets[-2])
        cools.append(planets[0])
    else:
        hots.append(planets[suni - 1]) # left of Sun
        hots.append(planets[suni + 1]) # right of Sun
        # if sun is not right in the middle, then the coldest planets
        # is either the first or the last
        if len(planets) > 3:
            if suni == len(planets) // 2:
                if planets[0] != planets[suni - 1]:
                    cools.append(planets[0])
                if planets[-1] != planets[suni + 1]:
                    cools.append(planets[-1])
            else:
                if suni < len(planets) // 2:
                    cools.append(planets[-1])
                else:
                    cools.append(planets[0])
        else:
            # i am going to kill myself
            cools.append(planets[0])
            cools.append(planets[-1])

    print("Hot:", " ".join(hots))
    print("Cool:", " ".join(cools))
