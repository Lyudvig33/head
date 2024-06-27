
# Importing the random module for generating random words
import random


# Function to randomly select a word from a file
def random_words():
    with open('randomwords.txt','r') as file:
        words = file.read().split()
        rand = random.choice(words)
        return rand


# Function to return a list representations of hangman pictures
def picture():
    picture_list = ['''
       +---+
           |
           |
           |
          ===''', '''
       +---+
       O   |
           |
           |
          ===''', '''
       +---+
       O   |
       |   |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
      /    |
          ===''', '''
       +---+
       O   |
      /|\  |
      / \  |
          ===''']
    return picture_list

    
# Function to implement the hangman game
def hangman_game(word):

    # List to store guessed letters
    letters = []

    # List to store the display of the word with guessed letters
    output = []

    # Get the list of hangman pictures
    pict = picture()

    # Initialize the output list with '*' characters for each letter in the word
    for let in word:
        output.append('*')
    

    # Print the initial display of the word
    print('initial output', ''.join(output))

    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Index to track hangman picture displayed
    index = -1

    # Loop to play the game until the player wins or loses
    while(index < 7):

        # Increment the index to display the next hangman picture
        index += 1

        if index == len(pict) - 1:
            # Print the last hangman picture
            print(pict[6])

             # Print a message indicating loss
            print('You Lose, the word is: ', word)

            # Exit the loop since the player has lost
            break

        # Print the current hangman picture
        print(pict[index])
        
        # Prompt the player to input a letter and convert it to uppercase
        answer = input("Write Letter from " + ','.join(alphabet) + ' :' ).upper()

        # Check if the input letter is in the alphabet list
        if answer in alphabet:

            # Remove the input letter from the alphabet list
            alphabet.remove(answer)

         # Check if the input letter is in the word
        if answer in word:
            # Add the input letter to the list of guessed letters
            letters.append(answer)
             # Decremen the index to display the same hangman picture again
            index -= 1
      
         # Variable to track if the player has won
        hasWon = True
        for k, w in enumerate(word):
            if w not in letters:

                # Set hasWon to False if any letter in the word is not guessed
                hasWon = False

             # If the guessed letter is in the word
            if w == answer:

                # Update the output list with the guessed letter
                output[k] = w
                
        # Print the current display of the word
        print('output', ''.join(output))
         
        # If the player has guessed all letters in the word
        if hasWon:
            print("You Win")
            # Exit the loop since the player has won
            break

       


# Get a random word for the hangman game
word = random_words().upper()
hangman_game(word)













