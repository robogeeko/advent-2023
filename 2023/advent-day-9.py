f = open("day-9.txt", "r")

def is_all_zero(some_list):
    if all(x == some_list[0] for x in some_list):
        return some_list[0] == 0
    return False


def part1():
    extrapolated_vals = []
    for l in f:
        line = l.strip()
        numbers = line.split()
        integers = []
        for number in numbers:
            integers.append(int(number))
        index_to_check = 0
        numbers_to_check = [integers]
        diffs = [1]
        while not is_all_zero(diffs):
            diffs = []
            for index in range(len(numbers_to_check[index_to_check]) - 1):
                diffs.append(numbers_to_check[index_to_check][index + 1] - numbers_to_check[index_to_check][index])
            numbers_to_check.append(diffs)
            index_to_check += 1

        index = len(numbers_to_check) - 1
        numbers_to_check[index].append(0)
        index -= 1
        while index >= 0:
            numbers_to_check[index].append(numbers_to_check[index][-1] + numbers_to_check[index + 1][-1])
            index -= 1
        extrapolated_vals.append(numbers_to_check[0][-1])
    print(sum(extrapolated_vals))


# part1()

def part2():
    extrapolated_vals = []
    for l in f:
        line = l.strip()
        numbers = line.split()
        integers = []
        for number in numbers:
            integers.append(int(number))
        index_to_check = 0
        numbers_to_check = [integers]
        diffs = [1]
        while not is_all_zero(diffs):
            diffs = []
            for index in range(len(numbers_to_check[index_to_check]) - 1):
                diffs.append(numbers_to_check[index_to_check][index + 1] - numbers_to_check[index_to_check][index])
            numbers_to_check.append(diffs)
            index_to_check += 1

        index = len(numbers_to_check) - 1
        numbers_to_check[index].insert(0, 0)
        index -= 1
        while index >= 0:
            numbers_to_check[index].insert(0, numbers_to_check[index][0] - numbers_to_check[index + 1][0])
            index -= 1
        extrapolated_vals.append(numbers_to_check[0][0])
    print(sum(extrapolated_vals))

part2()
