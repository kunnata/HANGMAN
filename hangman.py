import random


languages = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(languages)
hidden = len(word) * '-'
lives = 8
guessed = []

print('H A N G M A N')

while True:
    welcome = input('Type "play" to play the game, "exit" to quit: ')
    if welcome == 'play':
        break
    elif welcome == 'exit':
        exit()
    else:
        continue

while True:
    random.seed()
    if lives > 0:
        print('')
        print(hidden)
        if hidden == word:
            print('You guessed the word!')
            print('You survived!')
            break
        letter = input('Input a letter: ')
        if len(letter) > 1 or letter == '':
            print('You should input a single letter')
            continue
        if not letter.isalpha() or letter != letter.lower():
            print('Please enter a lowercase English letter')
            continue
        if letter in guessed:
            print("You've already guessed this letter")
            continue
        if letter in set(word):
            position = 0

            for i in word:
                if i == letter:
                    guessed.append(i)
                    hidden = hidden[:position] + letter + hidden[position+1:]
                    position += 1
                else:
                    position += 1
        else:
            guessed.append(letter)
            lives -= 1
            print("That letter doesn't appear in the word")
    else:
        print("You lost!")
        break
