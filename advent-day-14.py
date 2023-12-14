f = open("day-14.txt", "r")

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
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

def tilt_north(grid):
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            # print("Checking {}, {}".format(row_index, col_index))
            # print_grid(grid)
            # input()
            if grid[row_index][col_index] == "O" or grid[row_index][col_index] == "#":
                continue
            # the character must be a .
            checking_row = row_index + 1
            while checking_row < len(grid):
                if grid[checking_row][col_index] == "O":
                    grid[row_index][col_index] = "O"
                    grid[checking_row][col_index] = "."
                    break
                elif grid[checking_row][col_index] == "#":
                    break
                checking_row += 1
            
def compute_score(grid):
    score = 0
    multiplier = len(grid)
    for row_index in range(len(grid)):
        total_rocks_in_row = 0
        for col_index in range(len(grid[row_index])):
            if grid[row_index][col_index] == "O":
                total_rocks_in_row += 1
        score += total_rocks_in_row * multiplier
        # print("Score: {}, total_rocks_in_row: {}, multiplier: {}".format(score,total_rocks_in_row,multiplier))
        multiplier -= 1
    return score

def find_rocks(grid):
    # maybe it's efficient to keep a sorted list of rocks, by column
    # {
    #     column: [row_val, row_val]
    # }
    rocks = {}
    for col_index in range(len(grid[0])):
        rocks[col_index] = []
        for row_index in range(len(grid)):
            if grid[row_index][col_index] == "O":
                rocks[col_index].append(row_index)
    return rocks

def fast_tilt_north(grid, rocks):
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            # print("Checking {}, {}".format(row_index, col_index))
            # print_grid(grid)
            # input()
            if grid[row_index][col_index] == "O" or grid[row_index][col_index] == "#":
                continue
            # the character must be a .
            checking_row = row_index + 1
            while checking_row < len(grid):
                if grid[checking_row][col_index] == "O":
                    grid[row_index][col_index] = "O"
                    grid[checking_row][col_index] = "."
                    break
                elif grid[checking_row][col_index] == "#":
                    break
                checking_row += 1

def rot_90(l):
    return [list(reversed(x)) for x in zip(*l)]

def cycle_grid(grid):
    tilt_north(grid)
    reflected_grid = rot_90(grid)
    tilt_north(reflected_grid)
    reflected_grid2 = rot_90(reflected_grid)
    tilt_north(reflected_grid2)
    reflected_grid3 = rot_90(reflected_grid2)
    tilt_north(reflected_grid3)
    reflected_grid4 = rot_90(reflected_grid3)
    return reflected_grid4

def part1():
    grids = process_file_to_grids()
    grid = grids[0]
    scores = []
    # This one was a cycle so run it until you find the cycle, and do it by hand a bit
    print((340-200) % 9)
    print((1000000000-200) % 9)
    for i in range(1, 10000):
        # rocks = find_rocks(grid)
        # print(rocks)
        # input()
        grid = cycle_grid(grid)
        # input()
        # if i % 100000 == 0:
        # print("Iteration: {}".format(i))
        score = compute_score(grid)
        if score in scores:
            print("Found a cycle at iteration {}, Score: {}".format(i, score))
        scores.append(score)
    print("Final grid: ")
    print_grid(grid)
    print(compute_score(grid))


part1()



def part2():
    for l in f:
        line = l.strip()
        print(line)
