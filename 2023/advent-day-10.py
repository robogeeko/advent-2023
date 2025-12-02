f = open("day-10.txt", "r")

# 0, 1 -> goes right!
# 0, -1 -> goes left!
# 1, 0 -> goes down!!
# -1, 0 -> goes up!
pipe_types = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "[": [(1, 0), (-1, 0)],
    "]": [(0, 1), (0, -1)],
    "L": [(0, 1), (-1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
    "P": [],
    ".": [],
    "B": [],
    "S": [(0, -1), (1, 0)],
    # "S": [(0, 1), (1, 0)],
    # "S": [(0, -1), (-1, 0)],
}


def are_all_equal(list):
    return all(i == list[0] for i in list)

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print("")

def part1():
    analysis_grid = []
    grid = []
    row_number = 1
    start = None
    for l in f:
        line = l.strip()
        if row_number == 1:
            row = []
            analyze_row = []
            analyze_row.append(".")
            row.append(".")
            for character in line:
                row.append(".")
                analyze_row.append(".")
            row.append(".")
            analyze_row.append(".")
            grid.append(row)
            analysis_grid.append(analyze_row)
        row = []
        col_number = 1
        row.append(".")
        analyze_row = []
        analyze_row.append(".")
        for character in line:
            if character == "S":
                start = (row_number, col_number)
            row.append(character)
            analyze_row.append(".")
            col_number += 1
        row.append(".")
        analyze_row.append(".")
        grid.append(row)
        analysis_grid.append(analyze_row)
        row_number += 1
    row = []
    analyze_row = []
    for index in range(len(grid[0])):
        row.append(".")
        analyze_row.append(".")
    analysis_grid.append(analyze_row)
    grid.append(row)
    print_grid(grid)
    print(start)
    potential_directions = []
    checked_locations = []
    previous_directions = []
    analysis_grid[start[0]][start[1]] = "P"
    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        print(dir)
        check_spot = grid[start[0] + dir[0]][start[1] + dir[1]]
        print(check_spot)
        if check_spot == ".":
            continue
        for (x, y) in pipe_types[check_spot]:
            print("dir x: {}, dir y: {}, x {}, y {}".format(dir[0], dir[1], x, y))
            if dir[0] + x == 0 and dir[1] + y == 0:
                print("FOUND A POTENTIAL DIRECTION")
                potential_directions.append(dir)
                checked_locations.append((start[0] + dir[0], start[1] + dir[1]))
                previous_directions.append(dir)
                analysis_grid[start[0] + dir[0]][start[1] + dir[1]] = "P"
    print(potential_directions)
    
    print(checked_locations)
    print(previous_directions)
    steps = 1
    while not are_all_equal(checked_locations):
        for index in range(len(checked_locations)):
            location = checked_locations[index]
            analysis_grid[location[0]][location[1]] = "P"
            prev_direction = previous_directions[index]
            pipe = grid[location[0]][location[1]]
            # print("pipe: {}".format(pipe))
            for (x, y) in pipe_types[pipe]:
                if x + prev_direction[0] == 0 and y + prev_direction[1] == 0:
                    continue
                checked_locations[index] = (location[0] + x, location[1] + y)
                previous_directions[index] = (x, y)
            # print("new_location: {}, new pipe: {}".format(checked_locations[index], grid[checked_locations[index][0]][checked_locations[index][1]]))
        steps += 1
        # input()
    print_grid(analysis_grid)
    print(steps)

def find_outside(row_index, col_index, grid):
    visited = set()
    visited.add((row_index, col_index))
    things_to_visit = set()
    things_to_visit.add((row_index, col_index))
    found_outside = False
    steps = 0
    while len(things_to_visit) > 0:
        location = things_to_visit.pop()
        for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (location[0] + dir[0], location[1] + dir[1]) in visited:
                continue
            if grid[location[0] + dir[0]][location[1] + dir[1]] == "*" or grid[location[0] + dir[0]][location[1] + dir[1]] == "N":
                things_to_visit.add((location[0] + dir[0], location[1] + dir[1]))
                visited.add((location[0] + dir[0], location[1] + dir[1]))
            if grid[location[0] + dir[0]][location[1] + dir[1]] == "0":
                visited.add((location[0] + dir[0], location[1] + dir[1]))
                found_outside = True
        steps += 1
        # if steps % 10000 == 0:
        #     print(len(grid))
        #     print(len(grid[0]))
        #     print("steps: {}".format(steps))
        #     print(len(things_to_visit))
        #     print(len(visited))
        #     # input()
        # print(things_to_visit)
    
    if found_outside:
        for visited_location in visited:
            grid[visited_location[0]][visited_location[1]] = "0"

def part2():
    grid = []
    row_number = 1
    # start = (42, 112)
    start_type = "F"
    for l in f:
        line = l.strip()
        if row_number == 1:
            row = []
            row.append(".")
            for character in line:
                row.append(".")
            row.append(".")
            grid.append(row)
        row = []
        col_number = 1
        row.append(".")
        for character in line:
            if character == "S":
                start = (row_number, col_number)
            row.append(character)
            col_number += 1
        row.append(".")
        grid.append(row)
        row_number += 1
    row = []
    for index in range(len(grid[0])):
        row.append(".")
    grid.append(row)
    # print_grid(grid)
    # expand the grid by columns
    new_grid = []
    for row_index in range(1, len(grid) - 1):
        new_grid_row = []
        for col_index in range(1, len(grid[row_index]) - 1):
            new_grid_row.append(grid[row_index][col_index])
            if grid[row_index][col_index] == ".":
                new_grid_row.append("P")
            elif (0, 1) in pipe_types[grid[row_index][col_index]] and (0, -1) in pipe_types[grid[row_index][col_index + 1]]:
                new_grid_row.append("]")
            # elif grid[row_index][col_index] != "-" and grid[row_index][col_index + 1] != "-":
            #     new_grid_row.append("P")
            else:
                new_grid_row.append("P")
        new_grid.append(new_grid_row)
        # print("ROB CHECK NEW GRID")
        # print_grid(new_grid)
        # print(remove_from_final_count)
        # input()

    final_row = []
    for index in range(len(new_grid[0])):
        final_row.append("P")
    new_grid.append(final_row)

    # print("ROB CHECK NEW GRID")
    # print_grid(new_grid)
    # input()


    final_grid = []
    final_grid.append(new_grid[0])
    for row_index in range(1, len(new_grid) - 1):
        extra_grid_row = []
        final_grid.append(new_grid[row_index])
        extra_grid_row.append("P")
        for col_index in range(1, len(new_grid[row_index]) - 1):
            if new_grid[row_index][col_index] == "." or new_grid[row_index][col_index] == "P":
                extra_grid_row.append("P")
            elif (1, 0) in pipe_types[new_grid[row_index][col_index]] and (-1, 0) in pipe_types[new_grid[row_index + 1][col_index]]:
                extra_grid_row.append("[")
            # elif new_grid[row_index][col_index] != "|" and new_grid[row_index][col_index + 1] != "|":
            #     extra_grid_row.append("P")
            else:
                extra_grid_row.append("P")
        extra_grid_row.append("P")
        final_grid.append(extra_grid_row)
        # print("ROB CHECK FINAL GRID")
        # print_grid(final_grid)
        # input()

    final_row = []
    for index in range(len(new_grid[0])):
        final_row.append("P")
    final_grid.append(final_row)
    print("ROB CHECK")
    print_grid(final_grid)
    # input()
    grid = final_grid

    # find S again
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            if grid[row_index][col_index] == "S":
                start = (row_index, col_index)
    # print("checking start")
    # print(start)
    potential_directions = []
    checked_locations = []
    previous_directions = []
    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # print(dir)
        check_spot = grid[start[0] + dir[0]][start[1] + dir[1]]
        # print(check_spot)
        if check_spot == ".":
            continue
        for (x, y) in pipe_types[check_spot]:
            print("dir x: {}, dir y: {}, x {}, y {}".format(dir[0], dir[1], x, y))
            if dir[0] + x == 0 and dir[1] + y == 0:
                # print("FOUND A POTENTIAL DIRECTION")
                potential_directions.append(dir)
                checked_locations.append((start[0] + dir[0], start[1] + dir[1]))
                previous_directions.append(dir)

    analyzed_grid = []
    for row_index in range(len(grid)):
        analyzed_row = []
        if row_index == 0 or row_index == len(grid) - 1:
            for item in grid[row_index]:
                analyzed_row.append("0")
        else:
            for col_index in range(len(grid[row_index])):
                if col_index == 0 or col_index == len(grid[row_index]) - 1:
                    analyzed_row.append("0")
                elif grid[row_index][col_index] == "P":
                    analyzed_row.append("N")
                elif grid[row_index][col_index] == "[":
                    analyzed_row.append("N")
                elif grid[row_index][col_index] == "]":
                    analyzed_row.append("N")
                else: 
                    analyzed_row.append("*")
        analyzed_grid.append(analyzed_row)
        # print("analyzed grid")
        # print_grid(analyzed_grid)
        # input()

    # print(potential_directions)
    # print(checked_locations)
    # print(previous_directions)
    # print("ROB START")
    # print(start)
    # start = (42, 112)

    analyzed_grid[start[0]][start[1]] = "S"
    
    steps = 1
    # print("checking grid and analyzed")
    # print_grid(grid)
    # print("and analyzed")
    # print_grid(analyzed_grid)
    while steps < 100000:
        for index in range(len(checked_locations)):
            analyzed_grid[checked_locations[index][0]][checked_locations[index][1]] = "P"
            location = checked_locations[index]
            prev_direction = previous_directions[index]
            pipe = grid[location[0]][location[1]]
            # print("pipe: {}".format(pipe))
            if pipe != "S":
                for (x, y) in pipe_types[pipe]:
                    if x + prev_direction[0] == 0 and y + prev_direction[1] == 0:
                        continue
                    checked_locations[index] = (location[0] + x, location[1] + y)
                    previous_directions[index] = (x, y)
                # print("new_location: {}, new pipe: {}".format(checked_locations[index], grid[checked_locations[index][0]][checked_locations[index][1]]))
                # print(analyzed_grid[checked_locations[index][0]][checked_locations[index][1]])
                # analyzed_grid[checked_locations[index][0]][checked_locations[index][1]] = "P"
        steps += 1
        # input()
    print("Rob, printing analyzed grid")
    print_grid(analyzed_grid)
    print("GOT HERE ROB1")
    for row_index in range(len(analyzed_grid)):
        for col_index in range(len(analyzed_grid[row_index])):
            if analyzed_grid[row_index][col_index] == "0":
                continue
            if analyzed_grid[row_index][col_index] == "*":
                print("trying to find the outside of {}".format((row_index, col_index)))
                find_outside(row_index, col_index, analyzed_grid)
    print("final analyzed")
    print_grid(analyzed_grid)
    count_inside = 0 
    for row_index in range(len(analyzed_grid)):
        for col_index in range(len(analyzed_grid[row_index])):
            if analyzed_grid[row_index][col_index] == "*":
                count_inside += 1
    print(count_inside)

part2()