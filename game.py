from random import randint

# Welcome message
print ("\nWelcome to Magic 8 Ball!")

# Start "keep_playing" flag as True
keep_playing = True

# Dictionary of answers based on random_number
answer = {
    1: "\n*** It is certain ***",
    2: "\n*** Without a doubt ***",
    3: "\n*** Yes, definitely ***",
    4: "\n*** You may rely on it ***",
    5: "\n*** Most likely ***",
    6: "\n*** Signs point to yes ***",
    7: "\n*** Yes ***",
    8: "\n*** Cannot predict now ***",
    9: "\n*** Ask again later ***",
    10: "\n*** Better not tell you now ***",
    11: "\n*** Don't count on it ***",
    12: "\n*** My sources say no ***",
    13: "\n*** Outlook not so good ***",
    14: "\n*** Very doubtful ***"
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
    random_number = randint(1,14)

    # Call dictionary value to give magic answer
    print (answer[random_number])

    # Ask if user would like to play again
    play_again = input("Would you like to ask another question? (y/n) ")

    # Change "keep_playing" flag to end play if user didn't say "y" or "yes"
    if play_again.lower() != "y" and play_again.lower() != "yes":
        keep_playing = False
