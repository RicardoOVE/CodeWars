''' Write a function that accepts "fight" string consists of only small letters and return 
who wins the fight. When the left side wins return "Left side wins!", when the right side wins 
return "Right side wins!", in other case return "Let's fight again!".'''

def alphabet_war(fight):

    both_sides = {"w":4, "p":3, "b":2, "s":1, "t":0, "m":-4, "q":-3, "d":-2, "z":-1, "j":0}

    fight_score = 0

    for letter in fight:
        if letter in both_sides.values():
            fight_score += both_sides.get(letter)
#        if letter == "t":
        

    if fight_score == 0:
        results = "Let's fight again!"
    elif fight_score > 0:
        results = "Left side wins!"
    else:
        results = "Right side wins!"

    return fight_score, results

fight = "tzj"
print(alphabet_war(fight))