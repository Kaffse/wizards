spells = [
        "self",
        "target",
        "fire",
        "shield",
        "heal",
        "ball",
        "beam"
        ]

print ("Welcome to Wizards! You are a Wizard!")
print ("You are standing in an open field. Infront of you is a single training dummy on an iron pole")
print ("You are about 10m away from the dummy.")
print ("\nPlease Type 'sb' to access your spell book")
print ("Please Type 'help' if you want help with the game")

command = input("Please Enter a Command: ")

while (command != "q"):
    if (command == "help"):
        print ("\nWizards is a game in which you use use your typing skills to cast spells and defeat other wizards!")
        print ("Typing speed and skill is important!")
        print ("First, type 'sb' to access your spell book and see what you have avaliable to cast")
        print ("Assuming you are a brand new Wizard from Wizard School, you will only know <STUFF>")
        print ("These can be combined to create awesome spells which do all sorts of cool things, it's up to you to experiment and find combinations that do interesting things!")
        print ("\nAfter looking at your spells next job is to try and cast one. Simply type 'cast' to enter casting mode.")
        print ("In casting mode your keystrokes are timing and any mistakes recorded to judge the final result of your spell")
        print ("Type in a series of spell names from your spell book to create an awesome spell, then press enter to confirm you've finished casting")
        print ("Assuming you managed to successfully cast the spell (anything could happen!) you'll get an output reporting the effects of your spell")
        print ("Assuming you failed, you will also get an output of the spell failure, depending how drastically you failed!")

    if (command == "sb"):
        print ("\nSpells Avaliable:")
        for s in spells:
            print (s + ", ")

    if (command == "q"):
        print ("Thanks for Playing!")
