def cubes_print(startnum, endnum):
    cubes_list = []
    message = "The cubes of numbers are: "
    for i in range(startnum,endnum):
        cubes_list.append(i**2)
        message += str(i**2)
        message += ", "
    message += str(endnum**2)
    return message

startnum = int(input("Print the starting number: "))
endnum = int(input("Print the ending number: "))
print(cubes_print(startnum,endnum))