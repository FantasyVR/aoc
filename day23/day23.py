def day23P1():
    pullzle = "463528179"
    #pullzle = "389125467"
    cups = [int(x) for x in list(pullzle)]

    l = len(cups)
    startIdx = 0
    for i in range(100):
        p1 = (startIdx + 1) % l
        p2 = (startIdx + 2) % l
        p3 = (startIdx + 3) % l
        p4 = (startIdx + 4) % l
        pickup = [cups[p1], cups[p2], cups[p3]]
        destination = cups[startIdx] - 1
        nextCup = cups[p4]
        # find destination number
        while destination in pickup and destination > 0:
            destination -= 1
        if destination == 0:
            destination = 9
            while destination in pickup and destination > 0:
                destination -= 1

        print(f"----move {i+1}----")
        print(f"cups: {cups}")
        print(f"current cup: {cups[startIdx]}")
        print(f"pick up: {pickup}")
        print(f"destination: {destination}")

        for j in range(3):
            cups.remove(pickup[j])

        desIdx = cups.index(destination)
        # add pickup into cups
        cups = cups[:desIdx+1] + pickup + cups[desIdx+1:]
        # find new start
        startIdx = cups.index(nextCup)

    index1 = cups.index(1)
    return cups[index1+1:] + cups[:index1]


class Cup(object):
    def __init__(self, cupNum):
        self.cupNum = cupNum
        self.next = None
        self.pre = None


class CycleList(object):
    def __init__(self):
        self.root = Cup(0)
        self.current = self.root

    def construct(self, cups):
        if len(cups) == 0:
            print("Wrong Cups")
        self.root = Cup(cups[0])
        self.current = self.root
        for i in range(1,len(cups)):
            cup = Cup(cups[i])
            self.current.next = cup
            cup.pre = self.current
            self.current = cup
        self.current.next = self.root
        self.current = self.root

    def traverse(self):
        current = self.current
        while current.next != self.current:
            if current.cupNum == 1:
                self.current = current
                break
            current = current.next
        print(self.current.next.cupNum, self.current.next.next.cupNum)
        print(self.current.next.cupNum * self.current.next.next.cupNum)

        current = self.current
        while current.next != self.current:
            print(current.cupNum)
            current = current.next
        print(current.cupNum)

    def printList(self):
        current = self.current
        while current.next != self.current:
            print(current.cupNum, end = ' ')
            current = current.next
        print(current.cupNum)

    def remove(self, current):
        pickup = []
        for i in range(3):
            nextCup = current.next
            pickup.append(nextCup.cupNum)
            current.next = nextCup.next
        return pickup

    def add(self, current, pickups):
        for i in reversed(range(3)):
            cup = Cup(pickups[i])
            cup.next = current.next
            cup.pre = current
            current.next = cup
    def findDest(self, dest):
        current = self.current
        while current.cupNum != dest:
            current = current.next
        return current

    def move(self, numMoves, maxNum):
        for i in range(numMoves): # ten millision iteration
            print(f"----move {i + 1}----")
            #print(f"cups: ", end = ' ')
            #self.printList()
            pickup = self.remove(self.current)
            #print(f"current cup: {self.current.cupNum}")
            #print(f"pick up: {pickup}")
            destination = self.current.cupNum - 1
            # find destination number
            while destination in pickup and destination > 0:
                destination -= 1
            if destination == 0:
                destination = maxNum # one millision numbers
                while destination in pickup and destination > 0:
                    destination -= 1
            #print(f"destination: {destination}")

            des = self.findDest(destination)
            self.add(des, pickup)
            self.current = self.current.next

def day23P2():
    numMoves = 10000000
    numCups = 1000000
    maxNum = numCups
    pullzle = "463528179"
    pullzle = "389125467"
    init = [int(x) for x in list(pullzle)]
    cups = [x for x in range(numCups)]
    for i in range(len(init)):
        cups[i] = init[i]
    cycle = CycleList()
    cycle.construct(cups)
    cycle.move(numMoves, maxNum)
    cycle.traverse()

if __name__ == "__main__":
    #value = day23P1()
    #print(value)
    day23P2()