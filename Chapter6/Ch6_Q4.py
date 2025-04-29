myString = input("Please type in a word: ")
vowelCount = 0
for i in range(len(myString)):
    if(myString[i].lower() == 'a' or myString[i].lower() == 'e' or myString[i].lower() == 'i' or myString[i].lower() == 'o' or myString[i].lower() == 'u'):
        vowelCount += 1
if (vowelCount > 0):
    print("The word contains vowels.")
else:
    print("The word does not contain vowels.")