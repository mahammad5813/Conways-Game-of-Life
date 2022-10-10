from time import sleep
from os import system
import random, keyboard


game = int(input("""
New layout [0]
Load a layout [1]
>>> """))

map = ""
mat_ = input("Enter the space material (1 character)>> ")
subject_ = input("Enter the subject character (1 character) >> ")
subject = subject_
mat = mat_
grid = []
initial_positions = []
if game == 0:
    width_ = int(input("Enter the width of the map(<173) >> "))
    height_ = int(input("Enter the height of the map(<40) >> "))
    type_of_selection = int(input("""
    Type of the selection:
    Manual selection [0]
    Random selection [1]
    >>> """))

    width = width_
    height = height_
    for x in range(height):
        dummy_list = []
        for y in range(width):
            dummy_list.append(mat)
        grid.append(dummy_list)


    if type_of_selection == 0:
        selector_position = [0, 0]
        selection_loop = True
        initial_positions = []
        while selection_loop:
            system('cls')
            print(map)
            map = ""
            for initial_position in initial_positions:
                grid[initial_position[1]][initial_position[0]] = subject

            grid[selector_position[1]][selector_position[0]] = subject
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    map += grid[x][y] 
                map += "\n"
            if keyboard.is_pressed("d"):
                if selector_position[0] != width-1:
                    grid[int(selector_position[1])][int(selector_position[0])] = mat
                    selector_position[0] += 1
            if keyboard.is_pressed("a"):
                if selector_position[0] != 0:
                    grid[int(selector_position[1])][int(selector_position[0])] = mat
                    selector_position[0] -= 1
            if keyboard.is_pressed("w"):
                if selector_position[1] != 0:
                    grid[int(selector_position[1])][int(selector_position[0])] = mat
                    selector_position[1] -= 1
            if keyboard.is_pressed("s"):
                if selector_position[1] != height-1:
                    grid[int(selector_position[1])][int(selector_position[0])] = mat
                    selector_position[1] += 1
            if keyboard.is_pressed("space"):
                if selector_position not in initial_positions:
                    initial_positions.append([selector_position[0], selector_position[1]])
                elif selector_position in initial_positions:
                    initial_positions.remove([selector_position[0], selector_position[1]])
            if keyboard.is_pressed("enter"):
                selection_loop = False
            sleep(0.04)
             

    map = ""



    #RANDOMIZE
    def random_selection():
        randomness = int(input("Enter the level of randomness (0-10) >> "))
        if randomness > 10 or randomness < 0:
            print("Enter valid argument!!!")
            random_selection()
        for x in range(int((width*height/10)*randomness)):
            random_column_count = random.randint(0, height-1)
            random_row_count = random.randint(0, width-1)
            initial_positions.append([random_row_count, random_column_count])
            grid[random_column_count][random_row_count] = subject

    if type_of_selection == 1:
        random_selection()

if game == 1:
    file_path = input("Enter the full path to the file >> ")
    try:
        file = open(file_path, "r")
        file_loop = True
        line_num = 0
        while file_loop:
            line = file.readline()
            if line == "":
                file_loop = False
            line_num+=1
        file = open(file_path, "r")
        for x in range(line_num-1):
            line = file.readline()
            print(f"#{x} " + line)
        layout = int(input("Enter the layout number you want to select >> "))
        file = open(file_path, "r")
        for x in range(layout+1):
            content = file.readline()
        
        list1 = []

        splitted = content.split()
        print(splitted)
        for x in range(len(splitted)):
            if splitted[x].startswith("[["):
                list1.append([int(splitted[x][2:-1]), int(splitted[x+1][:-2])])
            elif splitted[x].startswith("["):
                list1.append([int(splitted[x][1:-1]), int(splitted[x+1][:-2])])
            elif splitted[x].startswith("width"):
                width = int(splitted[x][6:-1])
            elif splitted[x].startswith("height"):
                height = int(splitted[x][7:])
        print(list1, width, height)
        for x in range(height):
            dummy_list = []
            for y in range(width):
                dummy_list.append(mat)
            grid.append(dummy_list)
        
        for x in list1:
            if x not in initial_positions:
                initial_positions.append(x)

        for initial_position in initial_positions:
                grid[initial_position[1]][initial_position[0]] = subject

    except:
        print("File not found!!!") 


