# import random module
import random


def random_word():
    '''
    Pick a random word from a list
    '''
    words = ['happy', 'computer', 'programming', 'successfully']

    pick_random = random.choice(words)
    print(pick_random)
    create_jumble_word(pick_random)
    return pick_random


def create_jumble_word(word):
    '''
    Create jumbled word
    '''
    jumble_char = random.sample(word, len(word))
    jumble_word = ''.join(jumble_char)
    return jumble_word


def compare_words(jumbled_word, guess_word, random_word, lives):
    
    if guess_word.lower() == random_word:
        print(f'Yes! You got it right. The correct word is {random_word}')
        return True
    elif guess_word.lower() != random_word and lives > 0:
        print('Wrong Answer. Try again!')
        lives -= 1
        return False


def main():
    '''
    Pick a random word from a list
    '''
    score = 0
    lives = 3
    print('Welcome to Jumble Word')
    play = input('Press P to play or Q to quit\n')

    while True:
        if play.lower() == 'p':
            picked_word = random_word()
            jumble_picked_word = create_jumble_word(picked_word)
            print(f'Jumbled word is : {jumble_picked_word}')
            guess = input('Please type your guess here\n')
            result = compare_words(jumble_picked_word, guess, picked_word, lives)
            if result:
                score += 1
                print(f'Your score is {score}')
                continue
            else:
                lives -= 1
                print(f'Lives left {lives}')
                continue
            break
        elif play.lower() == 'q':
            quit()
        else:
            print('Please valid input. P to play, Q to quit\n')


main()
