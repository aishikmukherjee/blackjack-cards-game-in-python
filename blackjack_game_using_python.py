import blackjack_game_using_python_art  # Import 'art' module to display the game's logo
import random  # Import 'random' module to pick cards randomly

# List of cards with values; 11 represents Ace, 10 represents face cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Dictionary to store the cards for the player and the dealer
game = { 'player' : [],  # Player's cards
         'dealer' : []   # Dealer's cards
}

# Deals with ace value
def adjust_ace(hand):
    """Adjusts the value of Ace (11) to 1 if the score exceeds 21."""
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1  # Change the first occurrence of 11 to 1

def pick_cards_for_dealer():
    """Picks one card at a time for the dealer and appends it to dealer's hand"""
    game['dealer'].append(random.choice(cards))
    adjust_ace(game['dealer']) # Adjust Ace value if needed

def pick_cards_for_player():
    """Picks one card at a time for the player and appends it to player's hand"""
    game['player'].append(random.choice(cards))
    adjust_ace(game['player']) # Adjust Ace value if needed

def loose_by_picking_exceeding_cards(score_of_player):
    """Checks if the player's score has exceeded 21 (bust)"""
    if score_of_player > 21:
        print("==============================================================")
        final_cards_shower()  # Show the final cards if player goes over 21
        print("\nYou lose as your score exceeds 21.")
        print("==============================================================")
        return True  # Player loses
    else:
        return False  # Player has not lost yet

def result_checker(score_of_player, score_of_dealer):
    """Checks and displays the final result of the game based on scores"""
    # Dealer must pick cards until their score is at least 17
    while score_of_dealer < 17:
        pick_cards_for_dealer()  # Dealer picks another card
        score_of_dealer = sum(game['dealer'])  # Recalculate dealer's score

    # Check various game outcomes
    if score_of_dealer > 21 and score_of_player < 22:
        print("==============================================================")
        final_cards_shower()  # Show final cards if dealer goes over 21
        print("\nDealer score exceeded 21, You win")
        print("==============================================================")

    elif score_of_player == score_of_dealer:
        print("==============================================================")
        final_cards_shower()  # Show final cards if the game is a draw
        print("\nDraw")
        print("==============================================================")

    elif score_of_dealer < score_of_player < 22:
        print("==============================================================")
        final_cards_shower()  # Player wins if their score is higher than dealer's
        print("\nYou win.")
        print("==============================================================")
    else:
        print("==============================================================")
        final_cards_shower()  # Dealer wins if their score is higher
        print("\nYou lose.")
        print("==============================================================")

def final_cards_shower():
    """Shows the final cards and scores for both the player and dealer"""
    print(f"\nYour final hand: {game['player']}, final score: {sum(game['player'])}")
    print(f"Computer's final hand: {game['dealer']},  final score: {sum(game['dealer'])}")

def in_game_card_shower():
    """Shows the current cards and scores during the game"""
    print(f"\nYour cards: {game['player']}, current score: {sum(game['player'])}")
    print(f"Computer's first card: {game['dealer'][0]}")  # Only shows one of the dealer's cards

def add_card_input_checker(input_to_check):
    """Checks if the player's input is valid when picking more cards"""
    if input_to_check != 'n' and input_to_check != 'y':
        # If the input is not 'y' or 'n', prompt again
        new_input = input(f"You typed '{input_to_check}', which is a wrong input."
                          f"\nType 'y' to get another card, type 'n' to pass: ")
        if new_input != 'n' and new_input != 'y':
            print("\nDue to multiple wrong inputs, the game has ended. Restart the program to play again.")
        else:
            return new_input  # Return the corrected input
    else:
        return input_to_check  # If input is valid, return it

def black_jack():
    """Main function to play Blackjack"""
    print(blackjack_game_using_python_art.logo)  # Display the game's logo

    # Reset the player's and dealer's hands for a new game
    game['player'] = []
    game['dealer'] = []

    # Deal two cards to both the player and dealer
    pick_cards_for_dealer()
    pick_cards_for_dealer()
    pick_cards_for_player()
    pick_cards_for_player()

    # Check if the player loses by going over 21
    if loose_by_picking_exceeding_cards(sum(game['player'])) is not True:
        add_card = True  # Flag to allow drawing additional cards
        while add_card is True:
            in_game_card_shower()  # Show current hands and scores
            choice_to_add_card = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
            choice_to_add_card = add_card_input_checker(choice_to_add_card)  # Validate the input
            if choice_to_add_card == 'y':
                pick_cards_for_player()  # Player picks another card
                # Check if the player has lost by going over 21
                if loose_by_picking_exceeding_cards(sum(game['player'])) is True:
                    add_card = False  # Stop drawing cards if the player busts
            else:
                result_checker(sum(game['player']), sum(game['dealer']))  # Show the final result
                add_card = False  # Stop drawing cards when the player passes

    # Ask if the player wants to replay the game
    restart = input("\nType 'yes' to replay the game"
                    "\nType anything else to quit the game"
                    "\nEnter choice: ").lower()
    if restart == 'yes':
        black_jack()  # Restart the game
    else:
        game_starter('n')  # Exit the game

def game_starter(input_to_check=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()):
    """Checks the player's input at the start of the game"""
    if input_to_check == 'n':
        print("\nGoodbye")  # Exit the game if the player chooses 'n'
        print(blackjack_game_using_python_art.credit_of_project) # prints credits of the project
        exit()
    elif input_to_check == 'y':
        black_jack()  # Start the game if the player chooses 'y'
    else:
        print("\nWrong input.")  # Handle invalid inputs
        game_starter(input("\nDo you want to restart the game of Blackjack? Type 'y' or 'n': ").lower())

# Start the game by calling the input checker
game_starter()
