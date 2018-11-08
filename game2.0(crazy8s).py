import random

WORD = ['apple', 'banana', 'cherry', 'watermelon', 'tomato', 'orange', 'jackfruit', 'cantaloupe', 'papaya', 'kumquat', 'Acai']

word = random.choice(WORD)
correct = word
clue = word[0] + word[(len(word)-1):(len(word))]
clue2 = 'fruit'
clue3 = 'You really want another clue? Really? Ok fine, its an english word. There happy?'
letter_guess = ''
word_guess = ''
store_letter = ''
count = 0
limit1 = (len(word)-1)
limit2 = len(word)
guess_limit= limit1 if len(word) > 4 else limit2
word_count = len(word)


print('Welcome to "Night Schools Guess Word Game!"')
print('You have',guess_limit,'guesses at guessing LETTERS in the secret word the secret word has:',word_count,'letters.')
print('Let\'s begin!')
print('\n')

while count < guess_limit:
    letter_guess = input('Guess a letter: ')

    if letter_guess in word:
        print('Right on the money!')
        store_letter += letter_guess
        count += 1

    if letter_guess not in word:
        print('Sorry that is incorrect')
        count += 1
        
    if count == 2:
        print('\n')
        clue_request = input("Would you like a clue?(type 'y' for yes and 'n' for no: ")
        if clue_request == 'y':
            print('\n')
            print('first CLUE:The word deals with', clue2 )
        if clue_request == 'n':
            print('Wow, you must be brave')
                
    if count == 4:
        print('\n')
        clue_request = input("Would you like a clue?(type 'y' for yes and 'n' for no: ")
        if clue_request == 'y':
            print('\n')
            print('second CLUE:The first and last letter of the word is: ', clue)
        if clue_request == 'n':
            print('Wow, you must be brave')


            if count == 6:
                print('\n')
        clue_request = input("Would you like a clue?(type 'y' for yes and 'n' for no: ")
        if clue_request == 'y':
            print('\n')
            print('Third CLUE:', clue3)
        if clue_request == 'n':
            print('Wow, you must be brave')








print('\n')
print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.')
print('These letters are: ', store_letter)
print('Remeber the secret word has:',len(word),'letters')
final = input('final guess time. Guess the Word:  ')
if final != WORD:
        print('that is incorrcet the word is:',word)
if final == WORD:
    print('You are correct! You must of googled it!')

    
    
