import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player1 = Player("Player1", "rock")
        self.player2 = Player("Player2", "paper")
        

    def test_player_has_name(self):
        self.assertEqual("Player1", self.player1.name)

    def test_player_has_choice(self):
        self.assertEqual("rock", self.player1.choice)

   
