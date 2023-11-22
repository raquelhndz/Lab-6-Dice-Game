# Raquel Hernandez and Alice Huynh 
# 2/28/2023
# Dice Game
import check_input
import player

def take_turn(dice):
  '''Receives the Player object and rolls die. Calculates points '''

  dice.roll_dice()
  print(dice)

  has_pair = dice.has_pair()
  three_of_a_kind = dice.has_three_of_a_kind()
  series = dice.has_series()
  score = dice.get_points()
  
  if three_of_a_kind == True: 
    #check if it's 3 of a kind
    print("You got 3 of a kind!") #If true
  elif series == True: #if not 3 of a kind, check for series
      print("You got a series of 3!") #if true
  elif has_pair == False: #if not 3 of a kind or series, check if they are all different from each other
      print("Aww.  Too Bad")
  else: 
    print("You got a pair!")
    
  print("Score =", score)
  return score
  
def main():
  print("-Yahtzee-")
  print()
  dice = player.Player()
  while True:
    score = take_turn(dice)
    answer = check_input.get_yes_no("Do you want to play again? Y/N: ")
    print()
    if answer == False:
      print("Game over")
      print("Final Score =",score)
      break
main()


