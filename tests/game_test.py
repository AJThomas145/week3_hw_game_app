import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.player = Player("Player1", "paper")
        
        

    def test_add_player_to_game(self):
        self.game.add_players_to_game(self.player)
        self.assertEqual(1, self.game.number_of_players())

    def test_which_player_wins(self):
        player1 = Player("Player1", "rock")
        player2 = Player("Player2", "paper")
        self.assertEqual("Player2 is the winner!!", self.game.who_wins(player1, player2))

    def test_which_player_wins_v2(self):
        player1 = Player("Player1", "rock")
        player2 = Player("Player2", "scissors")
        self.assertEqual("Player1 is the winner!!", self.game.who_wins(player1, player2))

    def test_which_player_wins_v3(self):
        player1 = Player("Player1", "rock")
        player2 = Player("Player2", "rock")
        self.assertEqual("No winner, play again!", self.game.who_wins(player1, player2))


    def test_which_player_wins_v4(self):
        player1 = Player("Player1", "paper")
        player2 = Player("Player2", "paper")
        self.assertEqual("No winner, play again!", self.game.who_wins(player1, player2))


    def test_which_player_wins_v5(self):
        player1 = Player("Player1", "paper")
        player2 = Player("Player2", "rock")
        self.assertEqual("Player1 is the winner!!", self.game.who_wins(player1, player2))


    def test_which_player_wins_v6(self):
        player1 = Player("Player1", "paper")
        player2 = Player("Player2", "scissors")
        self.assertEqual("Player2 is the winner!!", self.game.who_wins(player1, player2))


    def test_which_player_wins_v7(self):
        player1 = Player("Player1", "scissors")
        player2 = Player("Player2", "scissors")
        self.assertEqual("No winner, play again!", self.game.who_wins(player1, player2))


    def test_which_player_wins_v8(self):
        player1 = Player("Player1", "scissors")
        player2 = Player("Player2", "rock")
        self.assertEqual("Player2 is the winner!!", self.game.who_wins(player1, player2))


    def test_which_player_wins_v9(self):
        player1 = Player("Player1", "scissors")
        player2 = Player("Player2", "paper")
        self.assertEqual("Player1 is the winner!!", self.game.who_wins(player1, player2))

