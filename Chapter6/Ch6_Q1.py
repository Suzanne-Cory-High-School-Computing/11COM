myString = input("Type in a string: ")
# 1a
myStringLength = len(myString)
print("The number of characters in the string is",myStringLength)
# 1b
print("The string repeated 10 times is:")
for i in range(10):
    print(myString,end=" ")
# 1c
print("\nThe first character of the string is",myString[0])
# 1d
print("The first three characters of the string are",myString[:3])
# 1e
print("The last three characters of the string are",myString[-3:])
# 1f
print("The string backwards is",myString[::-1])
# 1g
if(len(myString)>=7):
    print("The seventh character of the string is",myString[6])
else:
    print("The string length is less than 7 characters.")
# 1h
print("The string without the first and last characters is",myString[1:len(myString)-1:])
# 1i
print("The string in all caps is",myString.upper())
# 1j
print("The string with every a replaced by an e is:")
for i in range(len(myString)):
    if(myString[i]=="a"):
        print("e",end="")
    else:
        print(myString[i],end="")
print("")
# 1k
print("The string with every letter replaced by a space is",myStringLength*" ")