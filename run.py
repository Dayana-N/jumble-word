# import random module
import random


def random_word():
    '''
    Pick a random word from a list
    '''
    words = [
        'happy', 'computer', 'programming', 'successfully', 'apple', 'hello',
        'table', 'chair', 'car', 'ship', 'chicken', 'house', 'village',
        'build', 'shake', 'fuss', 'instal', 'bother', 'hay', 'draw', 'theory',
        'inch', 'impact', 'public', 'tell', 'danger', 'talk', 'tower', 'aware',
        'wreck', 'plant', 'witch', 'smell', 'dine', 'noble', 'snap', 'hole',
        'aloof', 'marine', 'ego', 'cart', 'list', 'wind', 'endure', 'cereal',
        'slime', 'cancer', 'anger', 'decade', 'owner', 'resign',
        'fun', 'hate', 'bitter', 'tent', 'color', 'infect', 'truck', 'bind',
        'layout', 'self', 'abbey', 'family', 'flight', 'panic', 'fame', 'rear',
        'sigh', 'era', 'text', 'salmon', 'double', 'god', 'air', 'truck',
        'gear', 'pray', 'jacket', 'word', 'aloof', 'border', 'sow', 'prison',
        'sunday', 'hot', 'spray', 'file', 'agile', 'debate', 'thrust',
        'regard', 'mutter', 'study', 'evoke', 'peel', 'page', 'instal',
        'coat', 'spy', 'halt', 'remedy', 'judge', 'pull', 'body', 'money',
        'novel', 'jelly', 'fever', 'gem',
        'creed', 'duke'
    ]

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


def game_is_over(score):
    '''
    Game Over if lives are 0
    '''
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
    while True:
        play = input('Press P to play or Q to quit\n')
        if play.lower() == 'p':
            game_over = False
            while not game_over:
                # pick random word and create jumbled version
                picked_word = random_word()
                jumble_picked_word = create_jumble_word(picked_word)
                print(f'Jumbled word is : {jumble_picked_word}')
                # ask the user to make a guess
                guess = input('Please type your guess here\n')
                result = compare_words(guess, picked_word)
                if result:
                    score += 1
                    print(f'Your score is {score}')
                    print(f'You have {lives} lives')
                else:
                    lives -= 1
                    print(f'Your score is {score}')
                    print(f'You have {lives} lives')
                    if lives == 0:
                        game_over = True
                        game_is_over(score)
                        break
        elif play.lower() == 'q':
            quit()
        else:
            print('Invalid input. Please enter P to play or Q to quit.')


main()
