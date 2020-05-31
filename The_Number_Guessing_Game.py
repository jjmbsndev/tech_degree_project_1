import random

lower_range = 1
upper_range = 10
random_number = 0
continue_game = False
ultimate_score = 0



def start_game():
  print("****************************************\n Welcome to the number one NUMBER guessing game!!!\n****************************************")
  random_number = random.randint(lower_range, upper_range)
  return random_number


def high_score(guess_counts, ultimate_scores):
  current_score = 0
  
  if guess_counts >= 11:
    current_score = 5
    
  else:
    current_score = 10 ** int((upper_range + 1) - guess_counts)
  
  if ultimate_scores < current_score and ultimate_scores != 0:
    print("You have the current high score: {}  Maybe you're not so bad after all!!!".format(current_score))
    return current_score
  
  elif ultimate_scores == current_score:
    print("You tied for the high score: {}... Meh...".format(current_score))
    return current_score
  
  elif ultimate_scores == 0:
    print("This game must've been reset, so you have the high score: {}  A newbie's luck!".format(current_score))
    return current_score
  
  else:
    print("You're pretty unlucky.  You scored: {}  You fell short of beating the high score: {}".format(current_score, ultimate_score))                       
    return ultimate_scores
  
  
def intra_game(ultimate_scored): 
  random_number = start_game()
  guess_count = 0
    
  while True:
      try:
        guess_number = input("Please pick a number between 1 and 10: ")
        guess_number = int(guess_number)
        
      except ValueError as err:
        print("Ooops, you haven't input an integer. Error: {}".format(err))
      
      else:
        if guess_number < lower_range or guess_number > upper_range:
          print("You entered a number outside of the range, try again!")
          guess_count += 1 
          continue
          
        elif guess_number < random_number:
          print("The number is higher, try again!")
          guess_count += 1     
          continue
                
        elif guess_number > random_number:
          print("The number is lower, try again!")
          guess_count += 1
          continue
                
        else:
          guess_count += 1
          print("You're lucky, you've guessed the correct number!: {}".format(random_number))
          
          if guess_count > 1:
            print("Too bad it only took you {} tries...HAHAHA".format(guess_count))
            return high_score(guess_count, ultimate_scored) 
            break
            
          else:
            print("Good guess, but you won't be so lucky next time!")
            return high_score(guess_count, ultimate_scored)
            break
            
                                   

ultimate_score = intra_game(ultimate_score)


while True:
  try:
    continue_playing = int(input("Would you like to play again? Enter number: (1) Yes or (2) No "))
    
  except ValueError as err:
    print("You entered an incorrect command.  Please try again.  Error: {}".format(err))
    
  except SyntaxError as err:
    print("You entered an incorrect command.  Please try again.  Error: {}".format(err))
    
  except NameError as err:
    print("You entered an incorrect command.  Please try again.  Error: {}".format(err))
    
  else:
    if continue_playing == 1:
      ultimate_score = intra_game(ultimate_score)
      continue
      
    elif continue_playing == 2:
      break
    
    
    
   