from random import choice
from time import sleep

# Welcome message
print ("\nWelcome to Magic 8 Ball!")

# Start "keep_playing" flag as True
keep_playing = True

# List of answers
answer = [
    "*** It is certain ***",
    "*** It is decidedly so ***",
    "*** Without a doubt ***",
    "*** Yes, definitely ***",
    "*** You may rely on it ***",
    "*** As I see it, yes ***",
    "*** Most likely ***",
    "*** Outlook good ***",
    "*** Yes ***",
    "*** Signs point to yes ***",
    "*** Reply hazy try again ***",
    "*** Ask again later ***",
    "*** Better not tell you now ***",
    "*** Cannot predict now ***",
    "*** Concentrate and ask again ***",
    "*** Don't count on it ***",
    "*** My reply is no ***",
    "*** My sources say no ***",
    "*** Outlook not so good ***",
    "*** Very doubtful ***",
    "*** No ***",
    # The following are funny answers, comment them out if don't want to use
    "*** HELP ME, I'M TRAPPED IN THIS 8 BALL! ***",
    "*** Warning, I don't know what I'm talking about! ***",
    "*** Why are you asking me? I just give you random replies back! ***",
    "*** Shake and ask again... Don't actually shake, this is a computer! ***",
    "*** Just Google it! ***",
    "*** I dunno ***",
    "*** Just get lost! ***",
    "*** Please stop asking questions, you've asked enough! ***"
]

# The game
while keep_playing:
    # Ask for a question and verify not blank
    question = input("\nAsk a question: ")
    while question == "":
        print ("\nYou didn't ask anything")
        question = input("Ask a question: ")

    # Shake, then print a random answer from answer list
    print("\nShaking...")
    sleep(2)
    print (choice(answer))

    # Pause 3 seconds, then ask if user would like to play again
    sleep(3)
    play_again = input("\nWould you like to ask another question? (y/n) ")

    # Change "keep_playing" flag to end play if user didn't say "y" or "yes"
    if play_again.lower() != "y" and play_again.lower() != "yes":
        keep_playing = False
