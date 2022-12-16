import random

print("Welcome to Rock Paper Scissors!")

# Set the options for the game
options = ["rock", "paper", "scissors"]

# Set the number of rounds
num_rounds = int(input("How many rounds would you like to play? "))

# Initialize the scores
player_score = 0
computer_score = 0

# Play the game
for round in range(num_rounds):
  # Get the player's choice
  player_choice = input("Choose rock, paper, or scissors: ").lower()

  # Check if the player's choice is valid
  if player_choice not in options:
    print("Invalid choice. Please try again.")
    continue

  # Get the computer's choice
  computer_choice = random.choice(options)

  # Determine the winner
  if player_choice == computer_choice:
    print("It's a tie!")
  elif player_choice == "rock" and computer_choice == "scissors":
    print("You win! Rock beats scissors.")
    player_score += 1
  elif player_choice == "scissors" and computer_choice == "paper":
    print("You win! Scissors beats paper.")
    player_score += 1
  elif player_choice == "paper" and computer_choice == "rock":
    print("You win! Paper beats rock.")
    player_score += 1
  else:
    print("You lose. {} beats {}.".format(computer_choice, player_choice))
    computer_score += 1

# Print the final scores
print("\nFinal scores:")
print("You: {}".format(player_score))
print("Computer: {}".format(computer_score))

# Determine the overall winner
if player_score > computer_score:
  print("Congratulations, you won!")
elif player_score < computer_score:
  print("Sorry, the computer won.")
else:
  print("It was a tie.")
