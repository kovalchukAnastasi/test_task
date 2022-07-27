# You were given a map (2 dimensional grid) where each cell is either forest (marked as X) or grassland (marked as O). 
# Write a script that gets number of isolated forests on the map. Forest is formed of cells X that are connected in one of 8 directions. 
# In case code is not working, please explain the search strategy.

import random

class Cell:
    def __init__(self, isTree=None, coordinates=[], isChecked=False):
        self.isTree = isTree
        self.coordinates = coordinates
        self.isChecked = isChecked
        #print('This cell is a tree:', self.isTree, 'Coordinates:', self.coordinates, 'It was checked', self.isChecked)
        
def create_map(n, m):
    map = []
    for i in range(int(n)):
        inner_arrays = []
        for j in range(int(m)):
            rand_value = random.randrange(0, 2)
            if rand_value == 0:
                element = Cell(False, [i, j], False)
                inner_arrays.append(element)
            else:
                element = Cell(True, [i, j], False)
                inner_arrays.append(element)
        map.append(inner_arrays)
    return map

def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j].isTree == True:
                print('X', end=' ')
            else:
                print('O', end=' ')
        print()

# cheking the map for forests
def check_map(map):
    forests = [] # list of isolated forests
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j].isChecked == True:
                continue
            else:
                map[i][j].isChecked = True
                if map[i][j].isTree == False:
                    continue
                else:
                    forest = [] # list of coordinates of trees in one isolated forest
                    forest.append(map[i][j].coordinates)
                    check_neighbours(map, i, j, forest)
                    forests.append(forest)
    #print(forests)
    number_of_forests = len(forests)
    print('Number of isolated forests: ', number_of_forests)

# range of cells around a cell in a grid
def range_around_cell(map, i, j):
    if i == 0:
        if j == 0:
            range_k_1 = 0
            range_k_2 = 2
            range_l_1 = 0
            range_l_2 = 2
        elif j == len(map[i]) - 1:
            range_k_1 = 0
            range_k_2 = 2
            range_l_1 = len(map[i]) - 2
            range_l_2 = len(map[i])
        else:
            range_k_1 = 0
            range_k_2 = 2
            range_l_1 = j-1
            range_l_2 = j+2
    elif i == len(map) - 1:
        if j == 0:
            range_k_1 = len(map) - 2
            range_k_2 = len(map)
            range_l_1 = 0
            range_l_2 = 2
        elif j == len(map[i]) - 1:
            range_k_1 = len(map) - 2
            range_k_2 = len(map)
            range_l_1 = len(map[i]) - 2
            range_l_2 = len(map[i])
        else:
            range_k_1 = len(map) - 2
            range_k_2 = len(map)
            range_l_1 = j-1
            range_l_2 = j+2
    else:
        if j == 0:
            range_k_1 = i-1
            range_k_2 = i+2
            range_l_1 = 0
            range_l_2 = 2
        elif j == len(map[i]) - 1:
            range_k_1 = i-1
            range_k_2 = i+2
            range_l_1 = len(map[i]) - 2
            range_l_2 = len(map[i])
        else:
            range_k_1 = i - 1
            range_k_2 = i + 2
            range_l_1 = j - 1
            range_l_2 = j + 2
    range_around = [range_k_1, range_k_2, range_l_1, range_l_2]
    #print('range for cell', '[', i, j, ']', 'is', range_k_1, range_k_2 - 1, range_l_1, range_l_2 - 1)
    return range_around
    
# cheking cells around a tree to create an isolated forest
def check_neighbours(map, i, j, forest):
    cell_range = range_around_cell(map, i, j)
    for k in range(cell_range[0], cell_range[1]):
        for l in range(cell_range[2], cell_range[3]):
            if map[k][l].isChecked == True:
                continue
            else:
                map[k][l].isChecked = True
                if map[k][l].isTree == True:
                    forest.append(map[k][l].coordinates)
                    check_neighbours(map, k, l, forest)
                else:
                    #print('This cell is not a tree', k, l)
                    continue

n = input('Please, enter number of rows\n')
m = input('Please, enter number of columns\n')
map = create_map(n,m)
print_map(map)
check_map(map)