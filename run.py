# import random module
import random


def random_word():
    '''
    Pick a random word from a list
    '''
    words = ['happy', 'computer', 'programming', 'successfully']

    pick_random = random.choice(words)
    create_jumble_word(pick_random)
    return pick_random


def create_jumble_word(word):
    '''
    Create jumbled word
    '''
    jumble_char = random.sample(word, len(word))
    jumble_word = ''.join(jumble_char)
    return jumble_word


def compare_words(guess_word, random_word):
    '''
    compare input with word
    '''
    if guess_word.lower() == random_word:
        print(f'Yes! You got it right. The correct word is {random_word}')
        return True
    elif guess_word.lower() != random_word:
        print('Wrong Answer. Try again!')
        return False


def store_score(score, name):
    '''
    Store the highscore in a txt file
    '''
    with open('highscore.txt', 'a') as file:
        file.write(f'{name} - {score}\n')


def game_over(lives, score):
    '''
    Game Over if lives are 0
    '''
    if lives == 0:
        print('Game Over! You Lost!')
        user_name = input('Type your name here\n')
        store_score(score, user_name)
        print(f'{user_name} your score is {score}')
        print('Game Over, Bye!')
        quit()


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
            result = compare_words(guess, picked_word)
            if result:
                score += 1
                print(f'Your score is {score}')
                print(f'You have {lives} lives')
                continue
            else:
                lives -= 1
                print(f'Your score is {score}')
                print(f'You have {lives} lives')
                game_over(lives, score)
                continue
            break
        elif play.lower() == 'q':
            quit()
        else:
            print('Please valid input. P to play, Q to quit\n')


main()
