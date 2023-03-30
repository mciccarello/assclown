import random

class Card(object):
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

trials = 1000000
matches = 0
random.seed()

for trial in range(1, trials):
    deck = []
    for suit in range(4):
        for rank in range(13):
            deck.append(Card(suit,rank))

    random.shuffle(deck)

    roll1 = random.randint(1,6) + random.randint(1,6)
    for i in range(0,roll1):
        card1 = deck.pop(0)

    roll2 = random.randint(1,6) + random.randint(1,6)
    for i in range(0,roll2):
        card2 = deck.pop(0)

    roll3 = random.randint(1,6) + random.randint(1,6)
    for i in range(0,roll3):
        card3 = deck.pop(0)

    if card3.rank == card1.rank and card3.suit == card2.suit:
        matches = matches + 1


print(f"trials:  {trials}  matches:  {matches} or 1 in {trials / matches}")

       






