numEmail = eval(input("How many email addresses would you like to enter? "))
currEmail = ""
for i in range(numEmail):
    email = input("Enter an email address: ")
    currEmail += email
#    print(currEmail)
profCount = currEmail.count('professor')
#print(profCount)
if (profCount > 0):
    print("There were some professor addresses entered.")
else:
    print("All addresses are student addresses.")