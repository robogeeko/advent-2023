f = open("day-8.txt", "r")

def part1():
    directions = "LRRRLRRRLRRLRRLRLRRLRRLRRRLRRLRRRLRRRLLRRRLRRRLRRRLRLRRLRRRLRLRRRLRRRLLRLRLRRLRRLLLRRLRRLRRRLLRRRLLRRRLRLRRRLRRRLLRRLRLLRLRRRLRRLRRLRLRLRLRLRLRRRLRLRRRLLRLRRLRRRLRRRLRLRRLRLLLRLRLRLRLRLRRRLLRRLRLRLLRRRLRRLRRRLRRLRRLRRRLLRRLRLRRLRRRLRRLRLRRLRLLRRLLRLRRRLRRLRLLRRRR"
    key_to_next = {}
    curr_key = None
    for l in f:
        line = l.strip()
        key, potentials = line.split(" = ")
        potentials = potentials.replace("(", "")
        potentials = potentials.replace(")", "")
        potential_a, potential_b = potentials.split(", ")
        if len(potential_a) != 3:
            raise Exception("a length too long")
        if len(potential_b) != 3:
            raise Exception("b length too long")
        key_to_next[key] = (potential_a, potential_b)
        if curr_key is None:
            curr_key = key

    curr_key = "AAA"
    print(key_to_next)
    num_steps = 0
    index = 0
    while True:
    # for direction in directions:
        direction = directions[index]
        if direction == "L":
            curr_key = key_to_next[curr_key][0]
        else:
            curr_key = key_to_next[curr_key][1]
        # print(curr_key)
        # input()
        num_steps += 1
        if num_steps % 1000000 == 0:
            print("Just hit {} steps. key: {}".format(num_steps, curr_key))
        if curr_key == "ZZZ":
            break
        index += 1
        if index == len(directions):
            index = 0
        
    print(num_steps)

# part1()

def part2():
    directions = "LRRRLRRRLRRLRRLRLRRLRRLRRRLRRLRRRLRRRLLRRRLRRRLRRRLRLRRLRRRLRLRRRLRRRLLRLRLRRLRRLLLRRLRRLRRRLLRRRLLRRRLRLRRRLRRRLLRRLRLLRLRRRLRRLRRLRLRLRLRLRLRRRLRLRRRLLRLRRLRRRLRRRLRLRRLRLLLRLRLRLRLRLRRRLLRRLRLRLLRRRLRRLRRRLRRLRRLRRRLLRRLRLRRLRRRLRRLRLRRLRLLRRLLRLRRRLRRLRLLRRRR"
    key_to_next = {}
    a_nodes = []
    for l in f:
        line = l.strip()
        key, potentials = line.split(" = ")
        potentials = potentials.replace("(", "")
        potentials = potentials.replace(")", "")
        potential_a, potential_b = potentials.split(", ")
        if len(potential_a) != 3:
            raise Exception("a length too long")
        if len(potential_b) != 3:
            raise Exception("b length too long")
        key_to_next[key] = (potential_a, potential_b)
        if key.endswith("A"):
            a_nodes.append(key)

    print(key_to_next)
    print(a_nodes)
    num_steps = 0
    index = 0
    a_node_index = 0
    while True:
    # for direction in directions:
        direction = directions[index]
        for a_node_index in range(len(a_nodes)):
            if direction == "L":
                a_nodes[a_node_index] = key_to_next[a_nodes[a_node_index]][0]
            else:
                a_nodes[a_node_index] = key_to_next[a_nodes[a_node_index]][1]
        # print(curr_key)
        # input()
        num_steps += 1
        if num_steps % 100000 == 0:
            print("Just hit {} steps. nodes: {}".format(num_steps, a_nodes))
            input()
        all_nodes_end_with_z = True
        for a_node_index in range(len(a_nodes)):
            if a_nodes[a_node_index].endswith("Z"):
                print("Node {} ends with Z, steps: {}".format(a_node_index, num_steps))
            if not a_nodes[a_node_index].endswith("Z"):
                all_nodes_end_with_z = False

        if all_nodes_end_with_z:
            break
        index += 1
        if index == len(directions):
            index = 0
        
    print(num_steps)

part2()

# Node 0 ends with Z, steps: 11309
# Node 2 ends with Z, steps: 12361
# Node 4 ends with Z, steps: 13939
# Node 3 ends with Z, steps: 16043
# Node 5 ends with Z, steps: 18673
# Node 1 ends with Z, steps: 19199
# Node 0 ends with Z, steps: 22618
# Node 2 ends with Z, steps: 24722
# Node 4 ends with Z, steps: 27878
# Node 3 ends with Z, steps: 32086
# Node 0 ends with Z, steps: 33927
# Node 2 ends with Z, steps: 37083
# Node 5 ends with Z, steps: 37346
# Node 1 ends with Z, steps: 38398

# node 0, every 11309
# node 1, every 19199
# node 2, every 12361
# node 3, every 16043
# node 4, every 13939
# node 5, every 18673

# LCM
# 8906539031197