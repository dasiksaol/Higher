import random

player = []
game_master = []
player_score = 0
game_master_score = 0

def draw_card():
    """Draw a card from the deck."""
    return random.randint(1, 10)

def start_hand():
    """Start a new hand by drawing two cards for both player and game master."""
    player.clear()
    game_master.clear()
    for _ in range(5):
        player.append(draw_card())
        game_master.append(draw_card())

def show_hands():
    """Display the hands of both player and game master."""
    print(f"Player's hand: {player}")
    print(f"Game Master's hand: {game_master}")

def get_player_choice():    
    """Prompt the user to pick a number from their hand."""
    while True:
        try:
            choice = int(input(f"Pick a number from your hand {player}: "))
            if choice in player:
                return choice
            else:
                print("Please pick a number from your hand.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def remove_card_from_hand(hand, card):
    """Remove a card from the specified hand."""
    if card in hand:
        hand.remove(card)
    else:
        print(f"Card {card} not found in hand.")

def play_round():
    """Play a round of the game."""
    if not player or not game_master:
        print("No cards left to play. Starting a new hand.")
        start_hand()
    
    player_card = get_player_choice()
    game_master_card = random.choice(game_master)
    
    print(f"Player plays: {player_card}")
    print(f"Game Master plays: {game_master_card}")
    
    remove_card_from_hand(player, player_card)
    remove_card_from_hand(game_master, game_master_card)
    
    score = calculate_score(player_card, game_master_card)
    if score == 1:
        print("Player wins this round!")
        print(f"Player Score: {player_score}, Game Master Score: {game_master_score}")
    elif score == -1:
        print("Game Master wins this round!")
        print(f"Player Score: {player_score}, Game Master Score: {game_master_score}")
    else:
        print("It's a tie!")
        print(f"Player Score: {player_score}, Game Master Score: {game_master_score}")
        
    if not player or not game_master:
        print("One of the hands is empty. Ending the game.")
        return False
    
    return True

def calculate_score(card1, card2):
    """Calculate the score based on the cards played."""
    if card1 > card2:
        player_score += 1  # Player wins this round
        return 1
    elif card1 < card2:
        game_master_score += 1  # Game Master wins this round
        return -1
    else:
        return 0  # Tie, no score change

def main():
    """Main function to run the game."""
    start_hand()
    show_hands()
    
    while True:
        if not play_round():
            break
        show_hands()

main()