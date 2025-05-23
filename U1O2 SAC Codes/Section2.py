from random import randint
ready = input("Would you like to start playing? ")
comparestring = "begin"

if (ready == "Y" or ready == "y" or ready == "Yes" or ready == "YES" or ready == "yes"):
    # start playing
    print("Your starting word is begin.")
    totalscore = 0
    for round in range(10):
        currscore = 0
        print("Round",round+1)
        print("Here are your 10 random letters: ")
        for i in range(10):
            number = randint(0,25)
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            #print("number",number,"letter",alphabet[number])
            #print(alphabet[number])
            comparestring += alphabet[number]
        print(comparestring)
        currword = input("Type in a word using any of the letters provided above: ")
        invalidcount = 0
        for i in range(len(currword)):
            if currword[i] not in comparestring:
                invalidcount += 1
        if (invalidcount > 0):
            currscore = 0
        else:
            currscore = len(currword)
        print("Your score for this round is",currscore)
        totalscore += currscore
        comparestring = "begin"
    print("Your total score is",totalscore)
else:
    print("Goodbye!")