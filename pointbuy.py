total = 27 # what you start off with
attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
scores = [8, 8, 8, 8, 8, 8] # baseline, minimum
costs = [0, 0, 0, 0, 0, 0]

# to turn ability scores into modifiers
def mod(ability):
    if ability in [8, 9]: return -1
    elif ability in [10, 11]: return 0
    elif ability in [12, 13]: return 1
    elif ability in [14, 15]: return 2
      
# to print out your stats in a table
def display(scores, attributes):
    # the heading
    print(format("Attribute", "16s"), format("Ability Score", "<18s"), \
          format("Modifier", "<13s"), "Point Cost")
    print("------------------------------------------------------------")
    # using some indexed lists to accomplish the task
    for attribute in attributes:
        score = scores[attributes.index(attribute)]
        cost = costs[attributes.index(attribute)]
        print(format(attribute, "16s"),\
              format(score, "<18d"), format(mod(score), "<13d"), cost)

# there was probably a better way to do this... self explanatory though
def attr(att):
    if att.lower() == "str":
        return "Strength"
    elif att.lower() == "dex":
        return "Dexterity"
    elif att.lower() == "con":
        return "Constitution"
    elif att.lower() == "int":
        return "Intelligence"
    elif att.lower() == "wis":
        return "Wisdom"
    elif att.lower() == "cha":
        return "Charisma"
    
# the main program!
while True:
    menu = input("(d)isplay, (c)hange, (r)eset, or e(x)it >> ")

    if menu.lower() == "d":
        print()
        display(scores, attributes)
        print(">> You have", total, "points remaining!\n")
        continue

    elif menu.lower() == "c":
        
        while True:
            print()
            att = input("What attribute would you like to change?\n(STR, DEX, CON, INT, WIS, CHA) >> ")
            if att.lower() not in ["str", "dex", "con", "int", "wis", "cha"]:
                print("Not a valid attribute, try again!")
                continue
            else:
                break
            
        while True:
            print()
            change = input("How many points would you like to add/subtract? (i.e. +3, -2) >> ")
            edit = change[0]
            num = int(change[1])
            if edit == "+" and (scores[attributes.index(attr(att))] + num <= 15):
                scores[attributes.index(attr(att))] += num
                costs[attributes.index(attr(att))] += num
                total -= num
                print(">> Your ", attr(att), " score is now ", scores[attributes.index(attr(att))], "!", sep="", end="\n\n")
                break
            elif edit == "+" and (scores[attributes.index(attr(att))] + num > 15):
                print(">> You can only add up to a maximum of 15 points! Try again!")
                continue
            elif edit == "-" and (scores[attributes.index(attr(att))] - num >= 8):
                scores[attributes.index(attr(att))] -= num
                costs[attributes.index(attr(att))] -= num
                total += num
                print(">> Your ", attr(att), " score is now ", scores[attributes.index(attr(att))], "!", sep="", end="\n\n")
                break
            elif edit == "-" and (scores[attributes.index(attr(att))] - num < 8):
                print(">> You can only subtract to a minimum of 8 points! Try again!")
                continue

    elif menu.lower() == "r":
        total = 27
        attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        scores = [8, 8, 8, 8, 8, 8] 
        costs = [0, 0, 0, 0, 0, 0]
        print("\n>> Your character has been reset!\n")
    

    elif menu.lower() == "x":
        print("\nHere are your final stats:")
        display(scores, attributes)
        print(">> Happy playing!")
        break
