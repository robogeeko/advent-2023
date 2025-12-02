f = open("day-15.txt", "r")

def process_line_to_steps(line):
    steps = []
    for step in line.split(","):
        steps.append(step)
    return steps

def process_step(step):
    curr_val = 0
    for char in step:
        curr_val += + ord(char)
        curr_val *= 17
        curr_val %= 256
    return curr_val

def part1():
    for l in f:
        line = l.strip()
        steps = process_line_to_steps(line)
    total_score = 0 
    for step in steps:
        total_score += process_step(step)
    print(total_score)

# part1()

# boxes = [
#     [(rn 1), (cm 2), ...],
#     ,...
# ]

def process_step_part_2(step, boxes):
    if "=" in step:
        split_step = step.split("=")
        label = split_step[0]
        focal_length = int(split_step[1])
        box_num = process_step(label)
        for index in range(len(boxes[box_num])):
            lens = boxes[box_num][index]
            if label == lens[0]:
                boxes[box_num][index] = (label, focal_length)
                return 
        boxes[box_num].append((label, focal_length))
    if "-" in step:
        label = step.split("-")[0]
        box_num = process_step(label)
        for index in range(len(boxes[box_num])):
            lens = boxes[box_num][index]
            if label == lens[0]:
                boxes[box_num].pop(index)
                return

def print_boxes(boxes):
    for index in range(len(boxes)):
        if len(boxes[index]) > 0:
            print("Box {}".format(index))
            print(boxes[index])

def part2():
    for l in f:
        line = l.strip()
        steps = process_line_to_steps(line)
    boxes = [[]  for i in range(256)]
    for step in steps:
        process_step_part_2(step, boxes)
        # print_boxes(boxes)
        # input()
    total_score = 0
    for index in range(len(boxes)):
        box = boxes[index]
        for lens_index in range(len(box)):
            total_score += (index + 1) * (lens_index + 1) * box[lens_index][1]
    print(total_score)

part2()