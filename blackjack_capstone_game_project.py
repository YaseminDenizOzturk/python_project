import random
def deal_card():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selected_card = random.choice(cards)
    return selected_card


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0


# 11 olan kartı toplam 21 den büyükse 1 olarak değiştiriyorum.    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
# remove fonksiyonu seçtiğimiz elemanı kaldırır.
# sum fonkiyonu toplamı verir.

def compare(user_score, cmp_score):

    if user_score == cmp_score:
        return "draw"
    elif cmp_score == 0:
        return "lose,opponent has Blackjack!"
    elif user_score == 0:
        return "win with a Blackjack!"
    elif user_score > 21:
        return "you went over,you lose"
    elif cmp_score > 21:
        return "opponent went over,you win"
    elif user_score > cmp_score:
        return "you win"
    else:
        return "you lose"
    

def play_game():

    user_cards = []
    cmp_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        cmp_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        cmp_score = calculate_score(cmp_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {cmp_cards[0]}")

        if user_score == 0 or cmp_score == 0 or user_score > 21:
            is_game_over = True
        else:

            user_should_deal = input(
                "Type 'Y' to get another card, type 'N' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while cmp_score != 0 and cmp_score < 17:
        cmp_cards.append(deal_card())
        cmp_score = calculate_score(cmp_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"   Computer's final hand: {cmp_cards}, final score: {cmp_score}")
    print(compare(user_score, cmp_score))


while input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").lower() == "y":
  play_game()
 