mainloop = True
while mainloop:
    system("cls")
    print(map)
    map = ""
    if keyboard.is_pressed('p'):
        mainloop = False
    grid_validation = []
    for x in range(height):
        dummy_list = []
        grid_validation.append(dummy_list)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            valid = 0
            if y > 0:
                if grid[x][y-1] == subject:
                    valid += 1
            if y < len(grid[x]) - 1:
                if grid[x][y+1] == subject:
                    valid += 1
            if x > 0:
                if y > 0:
                    if grid[x-1][y-1] == subject:
                        valid += 1
                if y < len(grid[x]) - 1:
                    if grid[x-1][y+1] == subject:
                        valid += 1
                if y == 0 or 0 < y < len(grid[x]) - 1:
                    if grid[x-1][y] == subject:
                        valid += 1
            if x < len(grid) - 1:
                if y > 0:
                    if grid[x+1][y-1] == subject:
                        valid += 1
                if y < len(grid[x]) - 1:
                    if grid[x+1][y+1] == subject:
                        valid += 1
                if y == 0 or 0 < y < len(grid[x]) - 1:
                    if grid[x+1][y] == subject:
                        valid += 1
            if grid[x][y] == subject:
                if valid < 2 or valid > 3:
                    grid_validation[x].append(0)
                if 1 < valid < 4:
                    grid_validation[x].append(1)
            if grid[x][y] == mat:
                if valid == 3:
                    grid_validation[x].append(1)
                else:
                    grid_validation[x].append(0)
            map += grid[x][y]
        map += "\n"

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid_validation[x][y] == 0:
                grid[x][y] = mat
            if grid_validation[x][y] == 1:
                grid[x][y] = subject
    sleep(0.03)
    


if game != 1:
    endloop = True
    while endloop:
        command = int(input("""
    Do you want to save the layout?
    Yes [0]
    No [1]
    >>> """))
        if command == 1:
            endloop = False
        if command == 0:
                file_type = int(input("""
    Do you want to save the layout on a new file or existing file?
    New file [0]
    Existing file [1]
    >>> """))
                if file_type == 1:
                    try:
                        file_path = input("Enter the full path to the file >> ")
                        file = open(file_path, "r")
                        print(file.read())
                        name_of_layout = input("What do you want to name layout as(Do not use '[' or ']')? >> ")
                        file = open(file_path, "a")
                        validation_to_save = int(input("""
    Are you sure about saving this layout on this file? 
    Yes [0]
    No [1] 
    >> """))
                        if validation_to_save == 0:
                            file.write(name_of_layout + f" width:{width}, height:{height}"+ " - "+ str(initial_positions) + "\n")
                            endloop = False
                    except:
                        print("File not found!!!")
                if file_type == 0:
                    try:
                        file_name = input('''
    What do you want to name the file(without .txt)? 
    !Make sure that file doesn't already exist
    >> ''')
                        file_path = input("""
    Where do you want to place the file? 
    Example: C:\\Users\\user\\Desktop
    Places the file on the Desktop >> """)
                        file = open(f"{file_path}/{file_name}.txt", "x")
                        file = open(f"{file_path}/{file_name}.txt", "a")
                        name_of_layout = input("What do you want to name layout as(Do not use '[' or ']')? >> ")
                        validation_to_save = int(input("""
    Are you sure about saving this layout on this file? 
    Yes [0]
    No [1] 
    >> """))
                        if validation_to_save == 0:
                            file.write(name_of_layout + f" width:{width}, height:{height}" + " - " + str(initial_positions) + "\n")
                            endloop = False
                    except:
                        print("The file already exists!!!")
