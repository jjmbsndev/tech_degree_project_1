import random

lower_range = 1
upper_range = 10
random_number = 0
continue_game = False
high_score = 0


def start_game():
  print("****************************************\n Welcome to the number one NUMBER guessing game!!!\n****************************************")
  random_number = random.randint(lower_range, upper_range)
  return random_number

  
def intra_game(): 
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
            break
          else:
            print("Good guess, but you won't be so lucky next time!")
            break
            
            
intra_game()

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
      intra_game()
      continue
      
    elif continue_playing == 2:
      break
    
    
    
   