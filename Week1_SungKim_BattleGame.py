'''
workshop week 1 - Battlegame
By Sung Kim
08/06/2022
'''
import sys

WIZARD = "Wizard"
ELF = "Elf"
HUMAN = "Human"
ORC = "Orc"

WIZARD_HP = 70
ELF_HP = 100
HUMAN_HP = 150
ORC_HP = 200

WIZARD_DAMAGE = 150
ELF_DAMAGE = 100
HUMAN_DAMAGE = 20
ORC_DAMAGE = 50

DRAGON_HP = 300
DRAGON_DAMAGE = 50

print("welcome to the Battle Game!")

while True:
    USER_INPUT = input("Do you want to play this game? Yes or No? ")
    if USER_INPUT == "No".lower():
        print("Goodbye!")
        sys.exit(-1)
    print("Let's go!")

    while True:
        print("1) " + WIZARD)
        print("2) " + ELF)
        print("3) " + HUMAN)
        print("4) " + ORC)
        character = input("Choose your character: ")
        if character == WIZARD.lower():
            MY_CHARACTER = WIZARD
            MY_HP = WIZARD_HP
            MY_DAMAGE = WIZARD_DAMAGE
            break
        if character == ELF.lower():
            MY_CHARACTER = ELF
            MY_HP = ELF_HP
            MY_DAMAGE = ELF_DAMAGE
            break
        if character == HUMAN.lower():
            MY_CHARACTER = HUMAN
            MY_HP = HUMAN_HP
            MY_DAMAGE = HUMAN_DAMAGE
            break
        if character == ORC.lower():
            MY_CHARACTER = ORC
            MY_HP = ORC_HP
            MY_DAMAGE = ORC_DAMAGE
            break
        print("Unknown character")
    print("You have chosen the character #", character)
    print("Character:", MY_CHARACTER)
    print("Health:", MY_HP)
    print("Damage:", MY_DAMAGE, "\n")

    while True:
        DRAGON_HP = DRAGON_HP - MY_DAMAGE
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now:", DRAGON_HP, "\n")
        if DRAGON_HP <= 0:
            print("The Dragon has lost the battle!\n")
            break
        MY_HP = MY_HP - DRAGON_DAMAGE
        print("The Dragon strikes back at", character + "!")
        print("The", character + "'s hitpoints are now: ", MY_HP, "\n")
        if MY_HP <= 0:
            print("The", character + "has lost the battle!\n")
            break

    while True:
        EXIT_QUESTION = input("Would you like to play again? Yes or No? ")
        print(EXIT_QUESTION)
        if EXIT_QUESTION == "Yes".lower():
            while True:
                print("1) " + WIZARD)
                print("2) " + ELF)
                print("3) " + HUMAN)
                print("4) " + ORC, "\n")
                character = input("Choose your character: ")
                if character == WIZARD.lower():
                    MY_CHARACTER = WIZARD
                    MY_HP = WIZARD_HP
                    MY_DAMAGE = WIZARD_DAMAGE
                    break
                if character == ELF.lower():
                    MY_CHARACTER = ELF
                    MY_HP = ELF_HP
                    MY_DAMAGE = ELF_DAMAGE
                    break
                if character == HUMAN.lower():
                    MY_CHARACTER = HUMAN
                    MY_HP = HUMAN_HP
                    MY_DAMAGE = HUMAN_DAMAGE
                    break
                if character == ORC.lower():
                    MY_CHARACTER = ORC
                    MY_HP = ORC_HP
                    MY_DAMAGE = ORC_DAMAGE
                    break
                print("Unknown character")
            print("You have chosen the character #", character)
            print("Character:", MY_CHARACTER)
            print("Health:", MY_HP)
            print("Damage:", MY_DAMAGE, "\n")

            while True:
                DRAGON_HP = DRAGON_HP - MY_DAMAGE
                print("The", character, "damaged the Dragon!")
                print("The Dragon's hitpoints are now:", DRAGON_HP, "\n")
                if DRAGON_HP <= 0:
                    print("The Dragon has lost the battle!\n")
                    break
                MY_HP = MY_HP - DRAGON_DAMAGE
                print("The Dragon strikes back at", character + "!")
                print("The", character + "'s hitpoints are now: ", MY_HP, "\n")
                if MY_HP <= 0:
                    print("The", character, "has lost the battle!\n")
                    break
        print("Thank you for playing!")
        break
    break
