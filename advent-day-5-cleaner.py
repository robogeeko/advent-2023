import time
all_mins = []
if __name__ == '__main__': 
    from concurrent.futures import ProcessPoolExecutor
    f = open("day-5.txt", "r")

    def attempted_solve(maps, seed0, seed1):
        min_val = None
        index = 0
        
        
        start_seed = seed0
        end_seed = seed0 + seed1
        interval = 100

        min_found_at = None
        length = end_seed - start_seed
        for seed in range(start_seed, end_seed, interval):
            index += interval
            next_val = seed
            # print("seed: {}".format(seed))
            for map in maps:
                for individual_map in map:
                    if individual_map[1] <= next_val <= individual_map[1] + individual_map[2]:
                        next_val = (next_val - individual_map[1]) + individual_map[0]
                        break
                # print("next_val: {}".format(next_val))
            if min_val is None or next_val < min_val:
                min_val = next_val
                print("FIRST LOOP: seed: {}. new min found!: {}, index: {}".format(seed, min_val, index))
                min_found_at = seed
        all_mins.append(min_val)

        start_seed = min_found_at - 10000
        end_seed = start_seed + 20000
        interval = 1

        min_val = None
        index = 0
        length = end_seed - start_seed
        for seed in range(start_seed, end_seed, interval):
            index += interval
            next_val = seed
            # print("seed: {}".format(seed))
            for map in maps:
                for individual_map in map:
                    if individual_map[1] <= next_val <= individual_map[1] + individual_map[2]:
                        next_val = (next_val - individual_map[1]) + individual_map[0]
                        break
                # print("next_val: {}".format(next_val))
            if min_val is None or next_val < min_val:
                min_val = next_val
                print("SECOND LOOP: seed: {}. new min found!: {}, index: {}".format(seed, min_val, index))
        all_mins.append(min_val)

    def part1():
        seeds = []
        map_index = -1
        maps = []
        for l in f:
            line = l.strip()
            if line == "":
                continue
            if line.startswith("seeds: "):
                num_strings = line.split(" ")[1:]
                for num_string in num_strings:
                    seeds.append(int(num_string))
            else:
                if "map:" in line:
                    map_index += 1
                    maps.append([])
                else:
                    numbers = []
                    nums = line.split(" ")
                    for num in nums:
                        numbers.append(int(num))
                    maps[map_index].append(numbers)
            # print(line)

        for index in range(0, len(seeds), 2):
            print("-----")
            attempted_solve(maps, seeds[index], seeds[index + 1])
        print(all_mins)
        print(min(all_mins))

    part1()

# mins:
# 3347258382
# 450342284
# 100165135 current
# 1225674485 X
# 1225671459
# 233808685
# 643133711
# 178139714
# 291773951
# 121228757
# 121228757
# 121229625
# 100165128
