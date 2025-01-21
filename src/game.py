import random

class GuessingGame:
    def __init__(self, secret_number=None):
        self.secret_number = secret_number or random.randint(1, 100)

    def guess(self, number):
        if number == self.secret_number:
            return "Correct! You guessed the number."
        elif number < self.secret_number:
            return "Too low! Try again."
        else:
            return "Too high! Try again."
