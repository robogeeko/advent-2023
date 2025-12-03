import math

f = open("./2025/day-2.txt", "r")


def test_number(number):
    num_string = str(number)
    if len(num_string) % 2 != 0:
        return False

    first_half = num_string[: len(num_string) // 2]
    second_half = num_string[len(num_string) // 2 :]
    if first_half != second_half:
        return False

    return True


def get_divisors(number):
    divisors = []
    for i in range(1, math.ceil(math.sqrt(number) + 1)):
        if number % i == 0:
            divisors.append(i)
            divisors.append(number // i)
    set_divisors = set(divisors)
    set_divisors.remove(number)
    return set_divisors


def test_number_part_2(number):
    num_string = str(number)
    divisors = get_divisors(len(num_string))

    for divisor in divisors:
        string_parts = [
            num_string[i : i + divisor] for i in range(0, len(num_string), divisor)
        ]
        if len(set(string_parts)) == 1:
            return True
    return False


def part1():
    invalid_ids = []
    intervals = []
    for l in f:
        line = l.strip()
        print(line)
        intervals_in_line = line.split(",")
        for interval in intervals_in_line:
            if interval != "":
                interval_parts = interval.split("-")
                intervals.append((int(interval_parts[0]), int(interval_parts[1])))

    print(intervals)
    for interval in intervals:
        for i in range(interval[0], interval[1] + 1):
            if test_number(i):
                invalid_ids.append(i)
    sum = 0
    for invalid_id in invalid_ids:
        sum += invalid_id
    print(sum)


# part1()


def part2():
    invalid_ids = []
    intervals = []
    for l in f:
        line = l.strip()
        print(line)
        intervals_in_line = line.split(",")
        for interval in intervals_in_line:
            if interval != "":
                interval_parts = interval.split("-")
                intervals.append((int(interval_parts[0]), int(interval_parts[1])))

    print(intervals)
    for interval in intervals:
        for i in range(interval[0], interval[1] + 1):
            if test_number_part_2(i):
                invalid_ids.append(i)
    sum = 0
    for invalid_id in invalid_ids:
        sum += invalid_id
    print(sum)


part2()
