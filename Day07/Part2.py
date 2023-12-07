import functools

total = 0

with open('Day07/input.txt', 'r') as file:
    data = [line for line in file]

inputs = [(x, int(y)) for (x, y) in (line.split() for line in data)]

cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def getCardVal(card):
    return len(cards) - cards.index(card)

def getMaxCard(hand):
    return cards[len(cards) - max([getCardVal(card) for card in hand])]

handType = {
    7: 'Five of a Kind',
    6: 'Four of a Kind',
    5: 'Full House',
    4: 'Three of a Kind',
    3: 'Two Pair',
    2: 'One Pair',
    1: 'High Card'

}

def getJokerHand(hand):
    highest = 0
    for card in set(hand):
        if card == 'J':
            continue
        tempHand = hand.replace('J', card)
        highest = max(highest, getHandType(tempHand))
    return highest

def getHandType(hand):
    uniqueSet = set(hand)
    x = []
    for unique in uniqueSet:
        cardCount = hand.count(unique)
        if cardCount != 1:
            x.append(cardCount)
    x.sort()
    if x == [5]:
        return 7
    elif x == [4]:
        return 6
    elif x == [2, 3]:
        return 5
    elif x == [3]:
        return 4
    elif x == [2, 2]:
        return 3
    elif x == [2]:
        return 2
    else:
        return 1


sortedHands = [[] for _ in range(len(handType.keys()))] 
for hand, bid in inputs:
    sortedHands[getJokerHand(hand)-1].append((hand, bid))

def compareHands(h1, h2):
    for card1, card2 in zip(h1[0], h2[0]):
        card1Val = getCardVal(card1)
        card2Val = getCardVal(card2)
        if card1Val > card2Val:
            return 1
        elif card1Val < card2Val:
            return -1
    return 0

rank = 1
for z in sortedHands:
    z = sorted(z, key=functools.cmp_to_key(compareHands))
    for hand in z:
        total += hand[1] * rank
        rank += 1

print(total)
