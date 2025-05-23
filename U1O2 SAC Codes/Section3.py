ready = input("Would you like to start creating the list? ")
mylist = []

def calc_series(startnum):
    currnumber = startnum
    count = 0
    message = "Here are the numbers in the series: "

    for i in range(11):
        sum = currnumber + count
        message += str(sum) + " "
        currnumber = sum
        count += 1
        
    return message

if (ready == "Y" or ready == "y" or ready == "Yes" or ready == "YES" or ready == "yes"):
    # start 
    startnum = int(input("What is your starting number? "))
    print("Your starting number is",startnum)
    mylist = []
    print(calc_series(startnum))

else:
    print("Goodbye!")