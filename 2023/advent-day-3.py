f = open("day-3.txt", "r")

grid = []
visited = []
 
for line in f:
    visited_row = []
    row = []
    for c in line.strip():
        row.append(c)
        visited_row.append(False)
    grid.append(row)
    visited.append(visited_row)
 
# for row in grid:
#   print(row)
 
# for row in visited:
#   print(row)
 
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
 
def is_adjacent_to_symbol(row, col):
    for dir in dirs:
        new_row = row + dir[0]
        new_col = col + dir[1]
        if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[new_row]) and grid[new_row][new_col] != "." and not grid[new_row][new_col].isdigit():
            return True
    return False
 
 
def is_number_valid(start_row, start_col):
    cols = [start_col]
    visited[start_row][start_col] = True
    number = grid[start_row][start_col]
    full_number_found = False
    curr_col = start_col
    while not full_number_found:
        curr_col = curr_col + 1
        if curr_col < len(grid[start_row]) and grid[start_row][curr_col].isdigit():
            cols.append(curr_col)
            visited[start_row][curr_col] = True
            number += grid[start_row][curr_col]
        else:
            full_number_found = True
    for col in cols:
        if is_adjacent_to_symbol(start_row, col):
            return int(number)
    return False
 
def part1():
    sum = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col].isdigit() and not visited[row][col]:
                result = is_number_valid(row, col)
                if result != False:
                    sum += result
    print(sum)
 
 
def find_number(row, col):
    number = grid[row][col]
    right_end = False
    new_col = col
    while not right_end:
        new_col += 1
        if new_col < len(grid[row]) and grid[row][new_col].isdigit():
            number += grid[row][new_col]
            visited[row][new_col] = True
        else:
            right_end = True
 
    left_end = False
    new_col = col
    while not left_end:
        new_col -= 1
        if new_col >= 0 and grid[row][new_col].isdigit():
            number = grid[row][new_col] + number
            visited[row][new_col] = True
        else:
            left_end = True
    return number
 
 
def find_gear_factor(row, col):
    numbers = []
    for dir in dirs:
        new_row = row + dir[0]
        new_col = col + dir[1]
        if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[new_row]) and visited[new_row][new_col] == False and grid[new_row][new_col].isdigit():
            numbers.append(find_number(new_row, new_col))
    if len(numbers) == 2:
        return int(numbers[0]) * int(numbers[1])
    return False
 
 
def part2():
    sum = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "*":
                result = find_gear_factor(row, col)
                if result != False:
                    sum += result
    print(sum)
 
part2()