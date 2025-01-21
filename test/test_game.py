import pytest
from src.game import GuessingGame

def test_correct_guess():
    game = GuessingGame(secret_number=42)
    assert game.guess(42) == "Correct! You guessed the number."

def test_guess_too_low():
    game = GuessingGame(secret_number=42)
    assert game.guess(30) == "Too low! Try again."

def test_guess_too_high():
    game = GuessingGame(secret_number=42)
    assert game.guess(50) == "Too high! Try again."
