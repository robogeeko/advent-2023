# Day 1!
f = open("day-1.txt", "r")

digit_map = {
  "o": { "n": { "e": 1 } },
  "t": { "w": { "o": 2 },
    "h": { "r": { "e": { "e": 3 } } }
  },
  "f": { "o": { "u": { "r" : 4 } },
    "i": { "v": { "e": 5 } }
  },
  "s": { "i": { "x": 6 },
    "e": { "v": { "e": { "n": 7 } } } },
  "e": { "i": { "g": { "h": { "t": 8 } } } },
  "n": { "i": { "n": { "e": 9 } } }
}

def check_word(line, index, curr_map):
  if line[index] not in curr_map:
    return None
  if isinstance(curr_map[line[index]], int):
    return curr_map[line[index]]
  if index + 1 >= len(line):
    return None
  return check_word(line, index + 1, curr_map[line[index]])

sum = 0
for line in f:
  number_to_add = None
  first_number = None
  final_number = None

  for index in range(len(line.strip())):
    c = line[index]
    if not c.isdigit():
      checked_word = check_word(line.strip(), index, digit_map)
      if checked_word is not None:
        if first_number == None:
          first_number = checked_word 
        else:
          final_number = checked_word 
    else:
      if first_number == None:
        first_number = int(c) 
      else:
        final_number = int(c) 
  if final_number is None:
    number_to_add = first_number * 10 + first_number
  else:
    number_to_add = first_number * 10 + final_number
  sum += number_to_add
print(sum)