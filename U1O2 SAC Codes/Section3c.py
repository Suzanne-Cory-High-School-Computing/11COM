ready = input("Would you like to start creating the list? ")
mylist = []

if (ready == "Y" or ready == "y" or ready == "Yes" or ready == "YES" or ready == "yes"):
    # start 
    print("Your starting number is 1.")
    currnumber = 1
    count = 0

    for i in range(11):
        sum = currnumber + count
        mylist.append(sum)
        currnumber = sum
        count += 1

    print("Here are the numbers in the series: ")
    print(mylist)
else:
    print("Goodbye!")