# RESTRICTED: list split tuple append dict set [] sort insert del

"""a"""
planets = input()
# planets = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Sun"
# planets = "Sun Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune"
# planets = "Mercury Venus Earth Mars Sun Jupiter Saturn Uranus Neptune"

# กูเขียนอะไรวะไอเหี้ย

if planets == "Sun":
    print("Hot:")
    print("Cool:")
else:
    L = ""
    R = ""
    if planets.startswith("Sun "):
        R = planets[4:]
    elif planets.endswith(" Sun"):
        L = planets[:-4]
    else:
        i = planets.find(" Sun ")
        L = planets[:i]
        R = planets[i + 5:]

    # print(f"L: '{L}' R: '{R}'")

    # Find the last space in L and the first space in R
    last_space_L = L.rfind(" ")
    first_space_R = R.find(" ")

    # If there are no spaces, then it should be exactly 3 planets
    # e.g. "A Sun B" -> 'A', 'B' -> no spaces
    #      "A Sun" -> 'A' -> no spaces
    #      "Sun B" -> 'B' -> no spaces
    if last_space_L == -1 and first_space_R == -1:
        if L and R:
            print("Hot:", L.strip() + " " + R.strip())
            print("Cool:", L.strip() + " " + R.strip())
        elif L:
            print("Hot:", L.strip())
            print("Cool:", L.strip())
        else: # R
            print("Hot:", R.strip())
            print("Cool:", R.strip())
    else:
        if last_space_L == -1: # no space in left
            # print("no space in left")
            hot = L.strip() + " " + R[:first_space_R].strip()
            last_space_R = R.rfind(" ")
            cool = R[last_space_R:].strip()
        elif first_space_R == -1: # no space in right
            # print("no space in right")
            hot = L[last_space_L:].strip() + " " + R
            first_space_L = L.find(" ")
            cool = L[:first_space_L].strip()
        else:
            hot = L[last_space_L:].strip() + " " + R[:first_space_R].strip()
            first_space_L = L.find(" ")
            last_space_R = R.rfind(" ")
            before_space_count = L.count(" ")
            after_space_count = R.count(" ")
            if before_space_count == after_space_count:
                cool = L[:first_space_L].strip()+" "+R[last_space_R:].strip()
            elif before_space_count < after_space_count:
                cool = R[last_space_R:].strip()
            else:
                cool = L[:first_space_L]
        print("Hot:", hot.strip())
        print("Cool:", cool.strip())
