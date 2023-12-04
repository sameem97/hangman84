import unittest
from hangman import Hangman
from env_vars import word_list

class TestHangman(unittest.TestCase):
    def set_up(self):
        hangman = Hangman(word_list)