f = open("day-7.txt", "r")

hand_types_to_rank= {
    "FiveOfAKind": 1,
    "FourOfAKind": 2,
    "FullHouse": 3,
    "ThreeOfAKind": 4,
    "TwoPair": 5,
    "OnePair": 6,
    "HighCard": 7
}

cards_to_value = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14,
}

def classify_hand(hand):
    if hand == "JJJJJ":
        return "FiveOfAKind"
    j_counts = 0
    char_counts = {}
    for character in hand:
        if character != "J":
            if character not in char_counts:
                char_counts[character] = 1
            else:
                char_counts[character] += 1
        else:
            j_counts += 1
    list_counts = []
    for character, count in char_counts.items():
        list_counts.append(count)
    list_counts.sort(reverse=True)
    if j_counts > 0:
        list_counts[0] += j_counts
    if list_counts == [2, 2, 1]:
        return "TwoPair"
    elif list_counts == [5]:
        return "FiveOfAKind"
    elif list_counts == [1, 1, 1, 1, 1]:
        return "HighCard"
    elif list_counts == [4, 1]:
        return "FourOfAKind"
    elif list_counts == [3, 2]:
        return "FullHouse"
    elif list_counts == [3, 1, 1]:
        return "ThreeOfAKind"
    elif list_counts == [2, 1, 1, 1]:
        return "OnePair"
    raise Exception("Hand type not expected {}".format(hand))

# is hand1 bigger?
def is_hand1_better(hand1, hand2):
    hand1_type = classify_hand(hand1)
    hand2_type = classify_hand(hand2)
    hand1_rank = hand_types_to_rank[hand1_type]
    hand2_rank = hand_types_to_rank[hand2_type]
    # print("hand1: {}, hand2: {}, hand1_type: {}, hand2_type: {}, hand1_rank: {}, hand2_rank: {}".format(hand1, hand2, hand1_type, hand2_type, hand1_rank, hand2_rank))
    if hand1_rank < hand2_rank:
        return True
    elif hand2_rank < hand1_rank:
        return False 
    else:
        for i in range(len(hand1)):
            # print("hand1: {}, hand2: {}, v1: {}, v2: {}".format(hand1[i], hand2[i], cards_to_value[hand1[i]], cards_to_value[hand2[i]]))
            if cards_to_value[hand1[i]] > cards_to_value[hand2[i]]:
                return True
            elif cards_to_value[hand1[i]] < cards_to_value[hand2[i]]:
                return False
        raise Exception("Hands look equal {} {}".format(hand1, hand2))

def part1():
    hand_to_bid = {}
    hands_ranked = []
    for l in f:
        line = l.strip()
        split_line = line.split()
        hand = split_line[0]
        bid = split_line[1]
        hand_to_bid[hand] = bid
        if len(hands_ranked) == 0:
            hands_ranked.append(hand)
            continue
        insertion_index = len(hands_ranked)
        for index in range(len(hands_ranked)):
            if is_hand1_better(hand, hands_ranked[index]):
                insertion_index = index
                break
        # print("{}, {}".format(hand, insertion_index))
        hands_ranked.insert(insertion_index, hand)
        # print("{}".format(hands_ranked))
        # input()
    rank = len(hands_ranked)
    total_winnings = 0
    for hand in hands_ranked:
        total_winnings += rank * int(hand_to_bid[hand])
        rank -= 1
    print(total_winnings)

part1()



# def part2():
#     for l in f:
#         line = l.strip()
#         print(line)

# part2()