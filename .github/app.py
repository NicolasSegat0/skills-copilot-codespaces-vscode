import random 

def get_computer_choice(): 
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice): 
    if player_choice == computer_choice: 
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'scissors' and computer_choice == 'paper') or (player_choice == 'paper' and computer_choice == 'rock'): 
        return 'win'
    else: 
        return 'lose'
    

def paly_round():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while player_choice not in ['rock', 'paper', 'scissors']: 
        print("Invalid choice! Please choose rock, paper or scissors.")
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    computer_choice = get_computer_choice()

    result = determine_winner(player_choice, computer_choice)

    if result == 'win': 
        print("You win this round!")
    elif result == 'lose':
        print("You lose this round!")
        return -1
    else:
        print("This round is a tie!")
        return 0

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    player_score = 0
    play_again = 'yes'
    
    while play_again == 'yes':
        result = play_round()
        player_score += result
        play_again = input("Do you want to play again? (yes or no): ").lower()
        while play_again not in ['yes', 'no']:
            print("Invalid choice! Please answer yes or no.")
            play_again = input("Do you want to play again? (yes or no): ").lower()
    
    print(f"Your final score is: {player_score}")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()

