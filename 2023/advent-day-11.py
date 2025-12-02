f = open("day-11.txt", "r")

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print("")

def get_rows_to_expand(raw_grid):
    rows_to_expand = []
    for i in range(len(raw_grid)):
        all_rows_empty = True 
        for j in range(len(raw_grid[i])):
            if raw_grid[i][j] != ".":
                all_rows_empty = False
                break
        if all_rows_empty:
            rows_to_expand.append(i)
    return rows_to_expand

def get_cols_to_expand(raw_grid):
    columns_to_expand = []
    for i in range(len(raw_grid[0])):
        all_columns_empty = True
        for j in range(len(raw_grid)):
            if raw_grid[j][i] != ".":
                all_columns_empty = False
                break
        if all_columns_empty:
            columns_to_expand.append(i)
    return columns_to_expand

def expand_grid(raw_grid, rows_to_expand, columns_to_expand):
    expanded_grid = []
    for i in range(len(raw_grid)):
        row = []
        for j in range(len(raw_grid[i])):
            if j in columns_to_expand:
                row.append(".")
            row.append(raw_grid[i][j])
        expanded_grid.append(row)
        if i in rows_to_expand:
            copied_row = row.copy()
            expanded_grid.append(copied_row)
    return expanded_grid

def find_galaxies(expanded_grid):
    galaxies = []
    for i in range(len(expanded_grid)):
        for j in range(len(expanded_grid[i])):
            if expanded_grid[i][j] == "#":
                galaxies.append((i,j))
    return galaxies

def get_pairs_of_galaxies(galaxies):
    pairs = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            pairs.append((galaxies[i], galaxies[j]))
    return pairs

def get_distance_between_galaxies(galaxy1, galaxy2):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

def get_distance_between_galaxies_with_expansions(galaxy1, galaxy2, rows_to_expand, columns_to_expand):
    distance = 0
    for i in range(min(galaxy1[0], galaxy2[0]), max(galaxy1[0], galaxy2[0])):
        if i in rows_to_expand:
            distance += 999999
    
    for i in range(min(galaxy1[1], galaxy2[1]), max(galaxy1[1], galaxy2[1])):
        if i in columns_to_expand:
            distance += 999999

    distance += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    return distance

def part1():
    # process the text file into a raw grid
    raw_grid = []
    for l in f:
        row = []
        line = l.strip()
        for character in line:
            row.append(character)
        raw_grid.append(row)
    # expand the grid for the empty rows/columns
    rows_to_expand = get_rows_to_expand(raw_grid)
    columns_to_expand = get_cols_to_expand(raw_grid)

    expanded_grid = expand_grid(raw_grid, rows_to_expand, columns_to_expand)

    galaxies = find_galaxies(expanded_grid)

    pairs = get_pairs_of_galaxies(galaxies)
    print(len(pairs))

    distance_sum = 0
    for pair in pairs:
        distance_sum += get_distance_between_galaxies(pair[0], pair[1])
    print(distance_sum)

def part2():
    # process the text file into a raw grid
    raw_grid = []
    for l in f:
        row = []
        line = l.strip()
        for character in line:
            row.append(character)
        raw_grid.append(row)
    # expand the grid for the empty rows/columns
    rows_to_expand = get_rows_to_expand(raw_grid)
    columns_to_expand = get_cols_to_expand(raw_grid)

    # Let's not expand it manually. If when we're getting distance, we realize we need to cross 
    # something we should expand, we should just add 1 million to it. 
    # expanded_grid = expand_grid(raw_grid, rows_to_expand, columns_to_expand)

    galaxies = find_galaxies(raw_grid)
    pairs = get_pairs_of_galaxies(galaxies)

    distance_sum = 0
    for pair in pairs:
        distance_sum += get_distance_between_galaxies_with_expansions(pair[0], pair[1], rows_to_expand, columns_to_expand)
    print(distance_sum)

part2()