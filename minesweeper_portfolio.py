# Given a Minesweeper-like grid represented by a list of lists. 
# The grid contains two types of cells: "-" for free spots and "#" for mines. 
# Your task is to create a program that takes this grid as input 
# and returns a copy of the grid where each "-" is replaced with a 
# number representing the count of mines in the surrounding cells 
# (including diagonals).

# input_grid = [
#     ["-", "#", "-", "#", "#"],
#     ["#", "-", "-", "#", "#"],
#     ["-", "#", "#", "-", "-"],
#     ["-", "-", "-", "-", "#"],
#     ["#", "#", "-", "-", "-"]
# ]

# output_grid = minesweeper(input_grid)

# The resulting output_grid should be:
# [
#     [ 2,  "#",  3,  "#", "#"],
#     ["#",  4,   5,  "#", "#"],
#     [ 2,  "#", "#",  4,   3],
#     [ 3,   4,   3,   2,  "#"],
#     ["#", "#",  1,   1,   1]
# ]

input_grid = [
    ["-", "#", "-", "#", "#"],
    ["#", "-", "-", "#", "#"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "#"],
    ["#", "#", "-", "-", "-"]
]
rows = len(input_grid)                                              # find the number or rows and columns in the input_grid
cols = len(input_grid[0])


output_grid = [[" " for j in range(cols)] for i in range(rows)]     # create an output_grid of the same size but with blank spaces

for i in range(rows):                                               # loop through the indices of the outer lists in the grid (rows)
    for j in range(cols):                                           # within that loop, loop through the indices of the inner lists
        
        if input_grid[i][j] == "#":                                 # if there is a mine at each position in the input_grid[i][j] 
            output_grid[i][j] = "#"                                 # place a mine at the same position in the output_grid
        else:
            mine_count = 0                                          # set mine count to 0

            if i > 0 and j > 0:
                if input_grid[i-1][j-1] == "#":                         # count mine to top left [i-1][j-1] for items that have one
                    mine_count += 1

            if i > 0:
                if input_grid[i-1][j] == "#":                           # count mine to top middle [i-1][j] for items that have one
                    mine_count += 1

            if i > 0 and j < (cols - 1):
                if input_grid[i-1][j+1] == "#":                         # count mine to top right [i-1][j+1] for items that have one
                    mine_count += 1

            if j > 0:
                if input_grid[i][j-1] == "#":                           # count mine to middle left [i][j-1] for items that have one
                    mine_count += 1           
        
            if j < (cols - 1):
                if input_grid[i][j+1] == "#":                           # count mine to middle right [i][j+1] for items that have one
                    mine_count += 1

            if i < (rows - 1) and j > 0:
                if input_grid[i+1][j-1] == "#":                         # count mine to bottom left [i+1][j-1] for items that have one
                    mine_count += 1

            if i < (rows - 1):
                if input_grid[i+1][j] == "#":                           # count mine to bottom middle [i+1][j] for items that have one
                    mine_count += 1

            if i < (rows - 1) and j < (cols - 1):
                if input_grid[i+1][j+1] == "#":                         # count mines to bottom right [i+1][j+1] for items that have one
                    mine_count += 1    



            output_grid[i][j] = mine_count                                    # update the item at the same position in the output_grid with the mine count

for row in output_grid:                                     # print the output_grid
    print(row)


