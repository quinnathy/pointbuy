total = 27 # what you start off with
attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
scores = [8, 8, 8, 8, 8, 8] # baseline, minimum
costs = [0, 0, 0, 0, 0, 0]

# to turn ability scores into modifiers
def mod(ability):
    return int((ability-10)/2)
      
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

# using a dictionary and .get() to return the value from the key!
def attr(att):
    atts = {"str": "Strength", "dex": "Dexterity", "con": "Constitution",\
            "int": "Intelligence", "wis": "Wisdom", "cha": "Charisma"}
    att = att.lower()
    return atts.get(att)
    
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
            if change == "0":
                print()
                break
            else:
                edit = change[0]
                num = int(change[1])
            if edit == "+" and (scores[attributes.index(attr(att))] + num <= 15) and num <= total:
                scores[attributes.index(attr(att))] += num
                costs[attributes.index(attr(att))] += num
                total -= num
                print(">> Your ", attr(att), " score is now ", scores[attributes.index(attr(att))], "!", sep="")
                print("You have", total, "points left.\n")
                break
            elif edit == "+" and (scores[attributes.index(attr(att))] + num > 15):
                print(">> You can only add up to a maximum of 15 points! Try again!")
                continue
            elif edit == "-" and (scores[attributes.index(attr(att))] - num >= 8):
                scores[attributes.index(attr(att))] -= num
                costs[attributes.index(attr(att))] -= num
                total += num
                print(">> Your ", attr(att), " score is now ", scores[attributes.index(attr(att))], "!", sep="")
                print("You have", total, "points left.\n")
                break
            elif edit == "-" and (scores[attributes.index(attr(att))] - num < 8):
                print(">> You can only subtract to a minimum of 8 points! Try again!")
                continue
            else:
                print("You don't have enough points left for that :( try again!")
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
