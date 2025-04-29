myString = input("Type in a string: ")
spaceCount = 0
for i in range(len(myString)):
    if(myString[i]==" "):
        spaceCount += 1
print("The estimated number of words in this string is",spaceCount+1)