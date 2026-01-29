#TERMINAL HANGMAN (CS50P FINAL PROJECT)
#SYED SALMAN HAIDER
#syed_2004_26
#Lahore, Pakistan
#29/01/2026

import time
import os
import random

def main():
    lives = 6
    guessed_letters = []
    display = []
    play = True
    run = True
    rules = False
    menu = True
    while run:
        while menu:
            clear()
            print('***A project of syed_2004_26 (SYED SALMAN HAIDER), Pak,Punjb,Lahre, Student of Prf.DAVID MALAN***')
            print('''_    _          _   _  _____ __  __          _   _
 | |  | |   /\\   | \\ | |/ ____|  \\/  |   /\\   | \\ | |
 | |__| |  /  \\  |  \\| | |  __| \\  / |  /  \\  |  \\| |
 |  __  | / /\\ \\ | . ` | | |_ | |\\/| | / /\\ \\ | . ` |
 | |  | |/ ____ \\| |\\  | |__| | |  | |/ ____ \\| |\\  |
 |_|  |_/_/    \\_\\_| \\_|\\_____|_|  |_/_/    \\_\\_| \\_|''', '\n')
            print('1. START GAME', '\n')
            print('2. RULES', '\n')
            print('3. QUIT GAME', '\n')

            choice = input('# ')

            if choice == '1':
                menu = False
                play = True
            elif choice == '2':
                clear()
                print('===RULES===', '\n')
                print('1. Guess the word letter by letter.', '\n')
                print('2. Each wrong guess costs you 1 life.', '\n')
                print('3. You have 6 lives total.', '\n')
                input('Press any button to return to main-menu.')
                clear()
            elif choice == '3':
                quit()
            else:
                continue

        while play:
            lives = 6
            guessed_letters = []
            clear()
            print('Loading Words.......', '\n', flush=True)
            time.sleep(3)
            words = words_extract('words.txt')
            print(f'{len(words)} words Loaded Successfully!')
            time.sleep(2)
            guess_word = word_picker(words)
            display = ['_' for i in range(len(guess_word))]
            clear()
            print('An english Word has been picked. You have to guess it!!')
            time.sleep(2)
            clear()
            print(display, '\n')
            while lives > 0:
                if '_' not in display:
                    clear()
                    print(f'The Word was: {guess_word}')
                    print()
                    print(r"""
  __     ______  _    _  __          ______  _   _ _
  \ \   / / __ \| |  | | \ \        / / __ \| \ | | |
   \ \_/ / |  | | |  | |  \ \  /\  / / |  | |  \| | |
    \   /| |  | | |  | |   \ \/  \/ /| |  | | . ` | |
     | | | |__| | |__| |    \  /\  / | |__| | |\  |_|
     |_|  \____/ \____/      \/  \/   \____/|_| \_(_)

    """)
                    time.sleep(3)
                    play = False
                    menu = True
                    break
                clear()
                draw(lives)
                print()
                print(f'Words guessed so far: {display}')
                print()
                print(f'Lives left: {lives}')
                print()
                guess = input('Guess a letter: ').strip().upper()

                if guess in guessed_letters:
                    clear()
                    print('Oops, you already tried this letter, try something else!')
                    time.sleep(2)
                    continue
                guessed_letters.append(guess)
                if word_match(guess, guess_word):
                    index = indices(guess, guess_word)
                    for i in index:
                        display[int(i)] = guess
                        clear()
                else:
                    lives -= 1
            if lives == 0:
                clear()
                draw(lives)
                print(f'The Word was: {guess_word}')
                print(r"""
   _____          __  __ ______    ______      ________ _____
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\

    """)
                time.sleep(3)
                play = False
                menu = True



def clear():
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for macOS and Linux
        _ = os.system('clear')


def words_extract(name):
    try:
        with open(name, 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        return f'Word file couldnt be loaded!'

def word_picker(words_list):
    word = random.choice(words_list).strip().upper()
    return word

def word_match(guess, guess_word): #guess is the letter we guessed, guess_word is the word we are guessing
    if guess in guess_word:
        return True
    else:
        return False


def indices(guess, guess_word):
    indices = []
    for i in range(len(guess_word)):
        if guess_word[i] == guess:
            indices.append(i)
    return indices


def draw(lives):
    if lives == 6:
        print("------------ ")
        print(" | ")
        print(" | ")
    elif lives == 5:
        print("------------ ")
        print(" | ")
        print(" | ")
        print(" O ")
    elif lives == 4:
        print("------------ ")
        print(" | ")
        print(" | ")
        print(" O ")
        print(" | ")
    elif lives == 3:
        print("------------ ")
        print(" | ")
        print(" | ")
        print(" O ")
        print("/| ")
    elif lives == 2:
        print("------------ ")
        print(" | ")
        print(" | ")
        print(" O ")
        print("/|\\")
    elif lives == 1:
        print("------------ ")
        print(" | ")
        print(" | ")
        print(" O ")
        print("/|\\")
        print("/  ")
    else:
        print("------------ ")
        print(" | ")
        print(" | ")
        print(" O ")
        print("/|\\")
        print("/ \\")





if __name__ == '__main__':
    main()
