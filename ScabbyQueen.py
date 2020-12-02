import playingCard as pc

minimumQueen = 1

def removeQueens():
    count = 0
    deck = pc.generateDeck()
    shuffledDeck = pc.shuffleCards(deck)
    for card in shuffledDeck:
        if card[-1] == "Q":
            shuffledDeck.remove(card)
            count += 1
        if count == (4 - minimumQueen):
            break
    return shuffledDeck
