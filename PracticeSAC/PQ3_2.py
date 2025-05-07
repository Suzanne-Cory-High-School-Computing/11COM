list = []
def number_cubes(startnum,endnum):
    for i in range(startnum,endnum+1):
        list.append(i**2)

number_cubes(3,11)
print(list)   