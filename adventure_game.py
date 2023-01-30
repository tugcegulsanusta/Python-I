import time
import random

enemy = ["wicked fairie", "gorgon", "pirate", "troll"]
random_enemy = random.choice(enemy)

sentences_fight_run = ["You approach the door of the house.",
                       "You approach of an old and mysterious house"]
random_fight_run = random.choice(sentences_fight_run)

weapons = ["sword", "pike", "tomahawk", "bayonet"]
random_weapon = random.choice(weapons)

different_ending = [" takes one look at your shiny new toy and runs away!",
                    " starts to fight with you,"
                    + " but it has no chance against you and your new "
                    + random_weapon + "!"]
ending = random.choice(different_ending)


def valid_input(prompt, options):
    while True:
        user_choice = input(prompt)
        if user_choice in options:
            return user_choice
        else:
            print_pause(f'Sorry, the option "{user_choice}" is invalid.'
                        + " Try again!")


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(random.randint(0, 5))


def play_again():
    responce = valid_input("Would you like to play again? (y/n)", ["y", "n"])
    if responce == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif responce == "n":
        print_pause("Thanks for playing! See you next time.")


def run(items):
    print_pause(
        "You run back into the field. Luckily, " +
        "you don't seem to have been followed."
    )
    print_pause("")
    house_or_cave(items)


def fight_or_run(items):
    print_pause(random_fight_run)
    print_pause(
        "You are about to knock when the door opens and out steps a "
        + random_enemy
        + "."
    )
    print_pause("Eep! This is the " + random_enemy + "'s house!")
    print_pause("The wicked " + random_enemy + " attacks you!")
    if random_weapon in items:
        responce = valid_input(
            "Would you like to (1) fight or (2) run away?", ["1", "2"]
        )
        if responce == "1":
            print_pause(
                "As the "
                + random_enemy
                + " moves to attack, you unsheath your new "
                + random_weapon + "."
            )
            print_pause(
                "The " + random_weapon + " shines brightly in your hand" +
                " as you brace yourself for the attack."
            )
            print_pause(random_enemy + ending)
            print_pause(
                "You have rid the town of the " + random_enemy +
                ". You are victorious!"
            )
            play_again()
        elif responce == "2":
            run(items)
    else:
        print_pause(
            "You feel a bit under-prepared for this, " +
            "what with only having a tiny dagger."
        )
        responce = valid_input(
            "Would you like to (1) fight or (2) run away?", ["1", "2"]
        )
        if responce == "1":
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the " +
                        random_enemy + ".")
            print_pause("You have been defeated!")
            play_again()
        elif responce == "2":
            run(items)


def house_or_cave(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    responce = valid_input("(Please enter 1 or 2.)", ["1", "2"])
    if responce == "1":
        fight_or_run(items)
    elif responce == "2":
        if random_weapon in items:
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
            print_pause("You have found the magical " + random_weapon + "!")
            print_pause(
                "You discard your silly old dagger and" +
                " take the "+random_weapon+" with you."
            )
            print_pause("You walk back out to the field.")
            print_pause(" ")
            items.append(random_weapon)
            house_or_cave(items)


def intro():
    print_pause(
        "You find yourself standing in an open field," +
        " filled with grass and yellow wildflowers."
    )
    print_pause(
        "Rumor has it that a "
        + random_enemy
        + " is somewhere around here, " +
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
