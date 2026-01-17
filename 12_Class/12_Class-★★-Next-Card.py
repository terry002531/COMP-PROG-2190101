class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        self.s1 = {
            'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
            '10':10,'J':11,'Q':12,'K':13
        }
        self.s2 = {
            'club':1,'diamond':2,'heart':3,'spade':4
        }
        self.s3 = {
            1:'A',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',
            10:'10',11:'J',12:'Q',13:'K'
        }
        self.s4 = {
            1:'club',2:'diamond',3:'heart',4:'spade',
        }


    def __str__(self):
        return f"({self.value} {self.suit})"

    def next1(self):
        w1,w2 = self.value, self.suit
        w1a,w2a = self.s1[w1], self.s2[w2]
        if w2a == 4:
            w1a += 1
            w2a = 1
        else:
            w2a += 1
        if w1a > 13:
            w1a -= 13
        w1b = self.s3[w1a]
        w2b = self.s4[w2a]
        return f"({w1b} {w2b})"

    def next2(self):
        w1, w2 = self.value, self.suit
        w1a, w2a = self.s1[w1], self.s2[w2]
        if w2a == 4:
            w1a += 1
            w2a = 1
        else:
            w2a += 1
        if w1a > 13:
            w1a -= 13
        w1b = self.s3[w1a]
        w2b = self.s4[w2a]
        self.value = w1b
        self.suit = w2b

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
