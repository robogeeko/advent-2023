if __name__ == '__main__': 
    from concurrent.futures import ProcessPoolExecutor
    f = open("day-5.txt", "r")

    def process_function(start_seed, end_seed, pool_index, maps):
        print("starting process for pool: {}".format(pool_index))
        min_val = None
        index = 0
        length = end_seed - start_seed
        for seed in range(start_seed, end_seed):
            index += 1
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
            if index % 10000 == 0:
                print("Pool: {}. {} out of {}. min: {}".format(pool_index, index, length, min_val))

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

        print(seeds[0])
        print(seeds[1])
        print(seeds[1] // 4)
        interval = seeds[1] // 4
        with ProcessPoolExecutor(max_workers=4) as exe:
            # process_function(start_seed, end_seed, pool_index, maps)
            start_seed = seeds[0]
            end_seed = seeds[0] + interval
            for i in range(4):
                exe.submit(process_function, start_seed, end_seed, i, maps)
                start_seed += interval


        # new_seeds = []
        # for i in range(0,2,2):
        #     for j in range(0, seeds[i+1]):
        #         new_seeds.append(seeds[i] + j)

    # map1 is the old one
    # map2 is the new one
    def do_maps_overlap(map1, map2):
        map1_min = map1[0]
        map1_max = map1[0] + map1[2] - 1

        map2_min = map2[1]
        map2_max = map2[1] + map2[2] - 1
        return map1_min <= map2_max and map2_min <= map1_max

    # map1 is old
    # map2 is the new map

    # [50, 98, 2]
    # [0, 15, 37] -> [[35, 98, 2], [0, 15, 35]]

    # [50, 98, 3]
    # [0, 15, 37] -> [[35, 98, 2], [0, 15, 35], [53, 100, 1]]

    # [50, 1, 5], [100, 50, 5] -> [100, 1, 5]

    # [50, 1, 5], [100, 45, 10] -> 

    def return_simplified_maps(old, new):
        old_origin_range = (old[1], old[1] + old[2])
        old_dest_range = (old[0], old[0] + old[2])
        new_origin_range = (new[1], new[1] + new[2])
        new_dest_range = (new[0], new[0] + new[2])

        print(old_origin_range)
        print(old_dest_range)
        print(new_origin_range)
        print(new_dest_range)

        flattened_maps = []

        if old_dest_range[1] == new_origin_range[1] and old_dest_range[0] == new_origin_range[0]:
            flattened_maps.append(
                [new[0], old[1], old[2]]
            )
        if old_dest_range[0] >= new_origin_range[0] and old_dest_range[1] <= new_origin_range[1]:
            lower_overlap = old_dest_range[0] - new_origin_range[0] 
            upper_overlap = new_origin_range[1] - old_dest_range[1] 
            if lower_overlap > 0:
                flattened_maps.append(
                    [new[0], new[1], lower_overlap]
                )
            flattened_maps.append(
                [new[0] + lower_overlap, new[1], old[2]]
            )
            if upper_overlap > 0:
                flattened_maps.append(
                    [new[0] + lower_overlap + old[2], new_origin_range[1], upper_overlap - 1]
                )
            
        
        print(flattened_maps)



    # return_simplified_maps([50, 1, 5], [100, 42, 20])

    def part2():
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

        simplified_maps = []
        map_index = 0
        for map in maps:
            for individual_map in map:
                if len(simplified_maps) == 0 or map_index == 0:
                    simplified_maps.append(individual_map)
                else:
                    no_maps_overlap = True
                    for simplified_map in simplified_maps:
                        if do_maps_overlap(simplified_map, individual_map):
                            print(simplified_maps)
                            print(simplified_map)
                            print(individual_map)
                            new_maps = return_simplified_maps(simplified_map, individual_map)
                            print(new_maps)
                            input()
                            
                            no_maps_overlap = False
                    if no_maps_overlap:
                        simplified_maps.append(individual_map)
            map_index += 1
                            


        print(seeds)
        new_seeds = []
        for i in range(0,2,2):
            for j in range(0, seeds[i+1]):
                new_seeds.append(seeds[i] + j)

        # print(new_seeds)

        min_val = None
        for seed in new_seeds:
            next_val = seed
            # print("seed: {}".format(seed))
            for map in maps:
                for individual_map in map:
                    if individual_map[1] <= next_val <= individual_map[1] + individual_map[2] - 1:
                        next_val = (next_val - individual_map[1]) + individual_map[0]
                        break
                # print("next_val: {}".format(next_val))
            if min_val is None or next_val < min_val:
                min_val = next_val

        print(min_val)

    part1()
