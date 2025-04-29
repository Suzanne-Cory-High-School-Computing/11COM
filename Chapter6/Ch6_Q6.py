s = input("Type in a string: ")
s.lower()
newString = ""
for i in range(len(s)):
    if s[i] not in ",.":
        newString += s[i]
print(newString)