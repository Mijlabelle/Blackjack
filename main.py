
import random
from replit import clear
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card




def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    elif 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
        print(sum(cards))
        return sum(cards)
    else:
        return sum(cards)


def compare(user_score, computer_score):

    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose opponent has blackjack."
    elif user_score == 0:
        return "Blackjack. You win."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


def play_game():

    print(logo)

    
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(user_score)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f" Computers first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal_again = input(
                "Type 'Y' to get another card. Type 'N' to pass.")
            if deal_again == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(
        f" Your final hand is {user_cards}, your final score is {user_score}")
    print(
        f" Computers final hand: {computer_cards}, final score: {computer_score}"
    )
    print(compare(user_score, computer_score))


while input(
        "Do you want to play a game of blackjack? Type 'Y' for yes. Type 'N' for no."
) == 'y':

    clear()

    play_game()


