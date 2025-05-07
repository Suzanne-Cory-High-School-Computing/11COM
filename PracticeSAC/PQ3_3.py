cube_list = []
def number_cubes(startnum,endnum):
    for i in range(startnum,endnum+1):
        cube_list.append(i**2)

def recursive_print(list_name):
    message = "The cubes of numbers are: "
    for i in range(len(list_name)-1):
        message += str(list_name[i])
        message += ", "
    message += str(list_name[-1])
    return message

number_cubes(3,11)
print(recursive_print(cube_list))