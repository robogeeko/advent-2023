f = open("day-2.txt", "r")

bag = {
  "red": 12,
  "green": 13,
  "blue": 14
}

def part1():
  sum = 0

  for line in f:
    has_wrong = False
    find_index = line.split(" ")
    game_index = int(find_index[1][:len(find_index[1])-1])
    find_plays = line.split(":")
    plays = find_plays[1].strip().split(";")
    for play in plays:
      stone_types = play.strip().split(", ")
      for stone_type in stone_types:
        number_of_stones, color_of_stone = stone_type.split(" ")
        num_stones = int(number_of_stones)
        if color_of_stone not in bag:
          has_wrong = True
        if num_stones > bag[color_of_stone]:
          has_wrong = True
    if has_wrong is False:
      sum += game_index
  print(sum)

def part2():
  sum = 0
  for line in f:
    max_stones = {
      "red": 0,
      "green": 0,
      "blue": 0
    }
    find_index = line.split(" ")
    game_index = int(find_index[1][:len(find_index[1])-1])
    find_plays = line.split(":")
    plays = find_plays[1].strip().split(";")
    for play in plays:
      stone_types = play.strip().split(", ")
      for stone_type in stone_types:
        number_of_stones, color_of_stone = stone_type.split(" ")
        num_stones = int(number_of_stones)
        if num_stones > max_stones[color_of_stone]:
          max_stones[color_of_stone] = num_stones
    power = max_stones["red"] * max_stones["blue"] * max_stones["green"]
    sum += power
  print(sum)

part2()