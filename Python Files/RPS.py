#importing a library
import random

def get_choices():

#Define the default options to choose from
  options = ["rock", "paper", "scissors"]

#Get input from the player
  player_choice = input("Enter: ")

#Make computer randomly choose from the default options defined
  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def winner(player, computer):
  print(f"You: {player}, Computer:  {computer}")

#Game rules
  if player == computer:
    return "Tie!"
  elif player == "rock":
    if computer == "scissors":
      return "You win, Computer loses"
    else:
      return "You lose, Computer wins"
  elif player == "paper":
    if computer == "rock":
      return "You win, Computer loses"
    else:
      return "You lose, Computer wins"
  elif player == "scissors":
    if computer == "paper":
      return "You win, Computer loses"
    else:
      return "You lose, Computer wins"
  else:
    if player != "rock" or "paper" or "scissors":
      return "Enter proper input"

choice = get_choices()

result = winner(choice["player"], choice["computer"])
print(result)
