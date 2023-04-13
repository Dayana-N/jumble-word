# import random module
import random


def random_word():
    '''
    Pick a random word from a list
    '''
    words = ['happy', 'computer', 'programming', 'successfully']

    pick_random = random.choice(words)
    print(pick_random)
    return pick_random


def main():
    '''
    Pick a random word from a list
    '''

    while True:
        print('Welcome to Jumble Word')
        play = input('Press P to play or Q to quit\n')

        if play.lower() == 'p':
            random_word()
            break
        elif play.lower() == 'q':
            quit()
        else:
            print('Please valid input. P to play, Q to quit\n')


main()
