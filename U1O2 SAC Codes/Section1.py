colSel1 = 0 #initialise column selector for list row 1
colSel2 = 0 #initialise column selector for list row 2
colSel3 = 0 #initialise column selector for list row 3

# opting for a list to store the grid numbers
# alternatively, this could be done by assigning 9 different variables
list1 = []
list2 = []
list3 = []

sum_row1 = 0
sum_row2 = 0
sum_row3 = 0

for i in range(9):
    userNum = input("Input a number between 1 and 9 inclusive: ")
    # check that input is valid
    if (userNum!="1" and userNum!="2" and userNum!="3" and
        userNum!="4" and userNum!="5" and userNum!="6" and
        userNum!="7" and userNum!="8" and userNum!="9"):
        print("Invalid input!")
        exit(0)
    else:
        listSel = int(input("Which row would you like this number to be in (1 - default, 2 or 3): "))
        # select the appropriate list (row 1, row 2 or row 3).  default is row 1

        if (listSel==2):
            print("The first available column in row 2 is column",colSel2)
            list2.append(userNum)
            colSel2 += 1
            sum_row2 += int(userNum)
        elif (listSel==3):
            print("The first available column in row 3 is column",colSel3)
            list3.append(userNum)
            colSel3 += 1
            sum_row3 += int(userNum)
        else:
            print("The first available column in row 1 is column",colSel1)
            list1.append(userNum)
            colSel1 += 1
            sum_row1 += int(userNum)

print("Your grid is:")
# print first row including sum
for i in range(3):
    print(list1[i],end="\t")
print(sum_row1)
# print second row including sum
for i in range(3):
    print(list2[i],end="\t")
print(sum_row2)
# print third row including sum
for i in range(3):
    print(list3[i],end="\t")
print(sum_row3)