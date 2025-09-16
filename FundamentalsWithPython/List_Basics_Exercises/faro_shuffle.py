deck_of_cards = input().split(" ")
count_of_shuffles = int(input())

for _ in range(count_of_shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    first_half = deck_of_cards[:middle_of_deck]
    second_half = deck_of_cards[middle_of_deck:]

    shuffled_deck = []
    for idx in range(middle_of_deck):
        shuffled_deck.append(first_half[idx])
        shuffled_deck.append(second_half[idx])

    deck_of_cards = shuffled_deck

print(deck_of_cards)