name = input("Enter your name in lowercase: ")
capName = name.upper()
newName = name
newCapName = capName
finalName = ""
for i in range(name.count(' ')):
    spaceIndex = newName.index(' ') + 1
    finalName += newCapName[0]
    finalName += newName[1:spaceIndex:]
    newName = newName[spaceIndex::]
    newCapName = newName.upper()
#    print('spaceIndex',spaceIndex,'newName',newName,'newCapName',newCapName)
finalName += newCapName[0]
finalName += newName[1::]
print(finalName)