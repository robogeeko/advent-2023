f = open("day-6.txt", "r")

def part1():
    times = None
    distances = None
    for l in f:
        line = l.strip()
        numbers = line.split()
        numbers.pop(0)
        if times is None:
            times = numbers
        else:
            distances = numbers
    print(times)
    print(distances)

    ways_to_win = []
    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])
        print(time)
        print(distance)
        number_of_ways_to_win = 0
        max_time = int(time) + 1
        for i in range(max_time):
            speed = i * 1
            moving_time = int(time) - i 
            attempt_distance = speed * moving_time 
            if attempt_distance > distance:
                number_of_ways_to_win += 1
            if i % 1000000 == 0:
                print("attempt {} out of {}".format(i, max_time))
                print("{} ways to win".format(number_of_ways_to_win))
        if number_of_ways_to_win > 0:
            ways_to_win.append(number_of_ways_to_win)
    product = 1
    for way in ways_to_win:
        product *= way
    print(product)

def part2():
    for l in f:
        line = l.strip()
        print(line)

part1()