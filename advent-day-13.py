f = open("day-13.txt", "r")

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print("")

def print_grids(grids):
    for grid in grids:
        print_grid(grid)
        print("")

def process_file_to_grids():
    grids = []
    grid = []
    grid_row = []
    for l in f:
        line = l.strip()
        grid_row = []
        if line == "":
            grids.append(grid)
            grid = []
            continue
        for character in line:
            grid_row.append(character)
        grid.append(grid_row)
    grids.append(grid)
    return grids

# maybe just find two that are identical that are right next to each other and then check the others
def find_reflection(grid):
    left = 0
    right = 1
    reflection_found = False
    while reflection_found is False:
        if grid[left] == grid[right]:
            found_unmatching = False
            checking_left = left
            checking_right = right
            while checking_left >= 0 and checking_right < len(grid):
                if grid[checking_left] == grid[checking_right]:
                    checking_left -= 1
                    checking_right += 1
                else:
                    found_unmatching = True
                    break
            if found_unmatching is False:
                reflection_found = True
                return (left, right)
        left += 1
        right += 1
        if right >= len(grid):
            break
    return None

def part1():
    grids = process_file_to_grids()
    total = 0
    for grid in grids:
        horizontal_line_reflection = find_reflection(grid)
        if horizontal_line_reflection is not None:
            total += 100 * horizontal_line_reflection[1]
        else:
            reflected_grid = list(zip(*grid[::-1]))
            vertical_line_reflection = find_reflection(reflected_grid)
            total += vertical_line_reflection[1]
    print(total)
    
# part1()

def how_many_differences_between_two_lists(list1, list2):
    differences = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            differences += 1
    return differences

# Let's just brute force it, but count the differences. If the differences are exactly 1, then it's correct
def find_reflection_with_smudge(grid):
    left = 0
    right = 1
    reflection_found = False
    while reflection_found is False:
        total_differences = 0
        checking_left = left
        checking_right = right
        while checking_left >= 0 and checking_right < len(grid):
            differences = how_many_differences_between_two_lists(grid[checking_left],  grid[checking_right])
            total_differences += differences
            if total_differences > 1:
                break
            checking_left -= 1
            checking_right += 1
                  
        if total_differences == 1:
            reflection_found = True
            return (left, right)
        left += 1
        right += 1
        if right >= len(grid):
            break
    return None

def part2():
    grids = process_file_to_grids()
    total = 0
    for grid in grids:
        horizontal_line_reflection = find_reflection_with_smudge(grid)
        if horizontal_line_reflection is not None:
            total += 100 * horizontal_line_reflection[1]
        else:
            reflected_grid = list(zip(*grid[::-1]))
            vertical_line_reflection = find_reflection_with_smudge(reflected_grid)
            total += vertical_line_reflection[1]
    print(total)

part2()