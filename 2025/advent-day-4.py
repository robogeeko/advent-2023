f = open("./2025/day-4.txt", "r")

ops = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def get_adjacents(grid, row, col):
    adjacent_values = []
    for operation in ops:
        new_row = row + operation[0]
        new_col = col + operation[1]
        if (
            new_row < 0
            or new_row >= len(grid)
            or new_col < 0
            or new_col >= len(grid[0])
        ):
            continue
        adjacent_values.append(grid[new_row][new_col])
    return adjacent_values


def part1():
    grid = []
    for l in f:
        line = l.strip()
        print(line)
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    count_valid_rolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != "@":
                continue
            adjacents = get_adjacents(grid, row, col)
            count_adjacent_rolls = 0
            for adjacent in adjacents:
                if adjacent == "@":
                    count_adjacent_rolls += 1

            if count_adjacent_rolls < 4:
                count_valid_rolls += 1


# part1()


def part2():
    grid = []
    for l in f:
        line = l.strip()
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    overall_count = 0
    while True:
        count_valid_rolls = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != "@":
                    continue
                adjacents = get_adjacents(grid, row, col)
                count_adjacent_rolls = 0
                for adjacent in adjacents:
                    if adjacent == "@":
                        count_adjacent_rolls += 1

                if count_adjacent_rolls < 4:
                    count_valid_rolls += 1
                    grid[row][col] = "."
        overall_count += count_valid_rolls
        if count_valid_rolls == 0:
            break
    print(overall_count)


part2()
