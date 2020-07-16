import time
import random

weapons = ["Magical Sword of Ogoroth", "TNT", " Sharp Knife", "Golden Ax"]
creatures = ["Monster", "Gozilla", "Gorgon", "Pirate"]
weapon = random.choice(weapons)
creature = random.choice(creatures)
got_weapon = False


def print_pause(message_to_player):
    print(message_to_player)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a pirate is somewhere around here, and has "
                "been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")


def valid_input(prompt, options):
    while True:
        response = input(prompt)
        for option in options:
            if response == option:
                return response
        print_pause("Sorry I don't understand.")


def play_again():
    response2 = valid_input("Would you like to play again? (y/n)", ["y", "n"])
    if response2 == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    else:
        print_pause("Thanks for playing! See you next time.")


def fight():
    if got_weapon:
        print_pause("As the dragon moves to attack, you unsheath your new "
                    "sword.\n"
                    "The Sword of Ogoroth shines brightly in your hand as you "
                    "brace yourself for the attack.\n"
                    "But the dragon takes one look at your shiny new toy and "
                    "runs away!\n"
                    "You have rid the town of the dragon. You are victorious!")
        play_again()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the pirate.")
        print_pause("You have been defeated!")
        play_again()


def field():
    print_pause("You run back into the field. Luckily, you don't seem to have "
                "been followed.")
    # go back to step1
    house_or_cave()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a "
                + creature + ".")
    print_pause("Eep! This is the " + creature + "'s house!\n")
    print_pause("The " + creature + " attacks you!\n")
    if not got_weapon:
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.")

    response1 = valid_input("Would you like to (1) fight or (2) run away?",
                            ["1", "2"])
    if response1 == "1":
        fight()
    # choose "run away".
    else:
        field()


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the " + weapon + "!")
    print_pause("You discard your silly old dagger and take the sword "
                "with you.")
    print_pause("You walk back out to the field.")

    while True:
        response2 = valid_input("Enter 1 to knock on the door of the house.\n"
                                "Enter 2 to peer into the cave.\n"
                                "What would you like to do?\n"
                                "(Please enter 1 or 2.)", ["1", "2"])
        if response2 == "1":
            print_pause("You approach the door of the house.")
            print_pause("You are about to knock when the door opens and out "
                        "steps a " + creature + ".")
            print_pause("Eep! This is the " + creature + "'s house!")
            print_pause("The " + creature + " attacks you!")

            response3 = valid_input("Would you like to (1) fight or (2) run "
                                    "away?", ["1", "2"])
            if response3 == "1":
                print_pause("As the " + creature + " moves to attack, you "
                            "unsheath your new sword.")
                print_pause("The " + weapon + " shines brightly in your "
                            "hand as you brace yourself for the attack.")
                print_pause("But the " + creature + " takes one look "
                            "at your shiny new toy and runs away!")
                print_pause("You have rid the town of the " + creature +
                            ". You are victorious!")
                play_again()
            # choose run away
            else:
                print_pause("You run back into the field. Luckily, you don't "
                            "seem to have been followed.")
                house_or_cave()
            break
        else:
            print_pause("You peer cautiously into the cave.\n"
                        "You've been here before, and gottten all the "
                        "good stuff.\n"
                        "It's just an empty cave now.\n"
                        "You walk back out to the field")


def house_or_cave():
    response = valid_input("Enter 1 to knock on the door of the house.\n"
                           "Enter 2 to peer into the cave.\n"
                           "What would you like to do?\n"
                           "(Please enter 1 or 2.)", ["1", "2"])
    if response == "1":
        house()

    elif response == "2":
        cave()


def play_game():
    intro()
    house_or_cave()


play_game()
