import random
attempts_list = [] #pretend this is stored on the HDD in a text file. Note: Global variables should be avoided.
names_list = [] #same as above

def high_score():
  if len(attempts_list) != 0:
    best_score = min(attempts_list) #retrieves first element in list
    best_score_index = attempts_list.index(best_score) #retrieves index of the first element
    best_name = names_list[best_score_index] #retrieves the element from the names list that is in the index set above
    print("The current high score is {} attempts, ".format(min(attempts_list)) + "set by " + best_name)
    print()
    return
  print("There is currently no high score, it's yours for the taking!")
  print()

def random_number():
  random_number = int(random.randint(1, 10))
  return random_number

def check_guess(guess, rn, attempts):
  att = attempts
  if not guess.isdigit():
    return "The guess must be a number between 1 and 10"
  iGuess = int(guess)
  if iGuess > 10 or iGuess < 1:
    return "The guess must be between 1 and 10"
  if iGuess < rn:
    return "The target number is higher"
  if iGuess > rn:
    return "The target number is lower"
  if iGuess == rn:
    win_game(att)

def win_game(attempts):
  print("Nice! You got it!")
  print("It took you {} attempts".format(attempts))
  attempts_list.append(attempts)
  high_score()
  play_again()

def play_again():
  play_again_input = input("Would you like to play again? (Enter yes/no) ")
  if play_again_input.lower() == "no":
    print("That's cool, have a good one!")
    exit()
  if play_again_input.lower() == "yes":
    get_player_name()
  print("Please enter yes or no")
  play_again()

def get_player_name():
  player_name = input("What is your name? ")
  names_list.append(player_name)
  run_game(player_name)

def run_game(name):
  target = random_number()
  attempts = 0
  play = True
  print("Hi " + name + "!")
  high_score()
  while play:
    guess = input("Pick a number between 1 and 10: ")
    attempts += 1
    test = check_guess(guess, target, attempts)
    print(test)
    if test == "win":
      play = False

def start_game():
  print("Hello traveler! Welcome to the game of guesses!")
  get_player_name()

if __name__ == '__main__':
  start_game()
