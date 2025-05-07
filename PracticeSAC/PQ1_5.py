usernumber = int(input("Enter a number: "))

if (usernumber%10 == 0): # remainder of division by ten is nothing, therefore divisible
    print("a. The number",usernumber,"is divisible by 10.")
else:
    print("a. The number",usernumber,"is not divisible by 10.")

if (usernumber%2 == 0): # remainder of division by two is nothing, therefore divisible
    print("b. The number",usernumber,"is divisible by 2.")
else:
    print("b. The number",usernumber,"is not divisible by 2.")

if (usernumber%3 == 0): # remainder of division by three is nothing, therefore divisible
    print("c. The number",usernumber,"is divisible by 3.")
else:
    print("c. The number",usernumber,"is not divisible by 3.")

if (usernumber%4 == 0): # remainder of division by four is nothing, therefore divisible
    print("d. The number",usernumber,"is divisible by 4.")
else:
    print("d. The number",usernumber,"is not divisible by 4.")

# identifying the factors of the number
# there is no requirement for unique factors or ordered factors
# therefore we can just print factors as we go
# otherwise we can append to a list
# first print 1 and itself as factors
print("e. The factors of",usernumber,"are: 1",usernumber,end=" ")
for i in range(2,usernumber):
    if(usernumber%i==0):
        print(usernumber,end=" ")
        print(int(usernumber/i),end=" ")
print("")

usernumbersquare = usernumber**2 # get this value first because this is used in question h
print("f. The square of the number",usernumber,"is",usernumbersquare)
usernumbernext = usernumber + 1
usernumbersum = usernumber + usernumbernext # get this value first because this is used in question h
print("g. The sum of the number",usernumber,"and the number after it is",usernumbersum)
print("h. the sum of f and g are",usernumbersquare+usernumbersum)