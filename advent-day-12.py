from itertools import cycle
from copy import copy
from functools import lru_cache
f = open("day-12.txt", "r")

def is_schematic_valid(schematic, condition_list):
    new_list = copy(condition_list)
    condition = new_list.pop(0)
    currently_found = 0

    for character in schematic:
        if character == "#":
            currently_found += 1
        elif character == ".":
            if currently_found == 0:
                continue
            if currently_found != condition:
                return False
            if len(new_list) == 0:
                condition = 0
                currently_found = 0
            else:
                condition = new_list.pop(0)
                currently_found = 0

    if len(new_list) > 0:
        return False
    
    if currently_found != condition:
        return False
    
    return True

def find_all_possibilities(schematic, condition_list):
    possibilities = [""]
    for i in range(0, len(schematic)):
        if schematic[i] != "?":
            for j in range(len(possibilities)):
                possibilities[j] += schematic[i]
        else:
            length_of_possibilities = len(possibilities)
            for j in range(length_of_possibilities):
                new_possibility = copy(possibilities[j])
                new_possibility += "#"
                possibilities[j] += "."
                possibilities.append(new_possibility)
        print("went through {} out of {}".format(i, len(schematic)))
    count_valid_possibilities = 0
    index = 0
    for possibility in possibilities:
        if is_schematic_valid(possibility, condition_list):
            print(possibility)
            count_valid_possibilities += 1
        if index % 100000 == 0:
            print("Checking possibility {} out of {}".format(index, len(possibilities)))
        index += 1
    return count_valid_possibilities

def part1():
    schematics = []
    condition_lists = []
    for l in f:
        line = l.strip()
        schematic, group = line.split()
        schematics.append(list(schematic))
        condition_lists.append(
            list(
                map(lambda x: int(x), group.split(","))
            )
        )
    
    total_possible_arrangements = 0
    for i in range(0, len(schematics)):
        total_possible_arrangements += find_all_possibilities(schematics[i], condition_lists[i])
        print("Checking arrangement {}".format(i))

    print(total_possible_arrangements)

# part1()

@lru_cache(maxsize=None)
def find_all_possibilities_improved(schematic, condition_list):
    # print("schematic: {}, condition_list: {}".format(schematic, condition_list))
    # input()
    if len(schematic) == 0 and len(condition_list) == 0:
        # print("found a valid one, here 1")
        return 1
    if len(schematic) == 0 and len(condition_list) > 0:
        # print("found an invalid one, here 2")
        return 0
    if schematic[0] == ".":
        # for something like .#.#.#, 1,2,3 , we can just skip the first one -> #.#.#, 1,2,3
        return find_all_possibilities_improved(schematic[1:], condition_list)
    if schematic[0] == "?":
        # if it's something like ?#.#.#, 1,2,3 , we should branch and try both possibilities
        # ?#.#.#, 1,2,3 -> ##.#.#, 1,2,3 and .#.#.#, 1,2,3
        pound_list = list(copy(schematic))
        pound_list[0] = "#"
        first_branch = find_all_possibilities_improved(tuple(pound_list), condition_list)
        dot_list = list(copy(schematic))
        dot_list[0] = "."
        second_branch = find_all_possibilities_improved(tuple(dot_list), condition_list)
        # print("for schematic: {}, condition_list: {}, possibilities: {}".format(schematic, condition_list, first_branch + second_branch))
        return first_branch + second_branch
    if schematic[0] == "#":
        # if it's something like ## , [], it means we need to count but we ran out of numbers so it is invalid
        if len(condition_list) == 0:
            # print("found an invalid one, here 3")
            return 0
        # if it's something like ##, 4 it also means we ran out
        if len(schematic) < condition_list[0]:
            # print("found an invalid one, here 4")
            return 0
        # if it's something like ## , 1,2,3, it also breaks because we need it to be a 2 but it's a 1
        if len(schematic) > condition_list[0]:
            # this returns 0 if it is like - #.#, 2,2,3 -> schematic[1] == . so it does not work
            for i in range(0, condition_list[0]):
                if schematic[i] == ".":
                    # print("found an invalid one, here 5")
                    return 0
            # this returns 0 if it is like ###, 2,2,3 -> schematic[2] == # so it does not work
            if schematic[condition_list[0]] == "#":
                # print("found an invalid one, here 6")
                return 0
            # finally, we should recur!
            # skip one more in case the next one is a ?. it needs to always be a "." so we dont need to branch
            return find_all_possibilities_improved(schematic[condition_list[0] + 1:], condition_list[1:])
        elif len(schematic) == condition_list[0] and len(condition_list) == 1:
            # we repeat a check from above, but afterwards we need to check if schematic length is 0. 
            # this returns 0 if it is like - #.#, 2,2,3 -> schematic[1] == . so it does not work
            for i in range(0, condition_list[0]):
                if schematic[i] == ".":
                    # print("found an invalid one, here 6")
                    return 0
            # print("found a valid one, here 7")
            return 1
        elif len(schematic) == condition_list[0] and len(condition_list) > 1:
            # This fixes ?,? , 2,1
            # print("found an invalid one, here 8")
            return 0
    raise Exception("if we get here it's a bug")
            
        

def part2():
    schematics = []
    condition_lists = []
    for l in f:
        line = l.strip()
        schematic, group = line.split()
        initial_condition_list = list(
            map(lambda x: int(x), group.split(","))
        )
        total_cycles = len(initial_condition_list) * 5
        expanded_condition_list = []
        iter_count = 0 
        for condition in cycle(initial_condition_list):
            expanded_condition_list.append(condition)
            iter_count += 1
            if iter_count == total_cycles:
                break
        condition_lists.append(expanded_condition_list)
        # condition_lists.append(initial_condition_list)

        expanded_schematic = []
        for i in range(5):
            for character in schematic:
                expanded_schematic.append(character)
            if i != 4:
                expanded_schematic.append("?")
        schematics.append(list(expanded_schematic))
        # schematics.append(list(schematic))

    total_possible_arrangements = 0
    for i in range(0, len(schematics)):
        # print("Checking arrangement {} out of {}".format(i, len(schematics)))
        possibilities =  find_all_possibilities_improved(tuple(schematics[i]), tuple(condition_lists[i]))
        # print("Found {} possibilities for arrangement {}".format(possibilities, i))
        # print("cache stats: {}".format(find_all_possibilities_improved.cache_info()))
        total_possible_arrangements += possibilities
        # input()

    print("cache stats: {}".format(find_all_possibilities_improved.cache_info()))
    print(total_possible_arrangements)

part2()
