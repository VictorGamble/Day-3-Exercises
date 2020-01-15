#prompt a user for a number
#compare that # to a predetermine #
#if true print Mind read
#else prinit Not a mind reader


userInput = int(input("What number am i thinking of: "))
MAGICNUMBER = 9


if userInput == MAGICNUMBER:
    print("Mind Reader")
else:
    print("Not a mind reader")
