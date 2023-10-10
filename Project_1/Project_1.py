print("Enter a name: ")
name = input()
print("Welcome to the ChatGPT Adventure game")
Lives = 3
print("your eyes open. All you see is the black, there is a diary with vines coming off of it, the iron door is shut")
print(f"What are you going to do next {name}?")
option = ""
while option != "open diary":
    option = input()
    if option == "open diary":
        print("the vines prick you, there must be a way to get rid of them.")
    elif option == "open door":
        print("Maybe there is a key admist this darkness.")
        print(Lives)
    else:
        print("you feel nothing.")
        Lives -= 1
        break

print("There is a bright light shining off of a mysterious object")
anwser = ""
while anwser != "search for object":
    anwser = input()
    if anwser == "search for object":
            print("you find a axe!")
    else:
        print("There is nothing there.")
        Lives -= 1
        print(Lives)
        break
print ("You have found an axe what do you want to do with it.")
anwser_2 = ""
while anwser_2 != "find diary":
    anwser_2 = input()
    if anwser_2 == "find diary":
        print("the book can now be open.")
    else:
        print("what about the diary?")
        break
        Lives -= 1 
print("The diary is open, there is something in it, what would you like to do?")
anwser_3 = ""
while anwser_3 != "look through diary":
    anwser_3 = input()
    if anwser_3 == "look through diary":
        print("you found a key")
    else:
        print("Try again")
        Lives -= 1
    print("The key seems to unlock, an iron door")
    break
    print("What are you going to do next?")
anwser_4 = ""
while anwser_4 != "open the iron door":
    anwser_4 = ""
    if anwser_4 == "open the iron door":
        print("The key fit! the iron door is slowly opening.")
    else:
        print("seems like it can fit in the iron door")
    print("the door has opened")
    break
    print("The door seems to lead into another room.")
    print("there is a shadow. A shadow that covers the whole room. the only option is to fight it.")
monster_hp = 50
while monster_hp >= 1:
    print("What would you like to do? A for attack")
    option = input().upper()
    if option == "A":
        monster_hp -= 10
        print ("Monster took 10 damage")
    else:
        print("Not an option")
    print(f"Monster has collapsed and fades into dust {monster_hp} left")
print("You Won!!!")
print("you search around the monsters body, you seem to find the a key")
print("However, there is a gape between you and the door, what are you going to do?")
anwser_5 = ""
while anwser_5 != "Jump":
    if anwser_5 == "Jump":
        print("you successfully made it to the otherside")
    else:
        print("try again")
        break
    print("the door seems to lead to another room, one that is filled with flames, yet there seems to be a pattern on the roof")
anwser_6 = ""
print("What are you going to do next?")
while anwser_6 != "follow the pattern":
    if anwser_6 == "follow the pattern":
        print("the pattern sucessfully leads you to the door.")
    else:
        print("the flames pushes you back.")
        break
    print("The door leads you outside the cabin, you are surrounded by a furocious blizzard, you see a faint light in the distance")
    print(f"What are you going to do {name}")
anwser_7 = ""
while anwser_7 != "search for the light":
    if anwser == "search for the light":
        print("you have made it, you are no longer at mercy of this mysterious cabin. Congratulations!")
    else:
        print("the light is getting more and more faint.")
        break