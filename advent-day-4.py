f = open("day-4.txt", "r")

def parse_numbers(number_list):
    final_list = []
    numbers = number_list.split(" ")
    for number in numbers:
        if number.isdigit():
            final_list.append(int(number))
    return final_list

def part1():
    total_score = 0 
    for l in f:
        line = l.strip()
        card_number, card_values = line.split(":")
        card_values = card_values.strip()
        winning_numbers, numbers_you_have = card_values.split("|")
        winning_numbers = winning_numbers.strip()
        numbers_you_have = numbers_you_have.strip()

        winning_num_list = parse_numbers(winning_numbers)
        you_have_list = parse_numbers(numbers_you_have)

        winning_set = set(winning_num_list)
        score = 0
        for num_you_have in you_have_list:
            if num_you_have in winning_set:
                if score == 0:
                    score += 1
                else:
                    score = score * 2
        total_score += score
    print(total_score)


def process_cards(cards, num_cards):
    for index in range(1, len(cards)):
        num_matches = 0
        winning_nums = cards[index]["winners"]
        you_have = cards[index]["you_have"]
        for number in you_have:
            if number in winning_nums:
                num_matches += 1
        print("index: {}, matches: {}".format(index, num_matches))
        for match_index in range(1, num_matches + 1):
            num_cards[index + match_index] += num_cards[index]
    
    print(num_cards)
    score = 0
    for index in range(len(num_cards)):
        score += num_cards[index]
    print(score)
    return score

def part2():
    total_score = 0 
    cards = []
    num_cards = []
    num_cards.append(0)
    cards.append({})
    for l in f:
        line = l.strip()
        card_number, card_values = line.split(":")
        card_index = int(card_number.strip().split(" ")[-1].strip())
        card_values = card_values.strip()
        winning_numbers, numbers_you_have = card_values.split("|")
        winning_numbers = winning_numbers.strip()
        numbers_you_have = numbers_you_have.strip()

        winning_num_list = parse_numbers(winning_numbers)
        you_have_list = parse_numbers(numbers_you_have)
        cards.append({"winners": winning_num_list, "you_have": you_have_list})
        num_cards.append(1)

    print(process_cards(cards, num_cards))

part2()