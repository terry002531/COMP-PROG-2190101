class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        self.valueOrder = {
            "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "10": 8,
            "J": 9, "Q": 10, "K": 11, "A": 12, "2": 13
        }

        self.suitOrder = {
            "club": 1, "diamond": 2, "heart": 3, "spade": 4
        }

    def __str__(self):
        return f"({self.value} {self.suit})"

    def getScore(self):
        if self.value == 'A':
            return 1
        elif self.value in ['J', 'Q', 'K']:
            return 10
        else:
            return int(self.value)

    def sum(self, other):
        s = self.getScore() + other.getScore()
        s = s % 10
        return s

    def __lt__(self,rhs):
        if self.valueOrder[self.value] != self.valueOrder[rhs.value]:
            return self.valueOrder[self.value] < self.valueOrder[rhs.value]
        return self.suitOrder[self.suit] < self.suitOrder[rhs.suit]


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])