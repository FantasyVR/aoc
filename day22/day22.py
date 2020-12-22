def readFile(filepath):
    file = open(filepath,"r")
    player1 = []
    player2 = []
    p1 = False
    p2 = False
    lines = [line.strip("\n") for line in file.readlines()]
    for i in range(len(lines)):
        if "Player 1" in lines[i]:
            p1 = True
        elif "Player 2" in lines[i]:
            p1 = False
            p2 = True
        elif lines[i] == '':
            continue
        elif p1:
            player1.append(int(lines[i]))
        elif p2:
            player2.append(int(lines[i]))
    return player1, player2


def day22P1(cards1, cards2):
    numCards = len(cards1) + len(cards2)
    while len(cards1) != numCards and len(cards2) != numCards:
        c1 = cards1[0]
        c2 = cards2[0]
        if c1 > c2:
            cards1 = cards1[1:] + [c1, c2]
            cards2 = cards2[1:]
        else:
            cards2 = cards2[1:] + [c2, c1]
            cards1 = cards1[1:]
    cards = []
    if len(cards1) == numCards:
        cards = cards1
    else:
        cards = cards2

    sum = 0
    for i in range(numCards):
        sum += (numCards - i) * cards[i]
    return sum

def day22P2(cards1, cards2, depth = 0):
    numCards = len(cards1) + len(cards2)
    initCard1 = [x for x in cards1]
    initCard2 = [x for x in cards2]
    depth += 1
    winner = -1
    print(f"========Game {depth} ========")
    round = 0
    c1RoundList = []
    c2RouddList = []
    while len(cards1) != numCards and len(cards2) != numCards:
        if round > 0 and (cards1 in c1RoundList or cards2 in c2RouddList):
            c1RoundList = []
            c2RouddList = []
            print("Loop Hit")
            return [], 1
        round += 1
        c1 = cards1[0]
        c2 = cards2[0]
        numC1 = len(cards1) - 1
        numC2 = len(cards2) - 1
        print(f"---------Round {round} (Game {depth})-----")

        print("player 1's deck: ", cards1)
        print("player 2's deck: ", cards2)
        print("init card 1: ", initCard1)
        print("init card 2: ", initCard2)
        print("player 1 play: ", c1)
        print("player 2 play: ", c2)

        if c1 <= numC1 and c2 <= numC2:
            tc1 = [cards1[i] for i in range(1,1+c1)]
            tc2 = [cards2[i] for i in range(1,1+c2)]
            card, idx = day22P2(tc1, tc2, depth)
            if idx == 1: # player 1 win
                c1RoundList.append(cards1)
                c2RouddList.append(cards2)
                cards1 = cards1[1:] + [c1, c2]
                cards2 = cards2[1:]
                winner = 1
            else: # player 2 win
                c1RoundList.append(cards1)
                c2RouddList.append(cards2)
                cards2 = cards2[1:] + [c2, c1]
                cards1 = cards1[1:]
                winner = 2
        elif c1 > c2:
            c1RoundList.append(cards1)
            c2RouddList.append(cards2)
            cards1 = cards1[1:] + [c1, c2]
            cards2 = cards2[1:]
            winner = 1
        else:
            c1RoundList.append(cards1)
            c2RouddList.append(cards2)
            cards2 = cards2[1:] + [c2, c1]
            cards1 = cards1[1:]
            winner = 2

        print(f"Player {winner} wins round {round} of game {depth}")
        print("\n\n")

    idx = 1 if len(cards1) == numCards else 2
    cards = cards1 if len(cards1) == numCards else cards2
    return cards, idx

if __name__ == "__main__":
    play1, play2 = readFile("./input")
    print("player 1")
    print(play1)
    print("player 2")
    print(play2)
    value = day22P1(play1,play2)
    print(value)
    cards, idx = day22P2(play1,play2)
    sum = 0
    for i in range(len(cards)):
        sum += (len(cards) - i) * cards[i]
    print("problem 2: ",sum)