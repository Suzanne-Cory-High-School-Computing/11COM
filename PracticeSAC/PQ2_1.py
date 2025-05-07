name = input("What is your name? ")
print("Hello",name,end=" ")
ready = input("are you ready to begin? ")

readylower = ready.lower()

if (readylower == "yes"): #accept all cases, YES, yes, yEs, Yes
    # if-elif-else chain
    username = input("Type in a person's name: ")
    userage = input("Type in a person's age: ")
    while (username != ""):
        if (int(userage) < 0):
            print("Invalid age.")
            exit(0)
        else:
            countvowel = 0
            for i in range(len(username)):
                if username[i] in 'aeiou': # count the number of vowels in the name
                    countvowel += 1
            print("The name",username,"has",countvowel,"vowels.")
            if (int(userage) < 2): # between 0 and 2 years old
                print(username,"is a baby.")
            elif (int(userage) < 4):
                print(username,"is a toddler.")
            elif (int(userage) < 13):
                print(username,"is a child.")
            elif (int(userage) < 20):
                print(username,"is a teenager.")
            elif (int(userage) >=65):
                print(username,"is an elder.")
            else:
                print(username,"is an adult.")
        username = input("Type in a person's name: ")
        userage = input("Type in a person's age: ")
else: #exit the program because user is not ready
    print("Goodbye!")