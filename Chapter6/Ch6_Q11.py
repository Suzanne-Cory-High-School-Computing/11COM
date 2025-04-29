myWord = input("Enter a word that contains the letter a: ")
location = myWord.index('a')
print(myWord[0:location+1:])
print(myWord[location+1::])