choice = str(input("What kind of rental car would you like? "))
# accept any answer as long as it contains only letters of the alphabet
# another option would be to create a list and only accept answers from the list
choicelower = choice.lower() # lowercase letters to check easily
print (choicelower)
invalidcount = 0 # set initial invalid count to 0
for i in range(len(choicelower)):
    if choicelower[i] not in 'abcdefghijklmnopqrstuvwxyz':
        invalidcount += 1
# if any character is invalid, print an error message
if invalidcount > 0:
    print("Invalid input.  Please enter only letters.")
else:
# if all characters are letters, print the rental car they like with a message
    print("Let me see if I can find you a",choice)