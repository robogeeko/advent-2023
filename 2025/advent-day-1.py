f = open("./2025/day-1.txt", "r")


def parse_command(command):
    direction = command[0]
    distance = int(command[1:])
    return direction, distance


def part1():
    commands = []
    for l in f:
        line = l.strip()
        commands.append(line)

    curr = 50
    accumulation = 0
    for command in commands:
        direction, distance = parse_command(command)
        if direction == "L":
            curr -= distance
        else:
            curr += distance

        if curr < 0:
            curr = 100 + curr % 100
        if curr >= 100:
            curr = curr % 100
        print(curr)
        if curr == 0:
            accumulation += 1
            print("hit 0!")

    print(accumulation)


# part1()


def part2():
    def times_hit_zero_and_count(curr, direction, distance):
        accumulation = 0
        if direction == "L":
            operation = -1
        else:
            operation = 1
        for i in range(distance):
            curr += operation

            if curr == -1:
                curr = 99
            if curr == 100:
                curr = 0

            if curr == 0:
                accumulation += 1

        return accumulation, curr

    curr = 50
    accumulation = 0
    for l in f:
        line = l.strip()
        direction, distance = parse_command(line)
        times_hit_zero, curr = times_hit_zero_and_count(curr, direction, distance)
        accumulation += times_hit_zero

    print(accumulation)


part2()
