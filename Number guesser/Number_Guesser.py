import typing
import random


def get_guess():
    while True:
        guess = input('Enter your guess: ')
        if guess.isdigit() and int(guess) >= 0:
            print(f'returning {guess}')
            guess = int(guess)
            return guess
        elif guess == 'exit':
            print('Exiting the program')
            return -1
        else:
            print(f'Guess: {guess} is invalid.')


def update_win_loss(track, condition):
    if condition == 'win':
        track['win'] += 1
        track['pct'] = 100 * track['win'] / (track['win'] + track['loss'])
    elif condition == 'loss':
        track['loss'] += 1
        if track['win'] == 0:
            track['pct'] = 0
        else:
            track['pct'] = 100 * track['win'] / (track['win'] + track['loss'])
    print(f"Your record now is: wins: {track['win']}, losses: {track['loss']}, win percentage: {track['pct']}")
    return track


def number_guessing():
    won = True
    track = {'win': 0, 'loss': 0, 'pct': 0}
    while True:
        print('Starting a new game...')
        number = random.randint(0,10)
        for i in range(5):
            guess = get_guess()
            if guess == number:
                print(f'{guess} is the correct number! You win!')
                track = update_win_loss(track, 'win')
                won = True
                break
            elif guess < number:
                print('higher')
            elif guess > number:
                print('lower')
        if won:
            con = input('Do you want to continue? [yes/no]: ')
            if con == 'yes':
                won = False
                continue
            elif con == 'no':
                break
            else:
                print('Please provide yes or no')
        else:
            print(f'The correct number was: {number}. You lost')
            track = update_win_loss(track, 'loss')
            con = input('Do you want to continue? [yes/no]: ')
            if con == 'yes':
                continue
            elif con == 'no':
                break
            else:
                print('Please provide yes or no')


number_guessing()

