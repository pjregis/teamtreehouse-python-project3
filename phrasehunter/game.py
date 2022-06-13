import random
import string

from phrasehunter.phrase import Phrase


class Game:
    def __init__(self):
        self.phrases = []
        self.phrase_data = ['The Legend of Zelda', 'Maynard James Keenan',
                            'Mackenzie Grace', 'Cookies and Milk', 'Lupita Nyong\'o']
        self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = []
        self.missed = 0

    def create_phrases(self):
        phrases = []
        for data in self.phrase_data:
            phrases.append(Phrase(data))
        self.phrases = phrases

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print('============================')
        print('  W_lcom_ to Phras_ Hunt_r')
        print('============================')
        print('')
        print('Rules:')
        print('~ Guess letters until the phrase is revealed.')
        print('~ If you guess incorrectly, you will earn a miss.')
        print('~ Accumulate 5 misses and you lose.')
        print('')

    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print('')
            self.active_phrase.display(self.guesses)
            print(f'\nNumber missed: {self.missed}\n')
            while True:
                user_guess = self.get_guess()
                if user_guess in self.guesses:
                    print(f'You have already guessed "{user_guess}". Try again.')
                    continue
                if user_guess == '':
                    continue
                if user_guess not in string.ascii_lowercase or len(user_guess) > 1:
                    print('Invalid input. Try again.')
                else:
                    break
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
                print(f'Bummer! There is no "{user_guess}" in this phrase.\n')
        self.game_over()

    def get_guess(self):
        guess = input('Guess a letter: ').lower()
        return guess

    def game_over(self):
        if self.missed == 5:
            print('Oh no! You have missed too many. Game over :(')
        else:
            print('             ___________')
            print('            \'._==_==_=_.\'')
            print('            .-\:      /-.')
            print('           | (|:.     |) |')
            print('            \'-|:.     |-\'')
            print('              \::.    /')
            print('               \'::. .\'')
            print('                 ) (')
            print('               _.\' \'._')
            print('              `"""""""`')
            print('')
            print(f'The phrase was: {self.active_phrase}')
            print(f'Congratulations!! You are the new Phrase Hunter!')
            print('')

    def start_over(self):
        while True:
            play_again = input('Would you like to play again? Y/N >> ')
            if play_again.upper() == 'Y':
                return True
            elif play_again.upper() == 'N':
                return False
            else:
                print('Invalid input. Enter Y or N only.')


if __name__ == '__main__':
    pass


