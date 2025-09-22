"""a"""
def main():
    """fuck this"""
    DEBUG = True
    def debug(msg):
        if DEBUG:
            print(">>", msg)

    initial = int(input())
    max_rounds = int(input())

    # Properties A-X, -1 for special tiles
    props = [
        -1, # Start
        1000, 1100, 1200, 1300, 1400, 1500, # A-F
        -2, # Jail
        1600, 1700, 1800, 1900, 2000, 2100, # G-L
        -3, # Landmark
        2200, 2300, 2400, 2500, 2600, 2700, # M-R
        -4, # Travel
        2800, 2900, 3000, 3100, 3200, 3300, # S-X
    ]
    p1 = {
        "money": initial,
        # 0     = Start
        # 1-6   = Properties A-F
        # 7     = Jail (stop)
        # 8-13  = Properties G-L
        # 14    = Landmark
        # 15-20 = Properties M-R
        # 21    = Travel
        # 22-27 = Properties S-X
        "pos": 0,
        "jailed": False,
        "owned": [], # List of (Index into props, Multiplier)

        "moved": False,
    }
    p2 = {
        "money": initial,
        "pos": 0,
        "jailed": False,
        "owned": [],
        "moved": False,
    }

    rounds = 0
    while True:
        xs = input().split()
        if len(xs) == 0:
            pass
        player = xs[0]
        act = xs[1:]

        def letter_to_prop_idx(c):
            """a"""
            return ord(c) - ord("A") + 1 if c <= "F" else\
                   ord(c) - ord("G") + 8 if c <= "L" else\
                   ord(c) - ord("M") + 15 if c <= "R" else\
                   ord(c) - ord("S") + 22

        def when_normal(p, rolled):
            """a"""
            player = p1 if p == "P1" else p2
            other_player = p2 if p == "P1" else p1
            # Move player
            player["pos"] += rolled
            if player["pos"] > 27:
                player["pos"]   -= 28
                player["money"] += 0.5 * initial
                debug(f"{p} passed Start, +{0.5 * initial}")

            debug(f"{p} rolled {rolled}, now at {player['pos']} [{props[player['pos']]}]")
            player["moved"] = True

            # Land on property
            if props[player["pos"]] > 0:
                # If the property has not been bought by either player
                if  all(player["pos"] != owned[0] for owned in player["owned"])\
                and all(player["pos"] != owned[0] for owned in other_player["owned"]):
                    # Buy property if have enough money
                    if player["money"] >= props[player["pos"]]:
                        player["money"] -= 0.7 * props[player["pos"]]
                        player["owned"].append([player["pos"], 1])
                        debug(f"{p} bought property {player['pos']} for {props[player['pos']]}")
                    # Else, nothing happens...
                else:
                    # If owned by other player, pay the rent
                    # If we owned it, nothing happens
                    for owned in other_player["owned"]:
                        if owned[0] == player["pos"]:
                            rent = owned[1] * 0.7 * props[player["pos"]]
                            player["money"] -= rent
                            other_player["money"] += rent
                            debug(f"{p} paid rent {rent})")
                            break
            # Jail
            elif props[player["pos"]] == -2:
                player["jailed"] = True
                debug(f"{p} is now in Jail")
            # Landmark
            elif props[player["pos"]] == -3:
                pass # Handle outside
            # Travel
            elif props[player["pos"]] == -4:
                pass # Handle outside

        # Dice roll if all is number (e.g. "5 5", "3 4")
        if all(map(lambda x: x.isdigit(), act)):
            rolled = sum(map(int, act))
            when_normal(player, rolled)
        elif " ".join(act) == "pay to leave":
            if player == "P1":
                p1["money"] -= 0.1 * p1["money"]
                p1["jailed"] = False
            else:
                p2["money"] -= 0.1 * p2["money"]
                p2["jailed"] = False
            debug(f"{player} now has {p1['money'] if player == 'P1' else p2['money']}")
        elif act[1] == "x": # Landmark "prop x 2"
            prop = letter_to_prop_idx(act[0])
            multiplier = int(act[2])
            player_obj = p1 if player == "P1" else p2
            for owned in player_obj["owned"]:
                if owned[0] == prop:
                    owned[1] = multiplier
                    debug(f"{player} upgraded property {prop} to x{multiplier}")
                    break
        elif act[0] == "Go": # Travel "Go A"
            where = letter_to_prop_idx(act[1])
            when_normal(player, (where - (p1 if player == "P1" else p2)["pos"]) % 28)
            # player_obj = p1 if player == "P1" else p2
            # # If passing Start
            # if where <= player_obj["pos"]:
            #     player_obj["money"] += 0.5 * initial
            #     debug(f"{player} passed Start, +{0.5 * initial}")
            # player_obj["pos"] = where
            # player_obj["moved"] = True
            # debug(f"{player} travelled to {where}")

        # If either play ran out of money, end game
        if p1["money"] <= 0 or p2["money"] <= 0:
            debug(f"Game over: {'P1' if p1['money'] <= 0 else 'P2'} ran out of money")
            break

        if p1["moved"] and p2["moved"]:
            rounds += 1
            p1["moved"] = False
            p2["moved"] = False
            debug(f"P1: {p1['money']}, P2: {p2['money']}")
            if rounds >= max_rounds:
                debug("Game over: Reached max rounds")
                break

main()
