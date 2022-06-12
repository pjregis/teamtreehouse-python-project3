import string


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def __eq__(self, other):
        return self.phrase == other.phrase

    def __str__(self):
        return self.phrase

    def display(self, guesses):
        for letter in self.phrase:
            if letter == ' ':
                print(' ', end=' ')
                continue
            if letter.lower() not in string.ascii_lowercase:
                print(letter, end=' ')
                continue
            if letter in guesses:
                print(f'{letter}', end=' ')
            else:
                print('_', end=' ')

    def check_guess(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in string.ascii_lowercase:
                continue
            if letter not in guesses:
                return False
        return True


if __name__ == '__main__':
    pass
