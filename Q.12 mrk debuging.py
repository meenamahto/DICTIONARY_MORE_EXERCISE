
##  MERAKI DEBUGING QUESTIONS 1------


# def numbers_less_than_twenty(list):
#   counter = 0
#   while counter < len(list):
#     item = list[counter]
#     if item > 20:
#       list.remove(item)
#     else:
#       counter += 1
#   return list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
# print ("Initial list", num_list)

# num_list_sub_20 = numbers_less_than_twenty(num_list)

# print ("Initial list", num_list)
# print ("List that doesn't contain numbers greate than 20", num_list_sub_20)





## QUESTIONS 2---


# from random import randint

# def win():
#     print ('You win!')

# def lose():
#     print ('You lose!')

# while True:
#     player_choice = input('What do you pick? (rock, paper, scissors)')
#     player_choice.strip()
#     random_move = randint(0, 2)
#     moves = ['rock', 'paper', 'scissors']
#     computer_choice = moves[random_move]

#     if player_choice == computer_choice:
#         print ('Draw!')
#     elif  player_choice== 'rock' and computer_choice == 'scissors':
#         win()
#     elif  player_choice== 'paper' and computer_choice == 'scissors':
#         lose()
#     elif player_choice == 'scissors' and computer_choice== 'paper':
#         win()
#     elif player_choice == 'scissors' and computer_choice== 'rock':
#         lose()
#     elif player_choice== 'paper' and computer_choice== 'rock':
#         win()
#     elif player_choice=="rock"  and computer_choice=="paper" :
#         lose()
#     again = input('Do you want to play again? (y or n):')
#     if 'again' == 'y':
#         continue
#     else:
#         break






##QUESTIONS 3---


# def encrypt():
#   message = input("Enter the message you want to encrypt")
#   ascii_message = [ord(char)+3 for char in message]
#   encrypt_message = [ chr(char) for char in ascii_message]  
#   print (''.join(encrypt_message))


# def decrypt():
#   message = input("Enter the message you want to decrypt")
#   ascii_message = [ord(char)-3 for char in message]
#   decrypt_message = [ chr(char) for char in ascii_message]  
#   print (''.join(decrypt_message))

# # flag = True
# while True:
#     choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
#     if choice =='e':
#         encrypt()
#     else:
#         choice = 'd'
#         decrypt()    
# # else:
#     play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
#     if play_again == 'y':
#         continue
#     # elif play_again == 'N':
#     else:
#         break




## QUESTION 4-----



# from random import randint # allows you to generate a random number

# # variables for the alien
# # alive = True
# stamin = 10

# # this function runs each time you attack the alien
# def report(stamin):
# # syntactic error in if else statements
#     if stamin > 8:
#         print ("The alien is strong! It resists your pathetic attack!")
#     elif stamin > 5:
#         print ("With a loud grunt, the alien stands firm.")
#     elif stamin > 3:
#         print ("Your attack seems to be having an effect! The alien stumbles!")
#     elif stamin > 0:
#         print ("The alien is certain to fall soon! It staggers and reels!")
#     else:
#         print ("That's it! The alien is finished!")

# # main function - accepts your input for fight with the alien
# def fight(stamin): # stamina
#     while stamin >0:
#       # won't enter this loop ever. The function will always return False.
#         response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run")
#         # chose a response from ( hit, attack, fight and run)
#         # fight scene
#         if "hit" in response or "attack" in response:
#             less = randint(0, stamin)
#             print(stamin,less)
#             stamin -= less # subtract random int from stamina
#             report(stamin) # see function above
#         elif "fight" in response:
#             less = randint(0, stamin)
#             print(stamin,less)
#             print ("Fight how? You have no weapons, silly space traveler!")
#         elif "run" in response:
#             less = randint(0, stamin)
#             print(stamin,less)
#             print ("Sadly, there is nowhere to run."),
#             print ("The spaceship is not very big.")
#         else:
#             less = randint(0, stamin)
#             print(stamin,less)
#             print ("The alien zaps you with its powerful ray gun!")
#             return True
#     return False

# print ("A threatening alien wants to fight you!\n")
# # quotes at the end.

# # call the function - what it returns will be the value of alive
# alive = fight(stamin)
# # print(alive)

# if alive==True: # means if alive == True
#     print ("\nThe alien lives on, and you, sadly, do not.\n")
# else:
#     print ("\nThe alien has been vanquished. Good work!\n")





##QUESTION 5-----

# print(list(range(10)))

import random
def getSecretNum(numDigits):
# Returns a string that is numDigits long, made up of unique random digits.
  numbers = list(range(10))
  random.shuffle(numbers)
  secretNum = ''
  for i in range(numDigits):
        # print(numbers[i])
        secretNum =secretNum+str(numbers[i])
  print (secretNum)

def getClues(guess, secretNum):
# Returns a string with the pico, fermi, None clues to the user.
  if guess == secretNum:
    return 'You got it!'
  clue = []
  for i in range(len(secretNum)):
        print(secretNum[i])
    #   for j in secretNum:
    # if i == i:
    #     clue.append('Fermi')
    # elif guess[i] in secretNum:
    #     clue.append('Pico')
    # if len(clue) == 0:
    #     return 'None'
    # return ' '.join(clue)

def isOnlyDigits(num):
# Returns True if num is a string made up only of digits. Otherwise returns False.
  if num == '':
    return False

  for i in num:
    if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
      return False

def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
  play = input("Do you want to play again? Yes or No?") 
  return play.lower.startswith('y')

# NUMDIGITS = 3
# MAXGUESS = 10

# print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')

while True:
    NUMDIGITS = 3
    MAXGUESS = 10
#   NUMDIGITS=int(input("Enter your number:"))  
    secretNum = getSecretNum(NUMDIGITS)
#   print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
    numGuesses = 0
    # guess=NUMDIGITS
    guess = input("Guess Again:")
    while numGuesses < len(guess):
        
        if len(guess) == NUMDIGITS :
            print ('Guess',"=", (guess[numGuesses]))
            # guess = int(input("Guess Again:"))
            numGuesses += 1
        clue = getClues(guess, secretNum)
        print(clue)
        # numGuesses += 1
        if guess == secretNum:
            break
        if numGuesses < MAXGUESS:
            print ('You ran out of guesses. The answer was ' ,'+' ,secretNum)
        if not playAgain:
            break


