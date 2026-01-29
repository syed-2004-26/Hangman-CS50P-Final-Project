TERMINAL HANGMAN (CS50P FINAL PROJECT)
Video Demo: <(https://youtu.be/D9Vak2DRNc0)>
Description:
By, syed_2004_26 (SYED SALMAN HAIDER)
Although my first ever coding project!
This is a classic, terminal-based Hangman game built with Python. I wanted to create something that felt like a real arcade experience, even though it runs entirely in a text-based console. The game features a full main menu (Play, Rules and Quit.), viewable rules, and dynamic ASCII art that updates as the player loses lives(The classic hangman ART).

How It Works:
When the game starts, it reads from a words.txt file and picks a random word. I implemented a "loading" phase to give it a bit of dramatic flair. The player has 6 lives to guess the word correctly. Each wrong guess updates a visual gallows, while correct guesses fill in the blanks(This could be refined further, but i used a raw list to display and store the words guessed correctly!). If you win or lose, the game presents a large ASCII banner of "YOU WIN" or "GAME OVER" and then loops you back to the main menu instead of just crashing to the terminal.(I have made use of boolean flags.)

File Breakdown:
project.py: This is the heart of the game. It contains the main game loop and several helper functions like word_picker, indices (to find letter positions), and words_extract (to handle file reading).

test_project.py: To make sure my logic didn't break during development, I wrote unit tests for the core functions using pytest.

words.txt: A plain text file containing a list of potential words for the game.(1000 words)

requirements.txt: Since I stuck to Python's standard libraries like os, time, and random, this file is mostly empty, but it's here to satisfy the submission requirements.

Design Choices:
One of the biggest decisions I made was using nested while loops to manage the game states (menu, play, and run). Originally, I just had the game run once and exit, but it felt "clunky." By adding a state-based menu, the player can check the rules or play multiple rounds without restarting the script.

Also the draw function, which prints the hangman is using if , elifs. I also found another way to implement that after a bit of research, which was to store them in a list and then return them by comparing them with lives as list indices. But anyways i kept it simple , as it was my first attempt!

I also chose to use a custom clear() function that checks the operating system (nt for Windows or posix for Mac/Linux). This ensures the terminal stays clean and the ASCII art doesn't just scroll endlessly down the screen, which keeps the focus on the current game state.

