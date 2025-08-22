"""asdasdadasd"""
color1 = input()
color2 = input()

if color1 == color2 and (color1 in ("Red", "Blue", "Yellow")):
    print(color1)
elif (color1 == "Red" and color2 == "Yellow") or (color2 == "Red" and color1 == "Yellow"):
    print("Orange")
elif (color1 == "Red" and color2 == "Blue") or (color2 == "Red" and color1 == "Blue"):
    print("Violet")
elif (color1 == "Yellow" and color2 == "Blue") or (color2 == "Yellow" and color1 == "Blue"):
    print("Green")
else:
    print("Error")
