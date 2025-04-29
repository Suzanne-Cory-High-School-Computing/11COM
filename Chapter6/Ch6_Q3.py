myFormula = input("Please type in a formula: ")
countOpen = 0
countClose = 0
for i in range(len(myFormula)):
    if(myFormula[i]=="("):
        countOpen += 1
    elif(myFormula[i]==")"):
        countClose += 1
if countOpen != countClose:
    print("The number of open parentheses do not match the number of close parentheses.")
else:
    print("The number of open and close parentheses match.")