def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print("")

def process_file_to_grids(f):
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

def replicate_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for col in row:
            new_row.append(".")
        new_grid.append(new_row)
    return new_grid

# 0, 1 -> goes right!
# 0, -1 -> goes left!
# 1, 0 -> goes down!!
# -1, 0 -> goes up!

mirrors = {
    "/": {
        (0, 1): (-1, 0),
        (0, -1): (1, 0),
        (1, 0): (0, -1),
        (-1, 0): (0, 1)
    },
    "\\": {
        (0, 1): (1, 0),
        (0, -1): (-1, 0),
        (1, 0): (0, 1),
        (-1, 0): (0, -1)
    }
}

splitters = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)]
}

splitters_no_op = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)]
}

# beams should have location and direction.
# beams = [((location), (direction))]
def energize(grid, energize_grid, beams):
    used_splitters = []
    steps = 0
    any_thing_was_empty = True
    count_all_empty = 0
    while len(beams) > 0:
        any_thing_was_empty = False
        for index in range(len(beams)):
            beam = beams.pop(0)
            row, col = beam[0]
            if energize_grid[row][col] == ".":
                any_thing_was_empty = True
            energize_grid[row][col] = "#"
            drow, dcol = beam[1]
            new_row = row + drow
            new_col = col + dcol
            if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                continue
            grid_val = grid[new_row][new_col]
            if grid_val == ".":
                beams.append(((new_row, new_col), (drow, dcol)))
                continue
            if grid_val in mirrors:
                new_drow, new_dcol = mirrors[grid_val][(drow, dcol)]
                beams.append(((new_row, new_col), (new_drow, new_dcol)))
                continue
            if grid_val in splitters:
                if (drow, dcol) in splitters_no_op[grid_val]:
                    beams.append(((new_row, new_col), (drow, dcol)))
                    continue
                else:
                    if (new_row, new_col) in used_splitters:
                        continue
                    new_drow, new_dcol = splitters[grid_val][0]
                    beams.append(((new_row, new_col), (new_drow, new_dcol)))
                    new_drow, new_dcol = splitters[grid_val][1]
                    beams.append(((new_row, new_col), (new_drow, new_dcol)))
                    used_splitters.append((new_row, new_col))
                    continue
        if any_thing_was_empty is False:
            count_all_empty += 1
            any_thing_was_empty = True
        if any_thing_was_empty and count_all_empty > 50: # how do i end this loop
            break
        steps += 1

def count_energized(grid):
    count = 0
    for row in grid:
        for col in row:
            if col == "#":
                count += 1
    return count

def get_starting_direction(grid, row, col, starting_dir):
    grid_value = grid[row][col]
    if grid_value == ".":
        return [starting_dir]
    if grid_value in splitters_no_op:
        if starting_dir in splitters_no_op[grid_value]:
            return [starting_dir]
        else:
            return splitters[grid_value]
    if grid_value == "/" or grid_value == "\\":
        return [mirrors[grid_value][(starting_dir)]]

def get_point_max(grid, row, col, starting_dir):
    energized_grid = replicate_grid(grid)
    starting_dirs = get_starting_direction(grid, row, col, starting_dir)
    beams = [((row, col), starting_dir) for starting_dir in starting_dirs]
    energize(grid, energized_grid, beams)
    return count_energized(energized_grid)

def get_max_energization(grid):
    col = 0
    max_score = 0
    for row in range(len(grid)):
        starting_dir = (0, 1)
        point_max = get_point_max(grid, row, col, starting_dir)
        if point_max > max_score:
            max_score = point_max
    col = len(grid[0]) - 1
    for row in range(len(grid)):
        starting_dir = (0, -1)
        point_max = get_point_max(grid, row, col, starting_dir)
        if point_max > max_score:
            max_score = point_max
    row = 0
    for col in range(len(grid[0])):
        starting_dir = (1, 0)
        point_max = get_point_max(grid, row, col, starting_dir)
        if point_max > max_score:
            max_score = point_max
    row = len(grid) - 1
    for col in range(len(grid[0])):
        starting_dir = (-1, 0)
        point_max = get_point_max(grid, row, col, starting_dir)
        if point_max > max_score:
            max_score = point_max
    return max_score

def part1():
    f = open("day-16.txt", "r")
    grids = process_file_to_grids(f)
    grid = grids[0]
    energized_grid = replicate_grid(grid)
    starting_dirs = get_starting_direction(grid, 0, 0, (0, 1))
    beams = [((0, 0), starting_dir) for starting_dir in starting_dirs]
    energize(grid, energized_grid, beams)
    print(count_energized(energized_grid))
    
def part2():
    f = open("day-16.txt", "r")
    grids = process_file_to_grids(f)
    grid = grids[0]
    print(get_max_energization(grid))

part1()
part2()
