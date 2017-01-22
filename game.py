from random import randint

# Welcome message
print ("\nWelcome to Magic 8 Ball!")

# Start "keep_playing" flag as True
keep_playing = True

# Dictionary of answers based on random_number
answer = {
    1: "\n*** It is certain ***",
    2: "\n*** It is decidedly so ***",
    3: "\n*** Without a doubt ***",
    4: "\n*** Yes, definitely ***",
    5: "\n*** You may rely on it ***",
    6: "\n*** As I see it, yes ***",
    7: "\n*** Most likely ***",
    8: "\n*** Outlook good ***",
    9: "\n*** Yes ***",
    10: "\n*** Signs point to yes ***",
    11: "\n*** Reply hazy try again ***",
    12: "\n*** Ask again later ***",
    13: "\n*** Better not tell you now ***",
    14: "\n*** Cannot predict now ***",
    15: "\n*** Concentrate and ask again ***",
    16: "\n*** Don't count on it ***",
    17: "\n*** My reply is no ***",
    18: "\n*** My sources say no ***",
    19: "\n*** Outlook not so good ***",
    20: "\n*** Very doubtful ***",
    21: "\n*** No ***",
    # The following are funny answers, adjust random_number range to use / not use
    22: "\n*** HELP ME, I'M TRAPPED IN THIS 8 BALL! ***",
    23: "\n*** Warning, I don't know what I'm talking about! ***",
    24: "\n*** Why are you asking me? I just give you random replies back! ***",
    25: "\n*** Shake and ask again... Don't actually shake, this is a computer! ***",
    26: "\n*** Just Google it! ***",
    27: "\n*** I dunno ***"
}

# The game
while keep_playing:
    # Ask for a question
    question = input("\nAsk a question: ")

    # If question is blank, ask again
    while question == "":
        print ("\nYou didn't ask anything")
        question = input("Ask a question: ")

    # Get a random number that will be used for the magic answer
    random_number = randint(1,27)

    # Call dictionary value to give magic answer
    print (answer[random_number])

    # Ask if user would like to play again
    play_again = input("Would you like to ask another question? (y/n) ")

    # Change "keep_playing" flag to end play if user didn't say "y" or "yes"
    if play_again.lower() != "y" and play_again.lower() != "yes":
        keep_playing = False
