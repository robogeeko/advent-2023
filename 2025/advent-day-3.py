f = open("./2025/day-3.txt", "r")


def part1():
    sum = 0
    for l in f:
        line = l.strip()
        biggest = 0
        second_biggest = 0
        for i in range(len(line)):
            num = int(line[i])
            if num > biggest and i < len(line) - 1:
                second_biggest = 0
                biggest = num
            elif num > second_biggest:
                second_biggest = num

        accumulator = biggest * 10 + second_biggest
        sum += accumulator
    print(sum)


# part1()


def find_biggest_in_number(num_str, how_many_left, current_list):
    biggest_number = 0
    biggest_index = -1
    for i in range(len(num_str) - (how_many_left - 1)):
        number = int(num_str[i])
        if number > biggest_number:
            biggest_number = number
            biggest_index = i

    current_list.append(biggest_number)
    if how_many_left > 1:
        current_list = find_biggest_in_number(
            num_str[biggest_index + 1 :], how_many_left - 1, current_list
        )

    return current_list


def part2():
    sum = 0
    for l in f:
        line = l.strip()
        biggest_list = find_biggest_in_number(line, 12, [])
        big_num = 0
        count = 0
        for i in range(len(biggest_list) - 1, -1, -1):
            big_num += biggest_list[i] * 10 ** (count)
            count += 1
        sum += big_num

    print(sum)


part2()
