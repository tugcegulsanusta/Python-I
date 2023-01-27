import time
import random

enemy = ["wicked fairie", "gorgon", "pirate", "troll"]
random_enemy = random.choice(enemy)


def valid_input(prompt, option1, option2):
    while True:
        user_choice = input(prompt)
        if option1 in user_choice:
            break
        elif option2 in user_choice:
            break
    return user_choice


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def play_again():
    responce = valid_input("Would you like to play again? (y/n)", "y", "n")
    if "y" in responce:
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif "n" in responce:
        print_pause("Thanks for playing! See you next time.")


def run(items):
    print_pause(
        "You run back into the field. Luckily, " +
        "you don't seem to have been followed."
    )
    print_pause("")
    house_or_cave(items)


def fight_or_run(items):
    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door opens and out steps a "
        + random_enemy
        + "."
    )
    print_pause("Eep! This is the " + random_enemy + "'s house!")
    print_pause("The wicked " + random_enemy + " attacks you!")
    if "sword" in items:
        responce = valid_input(
            "Would you like to (1) fight or (2) run away?", "1", "2"
        )
        if "1" in responce:
            print_pause(
                "As the "
                + random_enemy
                + " moves to attack, you unsheath your new sword."
            )
            print_pause(
                "The Sword of Ogoroth shines brightly in your hand" +
                " as you brace yourself for the attack."
            )
            print_pause(
                "But the "
                + random_enemy
                + "takes one look at your shiny new toy and runs away!"
            )
            print_pause(
                "You have rid the town of the" + random_enemy +
                ". You are victorious!"
            )
            play_again()
        elif "2" in responce:
            run(items)
    else:
        print_pause(
            "You feel a bit under-prepared for this, " +
            "what with only having a tiny dagger."
        )
        responce = valid_input(
            "Would you like to (1) fight or (2) run away?", "1", "2"
        )
        if "1" in responce:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the " +
                        random_enemy + ".")
            print_pause("You have been defeated!")
            play_again()
        elif "2" in responce:
            run(items)


def house_or_cave(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    responce = valid_input("(Please enter 1 or 2.)", "1", "2")
    if "1" in responce:
        fight_or_run(items)
    elif "2" in responce:
        if "sword" in items:
            print_pause("You peer cautiously into the cave.")
            print_pause(
                "You've been here before, and gotten all the good stuff." +
                "It's just an empty cave now."
            )
            print_pause("You walk back out to the field.")
            house_or_cave(items)
        else:
            print_pause("You peer cautiously into the cave.")
            print_pause("It turns out to be only a very small cave.")
            print_pause("Your eye catches a glint of metal behind a rock.")
            print_pause("You have found the magical Sword of Ogoroth!")
            print_pause(
                "You discard your silly old dagger and" +
                " take the sword with you."
            )
            print_pause("You walk back out to the field.")
            print_pause(" ")
            items.append("sword")
            house_or_cave(items)


def intro():
    print_pause(
        "You find yourself standing in an open field," +
        " filled with grass and yellow wildflowers."
    )
    print_pause(
        "Rumor has it that a"
        + random_enemy
        + "is somewhere around here, " +
        "and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty" +
                " (but not very effective) dagger.")
    print_pause(" ")


def play_game():
    items = []
    intro()
    house_or_cave(items)


play_game()
