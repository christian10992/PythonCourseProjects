#this program will create a random number and allow the user to guess the number
#when the user guesses the number, it will tell the user how many tries it took

#import random module
import random

def main():
    #establish loop condition
    run = 'yes'
    while run == 'yes':
        #start the game
        game()
        #get user input to play again or not
        print('Would you like to play again?')
        playAgain = str(input('Enter yes or no: '))
        if playAgain != 'yes':
            run = 'no'
        #print farewell message
        print('Thanks for playing!')

def game():
    #initialize counter
    total = 1
    #assign a random number to a variable
    rand = random.randint(1,100)
    #get user input for first guess
    print('I am thinking of an integer between 1 and 100.')
    guess = int(input('Can you guess what it is? '))
    #initialize sentinel
    while guess !=rand:
        #control for high and low guess
        if guess>rand:
            print('Too high!')
            total += 1
        else:
            print('Too low!')
            total += 1
        guess = int(input('Guess again: '))
    #print winning statement
    print('Correct! You guessed the answer in ', total, 'tries!')
        
main()
