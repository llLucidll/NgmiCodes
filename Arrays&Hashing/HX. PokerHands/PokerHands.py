from collections import defaultdict

def value_checker(hand):
    '''
        [2,1,1,1]    pair
        [2,2,1]     2 pair
        [3,2]       three + pair
        [3,1,1]     three
        [4,1]       four
        [1,1,1,1,1] high/flush/straight/royal
    '''
    convert = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    count = {}
    suits = set()
    for card in hand:
        value, suit = card[0], card[1]
        if value in convert:
            value = convert[value]
        value = int(value)
        if suit not in suits:
            suits.add(suit)
        count[value] = count.get(value, 0) + 1
    
    freq = sorted(count.values(), reverse = True)
    values = sorted(count.keys())
    if freq == [2,1,1,1]:
        result = 2
    elif freq == [2,2,1]:
        result = 3
    elif freq == [3,1,1]:
        result = 4
    elif freq == [3,2]:
        result = 7
    elif freq == [4,1]:
        result = 8
    else:
        if len(suits) == 1:
            # Royal
            if values == [10, 11, 12, 13, 14]:
                result = 10
            # Straight Flush
            else:
                for i in range(1, len(values)):
                    if values[i] != values[i - 1] + 1:
                        result = 6 # Flush
                        break
                else:
                    result = 9
                

        else:
            # straight
            for i in range(1, len(values)):
                if values[i] != values[i - 1] + 1:
                    result = 0
                    break
            else:    
                result = 5

    return max(values), result

n = int(input())
hands = []

for i in range(n):
    hands.append(input().split(" "))

p1 = []
p2 = []

for i in range(n):
    p1.append(hands[i][:5])
    p2.append(hands[i][5:])

for i in range(n):
    p1_high, p1_score = value_checker(p1[i])
    p2_high, p2_score = value_checker(p2[i])

    if p1_score == p2_score:
        if p1_high > p2_high:
            win = 1 
        elif p2_high > p1_high:
            win = 2
        else:
            win = 0
    else:
        if p1_score > p2_score:
            win = 1
        else:
            win = 2

    if win == 1:
        print("Player 1")
    elif win == 2:
        print("Player 2")
    else:
        print("Tied Royal Flush")