my_string = input("Type in a string: ")
new_string = ""
for i in range(len(my_string)):
    if i == 1:
        new_string += '*'
    else:
        new_string += my_string[i]
new_string += '!!!'
print(new_string)