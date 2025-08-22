"""asdasdasdasd"""
CH = "H"
NUM = 4567
ch_input = input()
num_input = int(input())

if ch_input == CH and num_input == NUM:
    print("safe unlocked")
elif ch_input == CH:
    print("safe locked - change digit")
elif num_input == NUM:
    print("safe locked - change char")
else:
    print("safe locked")
